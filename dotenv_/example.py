import os

from dotenv import load_dotenv, dotenv_values

config = {
    **os.environ,
    **dotenv_values(),
}
print(config)
print(type(config))
