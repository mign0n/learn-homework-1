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

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="bot.log")

DATE_TODAY = date.today().strftime("%Y/%m/%d")


def greet_user(update, context):
    text = "Вызван /start"
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def get_constelation(update, context):
    user_text = update.message.text
    _, planet = user_text.split()
    planet = planet.lower().capitalize()
    try:
        p = getattr(ephem, planet)(DATE_TODAY)
    except AttributeError:
        update.message.reply_text("I don't know this planet. Maybe you meant the Moon?")
        planet = "Moon"
        p = getattr(ephem, planet)(DATE_TODAY)
    try:
        _, constellation = ephem.constellation(p)
        update.message.reply_text(f"Today {planet.capitalize()} is in the constellation of {constellation}.")
    except TypeError:
        update.message.reply_text("It's not a planet. Enter the name of a planet in the Solar System.")


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
