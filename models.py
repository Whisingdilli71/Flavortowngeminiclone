import requests

GOOGLE_API_KEY = "AIzaSyBaBufVHGUC9Gwgzw_sJRLzAyGJnaITnms"
url = f"https://generativelanguage.googleapis.com/v1/models?key={GOOGLE_API_KEY}"

response = requests.get(url)
print(response.json())
