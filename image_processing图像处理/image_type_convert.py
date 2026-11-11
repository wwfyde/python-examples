from pathlib import Path

import torch
import numpy as np
from PIL import Image, ImageOps


def path_pil(image: Path) -> Image.Image:
    image = Image.open(image)
    # image.show()
    return image


def pil2tensor(image: Image.Image) -> torch.Tensor:
    image = ImageOps.exif_transpose(image)  # 真实旋转图片
    image = image.convert("RGB")
    image = np.array(image).astype(np.float32) / 255.0
    image = torch.from_numpy(image)
    print(image.shape, image.size())
    image_new = image[None,]
    print(image_new.shape, image_new.size())
    return image, image_new


def extract_mask(image: Path) -> Image.Image:
    image: Image.Image = Image.open(image)
    if "A" not in image.getbands():
        image = image.convert("RGBA")
    r, g, b, a = image.split()
    a.show()


if __name__ == "__main__":
    image = Path(__file__).absolute().parent.joinpath("image_with_mask.png")
    # image = path_pil(image)
    # pil2tensor(image)
    extract_mask(image)

    pass
