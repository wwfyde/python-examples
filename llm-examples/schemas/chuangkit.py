from enum import Enum
from typing import NamedTuple

from fastapi.security import APIKeyHeader


class TagInfo(NamedTuple):
    """Tag information for Chuangkit."""

    label: str
    value: str
    id: int = 0

    APIKeyHeader


class Scene(Enum):
    poster = TagInfo("海报", "poster")
    douyin = TagInfo("抖音", "douyin")
    rednote = TagInfo("小红书", "rednote")
    wechat = TagInfo("公众号", "wechat")
