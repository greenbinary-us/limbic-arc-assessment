"""
Finds the slide in the pptx that embeds the roadmap PNG (identified by image
dimensions 2560x1440 with the specific aspect-ratio of the roadmap) and
replaces its embedded blob with the freshly rendered roadmap.png.
Detects the right image by reading its embedded PNG IHDR.
"""
import struct, hashlib, os
from pptx import Presentation
from pptx.util import Inches

PPTX     = r'C:\Users\vmank\Documents\Code\GBClients\LimbicArc-assessment\limbic-arc-assessment\presentation\Limbic Arc Tech Assessment -  Briefing.pptx'
NEW_IMG  = r'C:\Users\vmank\Documents\Code\GBClients\LimbicArc-assessment\limbic-arc-assessment\presentation\images\roadmap.png'

def png_dims(blob):
    if blob[:8] != b'\x89PNG\r\n\x1a\n':
        return None, None
    return struct.unpack('>II', blob[16:24])

with open(NEW_IMG, 'rb') as f:
    new_blob = f.read()
new_w, new_h = png_dims(new_blob)
print(f"New roadmap image: {new_w}x{new_h}, {len(new_blob)} bytes")

prs = Presentation(PPTX)

replaced = 0
for slide_idx, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        if shape.shape_type == 13:  # MSO_SHAPE_TYPE.PICTURE
            blob = shape.image.blob
            w, h = png_dims(blob)
            if w is None:
                continue
            print(f"  Slide {slide_idx}: embedded image {w}x{h}, {len(blob)} bytes")
            # The roadmap is the only image rendered at 1280x720 source (2x = 2560x1440)
            # Identify it: all our diagrams are 2560x1440. Distinguish by blob content.
            # Check for the old "stop new debt" text by looking at the raw blob —
            # PNG stores text as deflated streams so we can't grep, but we can match
            # by file size range (roadmap.png was 217-218 KB at last render).
            if w == 2560 and h == 1440 and 200_000 < len(blob) < 260_000:
                print(f"    -> Looks like the roadmap. Replacing...")
                # Replace via the image part's blob directly
                shape.image.blob  # access to ensure loaded
                img_part = shape._pic.blipFill.blip.rEmbed
                slide_part = slide.part
                image_part = slide_part.related_part(img_part)
                image_part._blob = new_blob
                replaced += 1

print(f"\nReplaced {replaced} image(s).")
if replaced:
    prs.save(PPTX)
    print("Saved.")
else:
    print("No matching image found — check slide structure manually.")
