import google.generativeai as genai
import keyboard
from rich.console import Console
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def tratarTexto(texto):
    texto = texto.replace("*","")
    texto = texto.replace(":","")

    return texto 

def main():
    assistente_falante = False
    ligar_microfone = False
    iniciar_assistente = True
    iniciar_microfone = True
    primeira_interacao = True

    genai.configure(api_key=API_GEMINI)


    model = genai.GenerativeModel('gemini-pro', safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    })

    chat = model.start_chat(history=[])

    contexto =        """
                      Quero que você haja como um mestre de RPG.
                      Seja conciso sempre.
                      Me pergunte qual raça e classe eu quero jogar.
                      """


    ### configura voz
    if iniciar_assistente:
        import pyttsx3
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('rate', 230)
 

        voz = 2
        engine.setProperty('voice', voices[voz].id)

    if iniciar_microfone:
        import speech_recognition as sr 
        r = sr.Recognizer()
        mic = sr.Microphone()

        
    Logo = """

            
        ██████╗░██████╗░░██████╗░
        ██╔══██╗██╔══██╗██╔════╝░
        ██████╔╝██████╔╝██║░░██╗░
        ██╔══██╗██╔═══╝░██║░░╚██╗
        ██║░░██║██║░░░░░╚██████╔╝
        ╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░

        
        █▀▀ █▀█ █▀▄▀█
        █▄▄ █▄█ █ ▀ █

        
        ░██████╗░███████╗███╗░░░███╗██╗███╗░░██╗██╗
        ██╔════╝░██╔════╝████╗░████║██║████╗░██║██║
        ██║░░██╗░█████╗░░██╔████╔██║██║██╔██╗██║██║
        ██║░░╚██╗██╔══╝░░██║╚██╔╝██║██║██║╚████║██║
        ╚██████╔╝███████╗██║░╚═╝░██║██║██║░╚███║██║
        ░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝

    """
    console = Console()
    texto_negrito = f"[bold]{Logo}[/bold]"
    console.print(texto_negrito)

    print("""

        Bem-vind@ à versão pré-alfa do meu RPG de NLP!

        Para começar, pressione a tecla "espaço".
          
        Para sair, fale "Desligar".
    """)

    while True:

        if keyboard.is_pressed('space'):  # Verifica se a tecla de espaço foi pressionada
            ligar_microfone = True
            assistente_falante = True
        if ligar_microfone:
            with mic as fonte:
                r.adjust_for_ambient_noise(fonte)
                print("Fale alguma coisa (ou diga 'desligar')")
                audio = r.listen(fonte)
                
                print("Enviando para reconhecimento")
                try:
                    texto = r.recognize_google(audio, language="pt-BR")
                    print("Você disse: {}".format(texto))
                    if primeira_interacao:
                        texto = contexto +'\n'+ texto
                        primeira_interacao = False
                except Exception as e:
                    print("Não entendi o que você disse. Erro", e)
                    texto = ""

            if texto.lower() == "desligar":
                break

            response = chat.send_message(texto)
            print("Gemini:", response.text, "\n")

            if assistente_falante:
                texto_tratado = tratarTexto(response.text)
                engine.say(texto_tratado)
                engine.runAndWait()
                assistente_falante = False
                ligar_microfone = False


    print("Encerrando Chat")

with open("api_key.txt") as file:
    API_KEYS = file.readlines()

API_GEMINI = str(API_KEYS[0]).strip("\n")


if __name__ == '__main__':
    main()