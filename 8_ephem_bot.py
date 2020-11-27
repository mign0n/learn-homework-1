"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
import ephem
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

DATE_TODAY = date.today().strftime('%Y/%m/%d')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_constelation(update, context):
    user_text = update.message.text
    user_request = user_text.split()
    print(user_request)
    planet = user_request[-1].lower()
    print(planet)
    if planet == 'mercury':
        p = ephem.Mercury(DATE_TODAY)
    elif planet == 'venus':
        p = ephem.Venus(DATE_TODAY)
    elif planet == 'mars':
        p = ephem.Mars(DATE_TODAY)
    elif planet == 'jupiter':
        p = ephem.Jupiter(DATE_TODAY)
    elif planet == 'saturn':
        p = ephem.Saturn(DATE_TODAY)
    elif planet == 'uranus':
        p = ephem.Uranus(DATE_TODAY)
    elif planet == 'neptune':
        p = ephem.Neptune(DATE_TODAY)
    elif planet == 'pluto':
        p = ephem.Pluto(DATE_TODAY)
    else:
        update.message.reply_text('I don\'t know this planet. Maybe you meant the Moon?')
        planet = 'moon'
        p = ephem.Moon(DATE_TODAY)

    constellation = ephem.constellation(p)
    print(constellation)
    update.message.reply_text(f'Today {planet.capitalize()} is in the constellation of {constellation[-1]}.')


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constelation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
