from typing import cast

from openai import OpenAI
from openai.types.responses import ResponseInputParam
from pydantic import BaseModel

client = OpenAI()


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=cast(
        ResponseInputParam,
        [
            {"role": "system", "content": "Extract the event information."},
            {
                "role": "user",
                "content": "Alice and Bob are going to a science fair on Friday.",
            },
        ],
    ),
    text_format=CalendarEvent,
)

event = response.output_parsed
print(event)
