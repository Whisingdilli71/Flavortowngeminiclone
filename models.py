import requests

GOOGLE_API_KEY = "I USED THIS TO FIGURE OUT THE MODELS FOR MY KEY"
url = "https://generativelanguage.googleapis.com/v1/models?key={GOOGLE_API_KEY}"

response = requests.get(url)
print(response.json())


