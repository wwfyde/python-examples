from google import genai

from lib import settings

api_key = settings.providers.gemini.api_key

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words",
)
print(response.text)
