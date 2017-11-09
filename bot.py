import config
import telebot

token = '410353133:AAGCNgjncdmvtm6KpJ7QY_xIMtMXhQZOgk4'
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
