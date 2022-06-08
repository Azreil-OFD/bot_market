from telebot import types
import telebot
import re
# Создаем экземпляр бота
bot = telebot.TeleBot('5528356844:AAHiM2oh8CtKvXKcWp7smdhj9XQXQrLx-Lo')

listName = ["альф" , "альфред", "альберт" , "аль"]

returns = {
    "кеша":{
        "персы":"""
    Персы Кеша:
        - Сайрин
        - Даниэлла
        - Колу
        - Грейс
        - Евгеша
        - Артур
        - Джереми
        - Марсель
        - Эмиль
        - Алиса
""",
        "даты":"""
    Даты Кеша:
        - Сайрин      - 17 сентября
        - Даниэлла    - 17 сентября
        - Колу        - 20 июня
        - Грейс       - 25 апреля
        - Евгеша       - 12 марта
        - Артур       - 25 ноября
        - Джереми     - 1 февраля
        - Марсель     - 29 декабря
        - Эмиль       - 11 июля
        - Алиса       - 12 июня
    """
    },
    "поля":{
        "персы":"""
    Персы Поля:
        - Джулия
        - Егор
        - Ира
        - Маркус
        - Норт
        - Олеся
        - Саня
    """,
        "даты":"""
    даты Поля:
        - Джулия    - 16 марта
        - Егор      - 12 августа
        - Ира       - 17 мая
        - Маркус    - 29 декабря
        - Норт      - 3 апреля
        - Олеся     - 17 июля
        - Саня      - 22 сентября
    """
    }

}


@bot.inline_handler(func=lambda query: True)
@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Персы Кеша', types.InputTextMessageContent(returns["кеша"]["персы"]))
        r2 = types.InlineQueryResultArticle('2', 'Персы Поля', types.InputTextMessageContent(returns["поля"]["персы"]))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

def search(lst, prefix):
    for i in lst:
        if i == prefix:
            return True
    return False


@bot.message_handler(content_types=["text"])
def handle_text(message):
    text : str = message.text.lower()

    text = text.split(' ')
    if len(text) != 1:
        if text[0] == "поля":
            bot.send_message(message.chat.id, returns[text[0]][text[1]])  
        elif text[0] == "кеша":
            bot.send_message(message.chat.id, returns[text[0]][text[1]])  
        elif text[0] == "эль":
            bot.send_message(message.chat.id, returns[text[0]][text[1]])  

        elif text[0] == "привет":
            if search(listName, text[1]):
                bot.send_message(message.chat.id, 'Привет ' + message.from_user.first_name)
    


bot.polling(none_stop=True, interval=0)