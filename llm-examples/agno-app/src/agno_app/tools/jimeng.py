import json
import base64
from uuid import uuid4
from typing import Any, List, Union
from urllib.parse import urlencode

import requests
from agno.team import Team
from agno.agent import Agent
from agno.media import ImageArtifact
from agno.tools import Toolkit
from agno.utils.log import logger, log_debug

from lib import settings
from lib.src.lib.image import upload_image
from lib.src.lib.volcengine import Params, create_volc_header


class JimengTools(Toolkit):
    def __init__(
        self,
        access_key: str = None,
        secret_key: str = None,
        width: int = 768,
        height: int = 768,
        **kwargs,
    ):
        self.access_key = access_key or settings.solutions.jimeng.access_key
        self.secret_key = secret_key or settings.solutions.jimeng.secret_key
        self.width = width
        self.height = height

        tools: List[Any] = []
        tools.append(self.create_image)
        super().__init__(name="即梦", tools=tools, **kwargs)

        pass

    def create_image(self, agent: Union[Agent, Team], prompt: str) -> str:
        """Use this function to generate an image for a prompt.

        Args:
            agent (Union[Agent, Team]): The agent or team that is generating the image.
            prompt (str): A text description of the desired image.

        Returns:
            str: str: A message indicating if the image has been generated successfully or an error message.
        """
        if not self.access_key or not self.secret_key:
            return "Please set the `access_key` and `secret_key` for JimengTools."
        if self.width > 768:
            self.width = 768
        if self.height > 768:
            self.height = 768

        try:
            body = {
                "req_key": "jimeng_high_aes_general_v21_L",
                "prompt": prompt,
                "use_sr": True,
                "width": self.width,
                "height": self.height,
                "return_url": False,
                # ......
            }
            params = Params(
                access_key=self.access_key,
                secret_key=self.secret_key,
                body=body,
            )
            query_string = (
                urlencode(sorted(params.query_params.items()))
                if isinstance(params.query_params, dict)
                else params.query_params
            )
            url = params.base_url + "?" + query_string
            headers = create_volc_header(params)
            response = requests.post(url=url, data=json.dumps(body), headers=headers)
            data = response.json()
            images_base64 = data.get("data", {}).get("binary_data_base64", [])

            log_debug(f"Response from Jimeng: {response.status_code}")
            log_debug(response.status_code)

            log_debug("Image generated successfully")
            response_str = ""
            for image_base64 in images_base64:
                if not image_base64:
                    continue
                # Decode the base64 image bytes
                # Create an ImageArtifact from the decoded bytes
                image_bytes = base64.b64decode(image_base64)
                id = str(uuid4())
                filename = f"{id}.png"

                url = upload_image(filename, image_bytes, prefix="jimeng")
                agent.add_image(
                    ImageArtifact(
                        id=id,
                        url=url,  # No URL provided, so set to None
                        original_prompt=prompt,
                        revised_prompt=None,  # No revised prompt provided
                        content=image_bytes,
                        mime_type="image/png",
                    )
                )
                response_str += f"Image has been generated successfully. {url=}\n"
            # Update the run response with the image URLs

            return response_str or "No images were generated"
        except Exception as e:
            logger.error(f"Failed to generate image: {e}")
            return f"Error: {e}"
