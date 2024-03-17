import google.generativeai as genai
import keyboard
import inspect

def tratarTexto(texto):
    texto = texto.replace("*","")
    texto = texto.replace(":","")

    return texto 

def main():
    assistente_falante = False
    ligar_microfone = False
    iniciar_assistente = True
    iniciar_microfone = True

    genai.configure(api_key="AIzaSyCTy36HvN8vmiK06aZphHDVWvSHWKu6Ato")
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         print(m.name)

    model = genai.GenerativeModel('gemini-pro')


    chat = model.start_chat(history=[])
    # chat.send_message("Haja como um assistente conciso")

    # print(chat.history)

    ### configura voz
    if iniciar_assistente:
        import pyttsx3
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('rate', 180) # velocidade 120 = lento

        # print("\nLista de Vozes - Verifique o número\n")
        # for indice, vozes in enumerate(voices): # listar vozes
        #     print(indice, vozes.name)

        voz = 0
        engine.setProperty('voice', voices[voz].id)

    if iniciar_microfone:
        import speech_recognition as sr  # pip install SpeechRecognition
        r = sr.Recognizer()
        mic = sr.Microphone()

    bem_vindo = "# Bem Vindo ao seu assistente com Gemini AI #"
    print("")
    print(len(bem_vindo) * "#")
    print(bem_vindo)
    print(len(bem_vindo) * "#")
    print("###   Digite 'desligar' para encerrar    ###")
    print("")

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
                except Exception as e:
                    print("Não entendi o que você disse. Erro", e)
                    texto = ""
        # else:
        #     texto = input("Escreva sua mensagem (ou #sair): ")

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

if __name__ == '__main__':
    main()