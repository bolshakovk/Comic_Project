from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap

source_path = r'C:\Users\bolsh\.gemini\antigravity\brain\ac323aa2-4fed-4b1f-9644-c337e40e4da2\media__1777220127908.jpg'
dest_path = r'edited_loading_screen.jpg'

text = "все началось с хаствуда, который рубил деревья на столько яростно, что придя в дом, он зарубил свою семью, он долго горевал, но черный алмаз нашел его, на землях вов сируса начался коричневый поход..."

# Load image
img = Image.open(source_path)
draw = ImageDraw.Draw(img, 'RGBA')

# The text bounding box will be approximately right-middle to bottom
box_x = 480
box_y = 310
box_width = 460
box_height = 180

# Dark semi-transparent patch to cover old text
patch = Image.new('RGBA', (box_width, box_height), (20, 15, 10, 180))
img.paste(patch, (box_x, box_y), patch)

# Setup font
try:
    font_path = r'C:\Windows\Fonts\times.ttf'
    font = ImageFont.truetype(font_path, 18)
except:
    font = ImageFont.load_default()

# Wrap text
wrapped_text = textwrap.fill(text, width=45)

# Calculate text drawing position
# To center text inside the bounding box
# Get text bounding box for positioning
text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, align="center")
t_w = text_bbox[2] - text_bbox[0]
t_h = text_bbox[3] - text_bbox[1]

text_x = box_x + (box_width - t_w) // 2
text_y = box_y + (box_height - t_h) // 2

# Draw black outline/shadow first
shadow_offset = 2
outline_color = (0, 0, 0, 255)
draw.multiline_text((text_x + shadow_offset, text_y + shadow_offset), wrapped_text, font=font, fill=outline_color, align="center")
draw.multiline_text((text_x - 1, text_y - 1), wrapped_text, font=font, fill=outline_color, align="center")
draw.multiline_text((text_x + 1, text_y - 1), wrapped_text, font=font, fill=outline_color, align="center")
draw.multiline_text((text_x - 1, text_y + 1), wrapped_text, font=font, fill=outline_color, align="center")
draw.multiline_text((text_x + 1, text_y + 1), wrapped_text, font=font, fill=outline_color, align="center")

# Draw text in pale gold (WC3 style)
text_color = (255, 214, 133, 255)
draw.multiline_text((text_x, text_y), wrapped_text, font=font, fill=text_color, align="center")

img.save(dest_path, "JPEG", quality=95)
print(f"Saved generated image to {dest_path}")
