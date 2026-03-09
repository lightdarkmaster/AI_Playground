import requests
import sys
import json

# =============================
# CONFIGURATION
# =============================
API_KEY = "YOUR_OPENAI_API_KEY"
API_URL = "https://api.openai.com/v1/chat/completions"

# =============================
# GET USER PROMPT FROM CMD
# =============================
if len(sys.argv) < 2:
    print("Usage: python llm_cmd.py 'your question'")
    sys.exit()

prompt = " ".join(sys.argv[1:])

# =============================
# REQUEST HEADERS
# =============================
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# =============================
# REQUEST DATA
# =============================
data = {
    "model": "gpt-4.1-mini",  
    "messages": [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.3,
    "max_tokens": 300
}

# =============================
# SEND REQUEST
# =============================
response = requests.post(API_URL, headers=headers, json=data)

# =============================
# HANDLE RESPONSE
# =============================
if response.status_code == 200:
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    print("\nAI Response:\n")
    print(reply)
else:
    print("Error:", response.status_code)
    print(response.text)