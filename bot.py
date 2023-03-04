import requests
import telebot

from extensions import Rates, CurrencyPrice


TELEGRAM_BOT_API_TOKEN = '6246572558:AAEJcF-DQxOJrXei7KnDdNPOTPOsUGa0h_4'

bot = telebot.TeleBot(TELEGRAM_BOT_API_TOKEN, parse_mode=None)

class APIException(BaseException):
    pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Чтобы получить цену интересующей вас валюты, отправите боту сообщение в виде:\n'
                          '<имя валюты, цену которой он хочет узнать> '
                          '<имя валюты, в которой надо узнать цену первой валюты> '
                          '<количество первой валюты>.\n'
                          'Наример:\n'
                          'USD EUR 100')


@bot.message_handler(commands=['values'])
def send_rates(message):
    rates = Rates().get_rates()
    reply_message = '\n'.join(f"{k}: {v/rates['RUB'] if k != 'RUB' else 1.0}" for k, v in rates.items())
    bot.reply_to(message, reply_message)


@bot.message_handler(func=lambda m:True)
def convert(message):
    try:
        message_split = message.text.strip().split(' ')
        base = message_split[0]
        quote = message_split[1]
        amount = int(message_split[2])
        rates = Rates().get_rates()

        if base in rates and quote in rates.keys():
            currency_price = CurrencyPrice()
            reply_message = str(currency_price.get_price(base, quote, amount))
            bot.reply_to(message, reply_message)
        else:
            reply_message = 'Введена неверная валюта.'
            bot.reply_to(message, reply_message)
            raise APIException(reply_message)
    except Exception as e:
        exception_type = type(e).__name__
        exception_text = str(e)
        reply_message = f'{exception_type}: {exception_text}'
        bot.reply_to(message, reply_message)
        raise





if __name__ == '__main__':
    bot.infinity_polling()
