from langchain_ollama import ChatOllama

class ModeloLocal:
    def __init__(self):
        self.modelo = ChatOllama(model="phi3:mini",temperature=0.1)

    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.content