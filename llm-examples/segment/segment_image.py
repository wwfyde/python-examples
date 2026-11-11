import torch
from transformers import AutoTokenizer, AutoModel
from PIL import Image
import numpy as np
import os

path = "ByteDance/Sa2VA-4B"
model = (
    AutoModel.from_pretrained(
        path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, use_flash_attn=True, trust_remote_code=True
    )
    .eval()
    .cuda()
)
tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True, use_fast=False)

image_path = "output_image2.png"
text_prompts = "<image>Could you please give me a brief description of the image? Please respond with interleaved segmentation masks for the corresponding parts of the answer."
image = Image.open(image_path).convert("RGB")
input_dict = {
    "image": image,
    "text": text_prompts,
    "past_text": "",
    "mask_prompts": None,
    "tokenizer": tokenizer,
}
return_dict = model.predict_forward(**input_dict)
answer = return_dict["prediction"]  # the text format answer
masks = return_dict["prediction_masks"]  # segmentat
