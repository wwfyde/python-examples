import os

from dotenv import find_dotenv, load_dotenv
from google import genai
from google.genai import types


# 需要 **gcloud auth application-default login**
load_dotenv(find_dotenv())
client = genai.Client(vertexai=True, project=os.getenv("GOOGLE_CLOUD_PROJECT_ID"), location="global", api_key="")
# If your image is stored in Google Cloud Storage, you can use the from_uri class method to create a Part object.
IMAGE_URI = "gs://generativeai-downloads/images/scones.jpg"

# model="claude-sonnet-4@20250514",  # 免费账户不可用
model = "gemini-2.5-flash-preview-05-20"
response = client.models.generate_content(
    model=model,
    contents=[
        "What is shown in this image?",
        types.Part.from_uri(
            file_uri=IMAGE_URI,
            mime_type="image/png",
        ),
    ],
)
print(response.text, end="")
