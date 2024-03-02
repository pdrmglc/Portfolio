import google.generativeai as genai
import telebot
import sys


with open("api_key.txt") as file:
    API_KEYS = file.readlines()

API_GEMINI = str(API_KEYS[0]).strip("\n")
API_TELEGRAM = str(API_KEYS[1]).strip("\n")

genai.configure(api_key=API_GEMINI)

model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(API_TELEGRAM)

chat = model.start_chat(history=[])

def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    print(mensagem.text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))

    try:
        response = chat.send_message(mensagem.text)
        # print(response.text)
        bot.reply_to(mensagem, response.text)
    except:
        bot.reply_to(mensagem, "Mande sem emojis ou stickers por favor T.T")

bot.polling()