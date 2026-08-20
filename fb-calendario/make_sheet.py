import os
from PIL import Image, ImageDraw, ImageFont

base = "/opt/data/tlaloc-repo/fb-calendario/creativos"
cols, rows = 5, 6
tile = 340
gap = 8
label_h = 34

W = cols * tile + (cols + 1) * gap
H = rows * (tile + label_h) + (rows + 1) * gap

sheet = Image.new("RGB", (W, H), (20, 24, 34))
draw = ImageDraw.Draw(sheet)

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except:
    font = ImageFont.load_default()

for i in range(1, 31):
    r = (i - 1) // cols
    c = (i - 1) % cols
    x = gap + c * (tile + gap)
    y = gap + r * (tile + label_h + gap)
    fn = os.path.join(base, f"day{i:02d}.png")
    im = Image.open(fn).convert("RGB").resize((tile, tile), Image.LANCZOS)
    sheet.paste(im, (x, y))
    draw.rectangle([x, y + tile, x + tile, y + tile + label_h], fill=(30, 34, 46))
    draw.text((x + 8, y + tile + 5), f"Día {i:02d}", fill=(255, 255, 255), font=font)

out = "/opt/data/tlaloc-repo/fb-calendario/contact-sheet.png"
sheet.save(out, optimize=True)
print("OK", out, sheet.size)