#!/usr/bin/env python3
"""Replace only the figure titles in the original images. Keep everything else intact."""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

def find_title_y(img_arr, half='left', threshold=200):
    """Find the y row where title text starts by scanning for dark pixels near top."""
    w = img_arr.shape[1]
    x_start = 0 if half == 'left' else w // 2
    x_end   = w // 2 if half == 'left' else w
    # Scan top 80px for the title text band
    for y in range(5, 80):
        row = img_arr[y, x_start:x_end, :3]
        dark = np.sum(row < threshold, axis=1)
        if np.any(dark == 3):  # found a dark pixel (text)
            return y
    return 20

def replace_title(img_path, out_path, left_title, right_title):
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img)
    w, h = img.size

    # Detect background colour from top-left corner
    bg_color = tuple(arr[3, 3, :3].tolist())  # usually white or near-white

    draw = ImageDraw.Draw(img)

    # Try to load a font similar to the original (DejaVu Sans / default)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)
    except:
        font = ImageFont.load_default()

    # White-out top title band for each half, then write new title
    half_w = w // 2
    title_band_h = 38  # pixels to blank

    for side, title in [('left', left_title), ('right', right_title)]:
        x0 = 0       if side == 'left' else half_w
        x1 = half_w  if side == 'left' else w

        # Blank the title area
        draw.rectangle([x0, 0, x1, title_band_h], fill=bg_color)

        # Measure text width to centre it
        bbox = draw.textbbox((0, 0), title, font=font)
        tw = bbox[2] - bbox[0]
        cx = x0 + (half_w - tw) // 2
        draw.text((cx, 8), title, fill=(0, 0, 0), font=font)

    img.save(out_path, dpi=(300, 300))
    print(f'Saved: {out_path}')

# orig_fig_2 = Figure 2 (left) + Figure 3 (right)
replace_title(
    '/home/user/Skill/orig_fig_2.png',
    '/home/user/Skill/figure2_combined.png',
    left_title  = '(a) k-Means Cluster Analysis of Airshed Regimes',
    right_title = '(b) Seasonal Dynamics of Coarse Fraction'
)

# orig_fig_1 = Figure 4 (left) + Figure 5 (right)
replace_title(
    '/home/user/Skill/orig_fig_1.png',
    '/home/user/Skill/figure3_combined.png',
    left_title  = '(a) Diurnal Cycle of Resuspension vs Ratio',
    right_title = '(b) Spearman Correlation Matrix'
)

# orig_fig_0 = Figure 6 (left) + Figure 7 (right)
replace_title(
    '/home/user/Skill/orig_fig_0.png',
    '/home/user/Skill/figure4_combined.png',
    left_title  = '(a) Weekly Anthropogenic Cycle',
    right_title = '(b) Seasonal Regression Slopes'
)

print('\nDone — all titles replaced, images otherwise unchanged.')
