from pathlib import Path

from pydantic import BaseModel, Base64Str, Field


class FileInput(BaseModel):
    file: Path = Field(title="File info", description="文件路径")
    image: bytes
    base64s: Base64Str


if __name__ == "__main__":
    print(FileInput.model_json_schema())
