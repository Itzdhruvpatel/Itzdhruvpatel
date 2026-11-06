"""Turns rendered frames into the animated images the README shows. Needs Pillow and render/frames from index.html."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
ASSETS = HERE.parent / "assets"
FONT = r"C:\Windows\Fonts\bahnschrift.ttf"
SIZE = (1200, 507)
PAPER, MUTED = (240, 238, 232, 255), (160, 166, 176, 255)

PLATES = {
    "bay-atlas": ("#ff7a2e", "01", "ATLAS", "A firewall for AI agents", [("3/12", "secrets leaked, no firewall"), ("0/12", "secrets leaked, firewall on"), ("18/20", "normal tasks still pass")], "Small test on one real model"),
    "bay-trustcheck": ("#4cc0ff", "02", "TRUSTCHECK", "Should you act on this message?", [("4", "signals scored per message"), ("LIVE", "Chrome call guard")], "Team build for D3COY"),
    "bay-agrix": ("#63e87a", "03", "AGRIX", "AI smart farming assistant", [("98.7%", "crop recommendation accuracy"), ("90.22%", "disease detection accuracy"), ("90K+", "images in the dataset")], "Python, TensorFlow, Random Forest"),
    "bay-nss": ("#ffc846", "04", "DJS NSS", "Official site and event sign-ups", [("100s", "of student registrations"), ("2", "event portals shipped")], "Team build in React and Tailwind"),
}


def font(size, weight="SemiBold"):
    face = ImageFont.truetype(FONT, size)
    face.set_variation_by_name(weight)
    return face


def spaced(draw, x, y, text, face, fill, gap):
    for char in text:
        draw.text((x, y), char, font=face, fill=fill)
        x += draw.textlength(char, font=face) + gap


def hero_overlay():
    layer = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for y in range(350, SIZE[1]):
        draw.line([(0, y), (SIZE[0], y)], fill=(0, 0, 0, int(205 * (y - 350) / (SIZE[1] - 350))))
    spaced(draw, 46, 402, "DHRUV PATEL", font(44, "Bold"), PAPER, 7)
    draw.text((47, 456), "IT at DJSCE, Mumbai. AI security, machine learning, fast websites.", font=font(19, "Regular"), fill=MUTED)
    return layer


def plate_overlay(colour, number, name, subtitle, stats, foot):
    layer = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for x in range(0, 660):
        draw.line([(x, 0), (x, SIZE[1])], fill=(0, 0, 0, int(250 * max(0, 1 - x / 660) ** 0.55)))
    draw.text((46, 38), f"BAY {number}" if number.isdigit() else number, font=font(16), fill=colour)
    draw.text((44, 62), name, font=font(50, "Bold"), fill=PAPER)
    draw.text((46, 122), subtitle, font=font(19, "Regular"), fill=MUTED)
    y = 178
    for value, label in stats:
        draw.text((46, y), value, font=font(38, "Bold"), fill=colour)
        draw.text((46, y + 45), label, font=font(15, "Regular"), fill=MUTED)
        y += 84
    draw.text((46, SIZE[1] - 38), foot, font=font(14, "Regular"), fill=MUTED)
    return layer


def finish_overlay():
    layer = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for y in range(330, SIZE[1]):
        draw.line([(0, y), (SIZE[0], y)], fill=(0, 0, 0, int(210 * (y - 330) / (SIZE[1] - 330))))
    spaced(draw, 46, 402, "END OF THE LAP", font(44, "Bold"), PAPER, 7)
    draw.text((47, 456), "Thanks for stopping by the garage. Next build is already on the lift.", font=font(19, "Regular"), fill=MUTED)
    return layer


def build(name, overlay):
    if not (HERE / "frames" / name).exists():
        return
    frames = []
    for path in sorted((HERE / "frames" / name).glob("*.png")):
        frame = Image.open(path).convert("RGB").resize(SIZE, Image.LANCZOS).convert("RGBA")
        frames.append(Image.alpha_composite(frame, overlay).convert("RGB"))
    if not frames:
        raise SystemExit(f"no frames for {name}")
    out = ASSETS / f"{name}.webp"
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=83, loop=0, quality=74, method=5)
    print(name, len(frames), "frames", round(out.stat().st_size / 1e6, 2), "MB")


build("hero", hero_overlay())
build("finish", finish_overlay())
tools = Image.new("RGBA", SIZE, (0, 0, 0, 0))
build("tools", tools)
for image, plate in PLATES.items():
    build(image, plate_overlay(*plate))
