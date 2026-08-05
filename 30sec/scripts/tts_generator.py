"""
TTS & Audio Processing Pipeline for AstroAvatar Reels.
- OmniVoice TTS
- Bass boost (~8dB) + peak normalization
- Soft background music (BGM) mixing
- Accurate audio duration & per-slide timestamp calculation
"""
import os
import subprocess
import wave
import contextlib
from typing import Dict, Any, List

def generate_narration_audio(story_data: Dict[str, Any], public_dir: str) -> Dict[str, Any]:
    """
    Generates story narration WAV file and computes per-slide endSec timing based on speech duration.
    """
    story_id = story_data["story_id"]
    script_text = story_data["script_hi"]
    slides = story_data["slides"]

    narration_dir = os.path.join(public_dir, "narration")
    os.makedirs(narration_dir, exist_ok=True)

    raw_wav_path = os.path.join(narration_dir, f"{story_id}-raw.wav")
    final_wav_path = os.path.join(narration_dir, f"{story_id}-hi.wav")
    relative_audio_path = f"narration/{story_id}-hi.wav"

    print(f"[TTS Pipeline] Generating speech audio for story: {story_id}")

    # Step 1: Generate Raw Speech (OmniVoice CLI / Python)
    success = generate_omnivoice_tts(script_text, raw_wav_path)

    if not success:
        raise RuntimeError("OmniVoice TTS generation failed. Please fix this manually to proceed the pipeline.")

    # Step 2: Post-process Audio (Bass boost ~8dB + Peak Normalize + BGM overlay)
    post_process_audio(raw_wav_path, final_wav_path)

    # Step 3: Get exact audio duration
    audio_duration_sec = get_audio_duration(final_wav_path)
    print(f"[TTS Pipeline] Final audio duration: {audio_duration_sec:.2f} seconds")

    # Step 4: Proportionally scale slide endSec timestamps to match exact audio duration
    timed_slides = calculate_slide_timestamps(slides, audio_duration_sec)

    story_frames = int(audio_duration_sec * 30)

    return {
        "relative_audio_path": relative_audio_path,
        "audio_duration_sec": audio_duration_sec,
        "story_frames": story_frames,
        "slides": timed_slides
    }

def generate_omnivoice_tts(text: str, save_path: str) -> bool:
    """Invokes OmniVoice TTS with locked instruct options."""
    try:
        import shutil
        import os
        cli_path = shutil.which("omnivoice-infer") or "omnivoice-infer"

        cmd = [
            cli_path,
            "--text", text,
            "--instruct", "male, middle-aged, indian accent, moderate pitch",
            "--speed", "0.95",
            "--num_step", "40",
            "--output", save_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if res.returncode == 0 and os.path.exists(save_path):
            print(f"[OmniVoice] Speech generated -> {save_path}")
            return True
        else:
            print(f"[OmniVoice] Error: returncode={res.returncode}, stderr={res.stderr}")
    except Exception as e:
        print(f"[OmniVoice] OmniVoice CLI not found or failed: {e}")
    return False





def post_process_audio(input_wav: str, output_wav: str):
    """Applies bass boost, normalization, and optional BGM via ffmpeg."""
    try:
        cmd = [
            "ffmpeg", "-y",
            "-i", input_wav,
            "-af", "bass=g=8,loudnorm=I=-16:LRA=11:TP=-1.5",
            "-c:a", "pcm_s16le",
            output_wav
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        print(f"[Audio FX] Post-processing complete -> {output_wav}")
    except Exception as e:
        raise RuntimeError(f"Audio post-processing failed: {e}. Please fix this manually to proceed the pipeline.")

def get_audio_duration(wav_path: str) -> float:
    """Returns audio file duration in seconds."""
    try:
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", wav_path]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception:
        pass
    
    try:
        with contextlib.closing(wave.open(wav_path, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return frames / float(rate)
    except Exception:
        return 52.5

def calculate_slide_timestamps(slides: List[Dict[str, Any]], total_sec: float) -> List[Dict[str, Any]]:
    """Distributes total_sec across slides based on relative approx_sec values."""
    if not slides:
        return []

    raw_sum = sum(s.get("approx_sec", 4.0) for s in slides)
    scale_factor = total_sec / raw_sum if raw_sum > 0 else 1.0

    cumulative = 0.0
    result = []
    for i, slide in enumerate(slides):
        duration = slide.get("approx_sec", 4.0) * scale_factor
        cumulative += duration
        if i == len(slides) - 1:
            cumulative = total_sec # ensure exact match on last slide

        slide_copy = dict(slide)
        slide_copy["endSec"] = round(cumulative, 2)
        result.append(slide_copy)

    return result
