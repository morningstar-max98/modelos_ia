from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class Prompt_roles:
    def __init__(self):
        self.modelo=ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def generar_respuestas(self):
        plantilla = ChatPromptTemplate.from_messages([
            ("system", 
            """
                Eres un experto en roles de trabajo y desarrollo profesional.

                instrucciones:
                -Responde siempre en español.
                -Utiliza lenguaje sencillo.
                - Ecplica los cenceptos paso a paaso.
                - Incluye un ejemplo en Python
                - No utilices tecnisismos innecesarios.
            """),
            ("human", 
            """
                Explica el concepto de {tema} 
            """)

        ])
        mensaje = plantilla.invoke({"tema": "Estructuras condicionales"})
        respuesta = self.modelo.invoke(mensaje)
        return respuesta.text