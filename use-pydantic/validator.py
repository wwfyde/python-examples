from typing import Literal

from pydantic import BaseModel, model_validator


class ToolOutputImage(BaseModel):
    name: Literal["image"] = "image"
    image_url: str | None = None
    file_id: str | None = None
    detail: Literal["low", "high", "auto"] | None = None

    @model_validator(mode="after")
    def check_at_least_one_required_field(self) -> ToolOutputImage:
        """Validate that at least one of image_url or file_id is provided."""
        if self.image_url is None and self.file_id is None:
            raise ValueError("At least one of image_url or file_id must be provided")
        return self
