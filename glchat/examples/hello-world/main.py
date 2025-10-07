from glchat_sdk import GLChat

client = GLChat()
response = client.message.create(
    chatbot_id="no-op",
    message="Hello!",
)

for chunk in response:
    print(chunk.decode("utf-8"), end="")
