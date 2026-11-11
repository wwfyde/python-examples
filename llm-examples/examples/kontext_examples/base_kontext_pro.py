import os
import time

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

url = "https://api.bfl.ai/v1/flux-kontext-pro"

payload = {
    "prompt": "remove subject on the image, only reserve the background ",
    # "input_image": "https://dms-upload.oss-cn-hangzhou.aliyuncs.com/seedream/b3fbf1a7-fe19-41b3-b640-0b4db8c5e356.png",
    "input_image": "https://delivery-us1.bfl.ai/results/d7/034828325fd7a2/325fd7a217474737be4d8955103c9623/sample.jpeg?se=2025-07-22T12%3A33%3A55Z&sp=r&sv=2024-11-04&sr=b&rsct=image/jpeg&sig=3Gv%2B2MjdgH629Ct%2BJ4kYouzvmYco3qH3EB3cKXF12YU%3D",
    "seed": 42,
    "output_format": "jpeg",
    "prompt_upsampling": False,
    "safety_tolerance": 2,
}
api_key = os.getenv("KONTEXT_API_KEY")
headers = {"x-key": api_key, "Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)
result = response.json()
task_id = result.get("id", None)
polling_url = result.get("polling_url")
print(response.text)
start_time = time.time()
interval = 5
while time.time() - start_time < 60:
    response = requests.get(polling_url)
    resp_dict = response.json()
    if resp_dict.get("status", None) == "Ready":
        image_url = resp_dict.get("result", {}).get("sample", None)
        print(image_url)
        if image_url:
            break
    else:
        print("generating...")
    time.sleep(interval)

# url 1 = https://delivery-us1.bfl.ai/results/d7/034828325fd7a2/325fd7a217474737be4d8955103c9623/sample.jpeg?se=2025-07-22T12%3A33%3A55Z&sp=r&sv=2024-11-04&sr=b&rsct=image/jpeg&sig=3Gv%2B2MjdgH629Ct%2BJ4kYouzvmYco3qH3EB3cKXF12YU%3D
