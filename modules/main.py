# Основные модули
import telebot
from telebot import types
from time import sleep
# Вторичные пакеты
from modules import config

# Токен и версия
bot = telebot.TeleBot(config.token)
version = config.version

# Постоянные переменные
my_id = '1793593147'
my_username = '@nigg_rsbelike'


# Запуск бота
def start():
    # Команда /start
    @bot.message_handler(commands=['start'])
    def command_start(message):
        # Переменная связанная с приветствием
        name = message.from_user.first_name
        chat_id = message.chat.id
        print(chat_id)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        shedule_button = types.KeyboardButton(
            "Расписание")
        other_button = types.KeyboardButton(
            "Другое")
        markup.add(shedule_button, other_button)
        bot.send_message(message.chat.id,
                         "Привет, {0}".format(name), reply_markup=markup)

    # Команда /help
    @bot.message_handler(commands=['help'])
    def command_help(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        shedule_button = types.KeyboardButton(
            "Расписание")
        other_button = types.KeyboardButton(
            "Другое")
        markup.add(shedule_button, other_button)
        bot.send_message(message.chat.id,
                         "Список команд: \n/start - запустить бота\n/help - отображение списка команд\n/about - "
                         "информация о проекте")

    # Команда /about
    @bot.message_handler(commands=['about'])
    def command_help(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        shedule_button = types.KeyboardButton(
            "Расписание")
        other_button = types.KeyboardButton(
            "Другое")
        markup.add(shedule_button, other_button)
        bot.send_message(message.chat.id,
                         "На данный момент актуальная версия бота - {0}.\nОсновной и единственный"
                         "разработчик - {1}".format(version, my_username), reply_markup=markup)

    # Кнопка Расписание и её подкнопки
    @bot.message_handler(content_types=['text'])
    def button_shedule(message):
        if message.text == 'Расписание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            first_course_button = types.KeyboardButton(
                "1 курс")
            second_course_button = types.KeyboardButton(
                "2 курс")
            third_course_button = types.KeyboardButton(
                "3 курс")
            menu_button = types.KeyboardButton(
                "Меню")
            markup.add(first_course_button, second_course_button, third_course_button, menu_button)
            bot.send_message(message.chat.id,
                             'Выберите свой курс', reply_markup=markup)
        else:
            button_other(message)
            button_secret(message)
            button_donut(message)
            button_back_from_other(message)
            button_information(message)
            button_first_course(message)
            button_second_course(message)
            button_third_course(message)
            button_menu(message)
            button_back_from_shedule(message)

        # Кнопка 1 курс

    def button_first_course(message):
        if message.text == '1 курс':
            # Здесь кнопки выбора группы
            markup = types.ReplyKeyboardMarkup()
            group_1_button = types.KeyboardButton(
                "МСПР-22-9-1")
            group_2_button = types.KeyboardButton(
                "МДР-22-9-1")
            group_3_button = types.KeyboardButton(
                "ЭМ-22-9-1")
            group_4_button = types.KeyboardButton(
                "МСР-22-9-1")
            group_5_button = types.KeyboardButton(
                "СВР-22-9-1")
            group_6_button = types.KeyboardButton(
                "ДФС-22-9-1")
            group_7_button = types.KeyboardButton(
                "МЖКХ-22-9-1")
            back_button = types.KeyboardButton(
                "Назад")
            markup.add(group_1_button)
            markup.add(group_2_button, group_3_button, group_4_button, group_5_button, group_6_button, group_7_button)
            markup.add(back_button)
            bot.send_message(message.chat.id,
                             "Выберите свою группу", reply_markup=markup)

        # Кнопка 2 курс

    def button_second_course(message):
        if message.text == '2 курс':
            # Здесь кнопки выбора группы
            markup = types.ReplyKeyboardMarkup()
            group_1_button = types.KeyboardButton(
                "МСПР-21-9-1")
            group_2_button = types.KeyboardButton(
                "МДР-21-9-1")
            group_3_button = types.KeyboardButton(
                "ЭМ-21-9-1")
            group_4_button = types.KeyboardButton(
                "МСР-21-9-1")
            group_5_button = types.KeyboardButton(
                "СВР-21-9-1")
            group_6_button = types.KeyboardButton(
                "ДФС-21-9-1")
            group_7_button = types.KeyboardButton(
                "МЖКХ-21-9-1")
            back_button = types.KeyboardButton(
                "Назад")
            markup.add(group_1_button)
            markup.add(group_2_button, group_3_button, group_4_button, group_5_button, group_6_button, group_7_button)
            markup.add(back_button)
            bot.send_message(message.chat.id,
                             "Выберите свою группу", reply_markup=markup)

        # Кнопка 3 курс

    def button_third_course(message):
        if message.text == '3 курс':
            # Здесь кнопки выбора группы
            markup = types.ReplyKeyboardMarkup()
            group_1_button = types.KeyboardButton(
                "МСПР-20-9-1")
            group_2_button = types.KeyboardButton(
                "МДР-20-9-1")
            group_3_button = types.KeyboardButton(
                "МСР-20-9-1")
            group_4_button = types.KeyboardButton(
                "МЖКХ-20-9-1")
            group_5_button = types.KeyboardButton(
                "ЭМ-20-9-1")
            group_6_button = types.KeyboardButton(
                "СВР-20-9-1")
            group_7_button = types.KeyboardButton(
                "ДФС-20-9-1")
            back_button = types.KeyboardButton(
                "Назад")
            markup.add(group_1_button)
            markup.add(group_2_button, group_3_button, group_4_button, group_5_button, group_6_button, group_7_button)
            markup.add(back_button)
            bot.send_message(message.chat.id,
                             "Выберите свою группу", reply_markup=markup)

        # Кнопка назад

    def button_back_from_shedule(message):
        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            first_course_button = types.KeyboardButton(
                "1 курс")
            second_course_button = types.KeyboardButton(
                "2 курс")
            third_course_button = types.KeyboardButton(
                "3 курс")
            menu_button = types.KeyboardButton(
                "Меню")
            markup.add(first_course_button, second_course_button, third_course_button, menu_button)
            sleep(0.073)
            bot.send_message(message.chat.id,
                             'Выберите свой курс', reply_markup=markup)

        # Кнопка меню

    def button_menu(message):
        if message.text == 'Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            shedule_button = types.KeyboardButton(
                "Расписание")
            other_button = types.KeyboardButton(
                "Другое")
            markup.add(shedule_button, other_button)
            bot.send_message(message.chat.id,
                             'Вы вернулись в главное меню', reply_markup=markup)

    # Кнопка Другое и её подкнопки
    def button_other(message):
        if message.text == 'Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            secret_button = types.KeyboardButton(
                "Секрет")
            donut_button = types.KeyboardButton(
                "Донат")
            information_button = types.KeyboardButton(
                "Информация")
            menu_button = types.KeyboardButton(
                "Меню")
            markup.add(secret_button, donut_button, information_button, menu_button)
            bot.send_message(message.chat.id,
                             "Вы перешли в раздел Другое", reply_markup=markup)

        # Кнопка Секрет

    def button_secret(message):
        if message.text == 'Секрет':
            bot.send_message(message.chat.id,
                             "В этом боте множество пасхалок, советую поискать получше, подсказки спрятаны везде."
                             "\nПри нахождении всех пасхалок, Вам откроются дополнительные "
                             "функции!\nУдачных поисков!")

        # Кнопка Донат

    def button_donut(message):
        if message.text == 'Донат':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yandex_button = types.KeyboardButton(
                "YooMoney")
            eth_button = types.KeyboardButton(
                "ETH Wallet")
            back_button = types.KeyboardButton(
                "Нaзад"
            )
            markup.add(yandex_button, eth_button)
            markup.add(back_button)
            bot.send_message(message.chat.id,
                             "Если Вам нравится пользоваться данным ботом, почему не поддержать меня рублём?"
                             "\nЯ действительно старался", reply_markup=markup)

        if message.text == 'YooMoney':
            bot.send_message(message.chat.id, "https://yoomoney.ru/to/4100117256730936")
        elif message.text == 'ETH Wallet':
            bot.send_message(message.chat.id, "0x661953550e92f04bE635D9F604933F608D40ce8f")
        else:
            pass
        # Кнопка Информация

    def button_information(message):
        if message.text == 'Информация':
            bot.send_message(message.chat.id,
                             "Данный бот написан на языке Python. Использовались модули pyTelegramBotAPI, "
                             "prettytable. Бот написан на чистом энтузиазме. Идея пришла спонтанно, да и давно "
                             "хотелось написать что-то подобное.\n"
                             "Обновления будут выходить частно, по мере нахождения багов и возможностей улучшения "
                             "функционала бота. "
                             "\n"
                             "\nВерсия бота на данный момент: {0}."
                             "\n"
                             "\nБолее подробная информация будет на Git-ветке: "
                             "# Добавить ссылку на Git".format(version))

        # Кнопка назад из Другое

    def button_back_from_other(message):
        if message.text == 'Нaзад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            secret_button = types.KeyboardButton(
                "Секрет")
            donut_button = types.KeyboardButton(
                "Донат")
            information_button = types.KeyboardButton(
                "Информация")
            menu_button = types.KeyboardButton(
                "Меню")
            markup.add(secret_button, donut_button, information_button, menu_button)
            bot.send_message(message.chat.id,
                             "Вы перешли в раздел Другое", reply_markup=markup)


if __name__ == '__main__':
    start()
    bot.polling(none_stop=True, interval=0)
