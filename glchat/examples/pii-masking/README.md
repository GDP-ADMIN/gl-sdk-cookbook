## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/GDP-ADMIN/gl-sdk-cookbook.git
   cd glchat/examples/pii-masking
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Run the example**

   ```bash
   uv run main.py
   ```

4. **Expected Output**

   You should see a response from the GLChat SDK, similar to:

   ```
   ...
   data:{"status": "data", "message": "{\"data_type\": \"deanonymized_data\", \"data_value\": {\"user_message\": {\"content\": \"Nama saya <PERSON_1>. Saya umur 20 tahun. Project saya LODA. Nomor HP saya <PHONE_NUMBER_1>. Saya asal Yogyakarta. Tolong rekap biodata saya\", \"deanonymized_content\": \"Nama saya Budiono Siregar. Saya umur 20 tahun. Project saya LODA. Nomor HP saya 081234567890. Saya asal Yogyakarta. Tolong rekap biodata saya\"}, \"ai_message\": {\"content\": \"Biodata singkat:\\n\\n- Nama: <PERSON_1>\\n- Umur: 20 tahun\\n- Project: LODA\\n- Nomor HP: <PHONE_NUMBER_1>\\n- Asal: Yogyakarta\\n\\nMau saya susun dalam format CV, kartu identitas, atau ringkasan untuk LinkedIn?\", \"deanonymized_content\": \"Biodata singkat:\\n\\n- Nama: Budiono Siregar\\n- Umur: 20 tahun\\n- Project: LODA\\n- Nomor HP: 081234567890\\n- Asal: Yogyakarta\\n\\nMau saya susun dalam format CV, kartu identitas, atau ringkasan untuk LinkedIn?\"}, \"deanonymized_mapping\": {\"<PERSON_1>\": \"Budiono Siregar\", \"<PHONE_NUMBER_1>\": \"081234567890\"}}}", "conversation_id": null, "user_message_id": null, "assistant_message_id": null, "created_date": 1759807953969, "stream_message_only": false}
   ```
