import telebot
# Вторичные пакеты
from modules import config
from modules.main import start

# Токен и версия
bot = telebot.TeleBot(config.token)
version = config.version

# Постоянные переменные
my_id = '1793593147'
my_username = '@nigg_rsbelike'

if __name__ == '__main__':
    start()
