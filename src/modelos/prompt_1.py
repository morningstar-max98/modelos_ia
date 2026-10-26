from langchain_ollama import ChatOllama

class prompt_1:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b",temperature=0.1)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke("Hola, ¿cómo estás? ¿Puedes ayudarme con un problema de programación?")
        return respuesta.text