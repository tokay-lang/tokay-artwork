#!/usr/bin/python3
"""
Generates README.md with rendered versions of the provided images
"""

import os, glob, cairosvg, PIL

output_folder = "rendered"
output_width = 2000

os.makedirs(output_folder, exist_ok=True)

print("""# Tokay Artwork

This repostitory contains artwork relating the [Tokay programming language](https://tokay.dev). It is licensed by Creative Commons CC-BY-SA 4.0.

The artwork was initially created and designed by [Timmytiefkuehl](https://github.com/timmytiefkuehl).

---
""")

for svg in sorted(glob.glob("*.svg")):
	base = svg.removesuffix(".svg")

	# generate png from svg
	png = os.path.join(output_folder, base + ".png")
	cairosvg.svg2png(url=svg, write_to=png, output_width=output_width)
	svg.removesuffix(".svg") + ".png"

	# generate webp from png
	webp = os.path.join(output_folder, base + ".webp")
	image = PIL.Image.open(png)
	image.save(webp, format="webp")

	print(f"## {base}\n")
	print("\n".join([f"### {x}\n![{x}]({x})\n" for x in [svg, png, webp]]))

