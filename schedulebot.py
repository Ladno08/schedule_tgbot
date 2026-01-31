import requests
from telebot import TeleBot
from datetime import datetime, timedelta
import time
import settings

bot = TeleBot(settings.TOKEN)

user_event = []
user_event_datetime = []

@bot.message_handler(commands=['start'])
def greed(message):
    print(message)
    bot.send_message(message.chat.id, 'Йоу чё как Марк' )

@bot.message_handler(commands=['addevent'])
def ask_eventdatetime(message):
    print(message)
    bot.send_message(message.chat.id, 'Введи дату и время события (ДД.ММ.ГГГГ ЧЧ:ММ)')
    bot.register_next_step_handler(message, add_eventtime)

def add_eventtime(message):
    event_datetime = message.text
    try:
        event_datetime = datetime.strptime(
            message.text,
            '%d.%m.%Y %H:%M')
        user_event_datetime.append(event_datetime)
        bot.send_message(
            message.chat.id,
            f'Событие сохранено: {event_datetime}'
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            'Блин чёто не так\nПопробуй ещё раз: ДД.ММ.ГГГГ ЧЧ:ММ'
        )
    bot.send_message(message.chat.id, 'а чё за событие?')
    bot.register_next_step_handler(message, add_eventname)


def add_eventname(message):
    event_name = message.text
    user_event.append(event_name)
    bot.send_message(message.chat.id, 'всё, запомнил, когда тебе напомнить о событии?')


@bot.message_handler(commands=['remindday'])
def remind_day(message):
    while True:
        now = datetime.now()
        delta = user_event_datetime[0] - now
        if delta <= timedelta(days=1):
            bot.send_message(message.chat.id, f'Марк до {user_event[0]} остался 1 день или меньше!')
            break
        else:
            time.sleep(3600)
    bot.send_message(message.chat.id, f'без б, напомню, что у тебя {user_event[0]} за день до')


    @bot.message_handler(commands=['hour'])
    def remind_hour(message):
        while True:
            now = datetime.now()
            delta = user_event_datetime[0] - now
            if delta <= timedelta(hours=1):
                break
            else:
                time.sleep(1800)
        bot.send_message(message.chat.id, f'без б, напомню, что у тебя {user_event[0]} за час до')
        print('dqa[]dewa3d')




bot.polling()


