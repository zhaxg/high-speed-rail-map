import os, math, argparse
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

parser = argparse.ArgumentParser(description='Generate DZI tiles from an image')
parser.add_argument('input', help='Input image path')
parser.add_argument('-o', '--output', help='Output directory name (default: input filename without extension)')
parser.add_argument('--tile-size', type=int, default=254, help='Tile size (default: 254)')
parser.add_argument('--overlap', type=int, default=1, help='Tile overlap (default: 1)')
parser.add_argument('--quality', type=int, default=85, help='JPEG quality (default: 85)')
args = parser.parse_args()

img = Image.open(args.input)
w, h = img.size
tile_size = args.tile_size
overlap = args.overlap
fmt = 'jpg'

out_name = args.output or os.path.splitext(os.path.basename(args.input))[0]
out_dir = os.path.join(os.path.dirname(args.input) or '.', out_name)
files_dir = os.path.join(out_dir, f'{out_name}_files')

max_dim = max(w, h)
num_levels = int(math.ceil(math.log2(max_dim))) + 1

print(f'Input: {args.input} ({w}x{h})')
print(f'Output: {out_dir}')
print(f'Zoom levels: {num_levels}')

os.makedirs(files_dir, exist_ok=True)

dzi_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<Image xmlns="http://schemas.microsoft.com/deepzoom/2009"
       TileSize="{tile_size}"
       Overlap="{overlap}"
       Format="{fmt}">
  <Size Width="{w}" Height="{h}" />
</Image>'''

with open(os.path.join(out_dir, f'{out_name}.dzi'), 'w') as f:
    f.write(dzi_content)

total = 0
for level in range(num_levels):
    scale = 2 ** (num_levels - 1 - level)
    lw = math.ceil(w / scale)
    lh = math.ceil(h / scale)
    level_dir = os.path.join(files_dir, str(level))
    os.makedirs(level_dir, exist_ok=True)
    cols = max(1, math.ceil((lw - overlap) / (tile_size - overlap)))
    rows = max(1, math.ceil((lh - overlap) / (tile_size - overlap)))
    resized = img.resize((lw, lh), Image.LANCZOS) if scale > 1 else img
    for row in range(rows):
        for col in range(cols):
            x0 = col * (tile_size - overlap)
            y0 = row * (tile_size - overlap)
            x1 = min(x0 + tile_size, lw)
            y1 = min(y0 + tile_size, lh)
            tile = resized.crop((x0, y0, x1, y1))
            tile.save(os.path.join(level_dir, f'{col}_{row}.{fmt}'), quality=args.quality)
            total += 1

print(f'Done: {total} tiles')
