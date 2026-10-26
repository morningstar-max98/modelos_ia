from langchain_groq import ChatGroq
from dotenv import load_dotenv

class ModeloGroq:
    def __init__(self):
        load_dotenv()
        self.model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)

    def generar_respuesta(self, prompt):
        response = self.model.invoke(prompt)
        return response.text
