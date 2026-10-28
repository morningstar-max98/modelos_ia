from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
class Prompt_Conexion:
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

        cadena = plantilla | self.modelo | StrOutputParser()

        mensaje = cadena.invoke({"tema": "Estructuras repetitivas"})
        
        respuesta = self.modelo.invoke(mensaje)

        return respuesta.text