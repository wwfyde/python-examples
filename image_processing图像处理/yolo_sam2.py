from PIL import Image
from ultralytics import SAM
import numpy as np
import cv2

# Load a model
model = SAM("sam2.1_b.pt")

# Display model information (optional)
model.info()

# Run inference with bboxes prompt
file_path = "//b3fbf1a7-fe19-41b3-b640-0b4db8c5e356.png"

results = model(file_path, bboxes=[100, 100, 200, 200])
# mask = results[0].masks
print(results)
mask = results[0].masks.data[0].cpu().numpy()  # 获取第一个掩码，转换为 NumPy 数组

# 确保掩码是二值化的 (0 或 1)
mask = mask.astype(np.uint8)  # 转换为 uint8 类型
mask[mask > 0] = 1  # 二值化处理

image = cv2.imread(file_path)  # 读取图像 (BGR 格式)


# 4. 应用掩码扣取对象
# 将图像转换为 RGBA 格式以支持透明背景
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换为 RGB
image_rgba = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2RGBA)  # 添加 alpha 通道

# 创建透明背景图像
output_image = np.zeros_like(image_rgba)
output_image[:, :, :3] = image_rgb  # 复制 RGB 通道
output_image[:, :, 3] = (
    mask * 255
)  # 设置 alpha 通道：掩码区域为 255（不透明），其他为 0（透明）

# 5. 保存扣取的对象（透明背景）
output_pil = Image.fromarray(output_image)
output_pil.save("output_object.png")  # 保存为 PNG 以保留透明度

# 6. 可选：显示结果
cv2.imshow("Deducted Object", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
