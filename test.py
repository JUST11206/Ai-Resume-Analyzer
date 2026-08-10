from google import genai

client = genai.Client(api_key="AQ.Ab8RN6I5uOWgam8YKcYCX7sPXAiOqdbdUWPSJhFT5LpM4iIaig")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Hello Gemini, are you working?"
)

print(response.text)