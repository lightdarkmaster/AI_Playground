import requests

API_KEY = "YOUR_OPENAI_API_KEY"
API_URL = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("LLM CLI Chat (type 'exit' to quit)\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    data = {
        "model": "gpt-4.1-mini",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        print("\nAI:", reply, "\n")
    else:
        print("Error:", response.text)