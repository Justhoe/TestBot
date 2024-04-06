import telebot

token = '6835704946:AAF-knQ9NYQLsQIDr3zht83jDxaXLXP0bkY'
bot = telebot.TeleBot('token')


@bot.message_handlers(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id,message.text)

if __name__=='__main__':
    bot.infinity_polling()
