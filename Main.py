from email import message

import telebot

bot = telebot.TeleBot('6835704946:AAF-knQ9NYQLsQIDr3zht83jDxaXLXP0bkY')


@bot.message_handlers(comands=['start'])
def main(massage):
    bot.send_message(message.chat.id, 'Привет!')


bot.pollint(none_stop=True)
