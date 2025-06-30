#!/usr/bin/python3
"""
Generates README.md with rendered versions of the provided images
"""

import os, glob, cairosvg, PIL

output_folder = "rendered"
output_widths = [400, 800, 1200, 1600]

os.makedirs(output_folder, exist_ok=True)

print("""# Tokay Artwork

This repostitory contains artwork relating the [Tokay programming language](https://tokay.dev). It is licensed by Creative Commons CC-BY-SA 4.0.

The artwork was initially created and designed by [Timmytiefkuehl](https://github.com/timmytiefkuehl).

The font used by the Logo is [Changa](https://fonts.google.com/specimen/Changa).

---
""")

for svg in sorted(glob.glob("*.svg")):
	base = svg.removesuffix(".svg")

	print(f"## {base}\n")
	print("\n".join([f"### {name}\n![{name}]({name})\n" for name in [svg]]))

	for width in output_widths:
		# generate png from svg
		png = os.path.join(output_folder, f"{base}-{width}.png")
		cairosvg.svg2png(url=svg, write_to=png, output_width=width)
		svg.removesuffix(".svg") + ".png"

		# generate webp from png
		webp = os.path.join(output_folder, f"{base}-{width}.webp")
		image = PIL.Image.open(png)
		image.save(webp, format="webp")

		print("\n".join([f"#### {name}\n![{name}]({name})\n" for name in [png, webp]]))
