from pydantic import BaseModel
from pydantic_settings import BaseSettings


class SubSettings(BaseSettings):
    b: int = 2


class Demo(BaseModel):
    pass


class Settings(BaseSettings):
    extra: SubSettings | None = None

    a: int = 12


settings = Settings(extra=SubSettings())

if __name__ == "__main__":
    b = settings.model_dump()
    print(b)
    extra = SubSettings()
    print(isinstance(extra, BaseModel))
