from glchat_sdk import GLChat

client = GLChat()

response = client.message.create(
    chatbot_id="general-purpose",
    message="Nama saya Budiono Siregar. Saya umur 20 tahun. Project saya LODA. Nomor HP saya 081234567890. Saya asal Yogyakarta. Tolong rekap biodata saya",
    anonymize_lm=True,
)

for chunk in response:
    print(chunk.decode("utf-8"), end="")
