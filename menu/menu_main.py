from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal

import os
from rich.console import Console
from rich.markdown import Markdown

class MenuPrincipal:
    def __init__(self):
        self.console = Console()
        self.opcion = 0


    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pausar(self):
        input("\nPresione Enter para continuar...")


    def mostrar_menu(self):
        print("=== Menú Principal ===")
        print("1. Modelo Google API KEY")
        print("2. Módelo Groq API KEY")
        print("3. Módelo Local")
        print("0. Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                modelo_google = ModeloGoogle()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_google.generar_respuesta(prompt)
                print("Respuesta del modelo Google:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "2":
                modelo_groq = ModeloGroq()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_groq.generar_respuesta(prompt)
                print("Respuesta del modelo Groq:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "3":
                from src.modelos.modelo_local import ModeloLocal
                modelo_local = ModeloLocal()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_local.generar_respuesta(prompt)
                print("Respuesta del modelo Local:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break 

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            self.pausar()   
