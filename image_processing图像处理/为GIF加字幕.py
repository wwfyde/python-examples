from PIL import Image, ImageDraw, ImageFont
import imageio

# Load the GIF
gif_path = "/mnt/data/Screen Recording 2024-07-14 at 22.20.15.gif"
gif = imageio.mimread(gif_path)

# Define the font and size
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)

# Define the text to add
text = "嗯!"

# Determine text size
text_width, text_height = font.getsize(text)

# Process each frame
frames = []
for frame in gif:
    pil_frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_frame)

    # Calculate text position (centered)
    frame_width, frame_height = pil_frame.size
    text_x = (frame_width - text_width) / 2
    text_y = frame_height - text_height - 10  # slightly above the bottom

    # Add text to the frame
    draw.text((text_x, text_y), text, font=font, fill="white")

    frames.append(pil_frame)

# Save the new GIF
output_path = "/mnt/data/Screen_Recording_with_subtitle.gif"
frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=100)

output_path
