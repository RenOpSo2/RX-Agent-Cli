import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

class GeminiAI:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_id = 'gemini-2.5-flash'

        instruction = (
    "You are RX-Agent, a witty and helpful terminal assistant. "
    "Every response MUST be a valid JSON with two fields: "
    "1. 'message': Your conversational response/explanation (string). "
    "2. 'actions': A list of objects for terminal commands, or an empty list [] if no action needed. "
    "Format actions: {'type': 'create_file'|'make_dir'|'delete'|'run_command', 'path': 'string', 'content': 'string'}. "
    "Example: {'message': 'Ready bro, the file has been created', 'actions': [{'type': 'make_dir', 'path': 'docs'}]}"
)

        self.chat_session = self.client.chats.create(
            model=self.model_id,
            config={'system_instruction': instruction}
        )

    def ask(self, message: str) -> str:
        try:
            response = self.chat_session.send_message(message)
            text = response.text or ""
            return text.strip().replace("```json", "").replace("```", "").strip()
        except Exception as e:
            return f'{{"error": "{str(e)}"}}'

