from pathlib import Path

from PIL import Image

path = Path(__file__).parent / "image.png"

image = Image.open(path)
img_width, img_heighgt = image.size
center_x = img_width // 2
center_y = img_heighgt // 2

# 确定剪裁区域
crop_width, crop_height = 400, 400
left = center_x - crop_width // 2
top = center_y - crop_height // 2
right = center_x + crop_width // 2
bottom = center_y + crop_height // 2
pass

cropped_image = image.crop((left, top, right, bottom))
canvas = Image.new("RGBA", image.size, (0, 0, 0, 0))
crop_width, crop_height = cropped_image.size
paste_x = (img_width - crop_width) // 2
paste_y = (img_heighgt - crop_height) // 2

# 将裁剪图像粘贴到中心
canvas.paste(cropped_image, (paste_x, paste_y))

background = Image.new("RGBA", image.size, (0, 0, 0, 0))
result = Image.composite(image, background, canvas)
result.show()
