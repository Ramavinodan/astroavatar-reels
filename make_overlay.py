import math
from PIL import Image, ImageDraw, ImageFont

# Dimensions
W, H = 720, 1280
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Load font
try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 36)
except:
    font = ImageFont.load_default()

text = "Follow us on Facebook & Instagram"
# Get text size using textbbox
bbox = font.getbbox(text)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

# Position text
y_text = 820
x_text = (W - tw) // 2

# Draw text shadow
draw.text((x_text + 2, y_text + 2), text, font=font, fill=(0, 0, 0, 200))
# Draw text
draw.text((x_text, y_text), text, font=font, fill=(255, 248, 231, 255))

# Load logos
fb = Image.open("fb.png").convert("RGBA")
ig = Image.open("ig.png").convert("RGBA")

# Resize logos to 60x60
fb = fb.resize((60, 60), Image.Resampling.LANCZOS)
ig = ig.resize((60, 60), Image.Resampling.LANCZOS)

# Position logos
gap = 40
total_w = 60 + gap + 60
start_x = (W - total_w) // 2
y_logos = y_text + th + 20

# Paste logos
overlay.paste(fb, (start_x, y_logos), fb)
overlay.paste(ig, (start_x + 60 + gap, y_logos), ig)

overlay.save("overlay.png")
