import os

from dotenv import find_dotenv, load_dotenv
from google import genai


def main():
    a = 12
    load_dotenv(find_dotenv())
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(model="gemini-2.5-flash", contents="Explain how AI works in a few words")
    print(response.text)


if __name__ == "__main__":
    main()
