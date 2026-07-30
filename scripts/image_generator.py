"""
AI Image Generator for AstroAvatar Reels.
Generates vertical 9:16 artwork using Pollinations.ai or API providers.
Saves slide images to reels-factory/public/generated/<story_id>/
"""
import os
import shutil
import urllib.parse
import requests
from typing import List, Dict, Any

POLLINATIONS_BASE_URL = "https://image.pollinations.ai/prompt/"

def generate_slide_images(story_data: Dict[str, Any], output_dir: str) -> List[Dict[str, Any]]:
    """
    Generates images for all slides in story_data and returns updated slides with staticFile path.
    """
    story_id = story_data["story_id"]
    target_folder = os.path.join(output_dir, "generated", story_id)
    os.makedirs(target_folder, exist_ok=True)

    updated_slides = []
    slides = story_data.get("slides", [])

    print(f"[Image Gen] Generating {len(slides)} vertical slideshow images for story: {story_id}")

    for slide in slides:
        idx = slide["slide_index"]
        prompt = slide["image_prompt"] + ", vertical 9:16 aspect ratio, high resolution oil painting, hindu mythology epic cinematic lighting, vibrant gold dark teal cosmic colors"
        filename = f"slide_{idx:02d}.png"
        filepath = os.path.join(target_folder, filename)
        remotion_file_path = f"generated/{story_id}/{filename}"

        # Check if file already exists
        if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
            print(f"  - Slide {idx:02d}: Already exists ({remotion_file_path})")
        else:
            success = download_pollinations_image(prompt, filepath)
            if not success:
                # Fallback to copy placeholder slide
                print(f"  - Slide {idx:02d}: Fallback to default slide plate")
                create_fallback_slide(filepath)

        slide_copy = dict(slide)
        slide_copy["file"] = remotion_file_path
        updated_slides.append(slide_copy)

    return updated_slides

def download_pollinations_image(prompt: str, save_path: str) -> bool:
    """Downloads AI generated image from Pollinations.ai API."""
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{POLLINATIONS_BASE_URL}{encoded_prompt}?width=1080&height=1920&nologo=true&seed=42&model=flux"
    try:
        res = requests.get(url, timeout=25)
        if res.status_code == 200 and len(res.content) > 5000:
            with open(save_path, "wb") as f:
                f.write(res.content)
            print(f"  - Downloaded AI Image -> {save_path} ({len(res.content)//1024} KB)")
            return True
    except Exception as e:
        print(f"  [Image Gen Error] Pollinations download failed: {e}")
    return False

def create_fallback_slide(save_path: str):
    """Creates a basic dark blue cosmic gradient fallback slide if generator fails."""
    # Copy from existing format-b slide if available
    default_source = "reels-factory/public/formats/slideshow/slide-01-title.png"
    if os.path.exists(default_source):
        shutil.copy(default_source, save_path)
    else:
        # Save empty placeholder byte file
        with open(save_path, "wb") as f:
            f.write(b"")
