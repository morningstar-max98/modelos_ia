from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal
from src.modelos.modelo_phi_mini import ModeloLocal
from src.modelos.prompt_1 import prompt_1
from src.modelos.prompt_2 import Prompt_02
from src.modelos.modelo_roles import Prompt_roles
from src.modelos.modelo_conectar import Prompt_Conexion

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
        print("4. Módelo Phi Mini")
        print("5. Prompt 1")
        print("6. Prompt 2")
        print("7. Prompt roles")
        print("8. Prompt Conexión")
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

            elif self.opcion == "4":
                from src.modelos.modelo_phi_mini import ModeloLocal
                modelo_phi_mini = ModeloLocal()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_phi_mini.generar_respuesta(prompt)
                print("Respuesta del modelo Phi Mini:")
                #print(respuesta)   
                self.console.print(Markdown(respuesta))

            elif self.opcion == "5":
                from src.modelos.prompt_1 import prompt_1
                modelo_prompt_1 = prompt_1()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_prompt_1.generar_respuesta(prompt)
                print("Respuesta del modelo Prompt 1:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "6":
                from src.modelos.prompt_2 import Prompt_02
                modelo_prompt_2 = Prompt_02()
                respuesta = modelo_prompt_2.generar_respuestas()
                print("Respuesta del modelo Prompt 2:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "7":
                prompt_roles = Prompt_roles()
                respuesta = prompt_roles.generar_respuestas()
                print("Respuesta del modelo Prompt Roles:")
                self.console.print(Markdown(respuesta))

            elif self.opcion == "8":
                from src.modelos.modelo_conectar import Prompt_Conexion
                prompt_conexion = Prompt_Conexion()
                respuesta = prompt_conexion.generar_respuestas()
                print("Respuesta del modelo Prompt Conexión:")
                self.console.print(Markdown(respuesta))


            elif self.opcion == "0":
                print("Saliendo del programa...")
                break 

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            self.pausar()   
