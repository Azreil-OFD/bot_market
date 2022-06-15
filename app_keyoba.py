from ast import If
from telebot import types
import telebot
import re
from Shop_v1_1 import *
import logging
from keyboa import Keyboa

# Создаем экземпляр бота
bot = telebot.TeleBot('5259849852:AAFZdUgKAPVQS98oCRajtcsTnJXWPaFrl3I')

product_all()

def get_category(message):
    return []

START_TEXT = """
Привет! Я бот для просмотра товаров в нашем интернет магазине.

Для просмотра товаров по категориям , введите категорию товара.

Что бы просмотреть категории введите /category.

Что бы просмотреть товары введите /product <id товара>.

Что бы посмотреть весь ассортимент введите /all.

"""

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, START_TEXT)

@bot.message_handler(commands=["category"])
def inline(message):
    fruits = []
    for i in category().data_list:
        print(i)
        fruits.append({i.title : i.id})
    keyboard = Keyboa(items=fruits , front_marker="&categories=")

    del category().data_list[:]

    bot.send_message(
                    chat_id=message.chat.id, reply_markup=keyboard(),
                    text="Категории:")

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    
    s = c.data.split("=")

    if s[1] == 'menu':
        fruits = []
        for i in category().data_list:
            print(i)
            fruits.append({i.title : i.id})
        del category().data_list[:]
        keyboard = Keyboa(items=fruits , front_marker="&categories=")
        bot.edit_message_text(chat_id=c.message.chat.id,
                                message_id=c.message.message_id,
                                reply_markup=keyboard(),
                                text="Категории:")

    elif s[0] == '&categories':
        fruits = [[]]
        pr = products(cat_id=int(s[1]))
        for i in pr.data_list:
            fruits[0].append({i.title : i.title})
        del pr.data_list[:]
        fruits.append({"Назад в меню" : "menu"})
        keyboard = Keyboa(items=fruits , front_marker="&product=")
        bot.edit_message_text(chat_id=c.message.chat.id,
                                message_id=c.message.message_id,
                                reply_markup=keyboard(),
                                text="Элементы категории:")

    elif s[0] == '&product':
        fruits = []
        print(s[1])
        pr = products(s[1])

        for i in pr.data_list:
            text = f"""Наименование: {i.title}\n
            Описание: {i.description}"""

            url = i.url_photo

        del pr.data_list[:]

        fruits.append({"Назад в меню" : "menu"})

        keyboard = Keyboa(items=fruits , front_marker="&product=")
        bot.send_photo(c.message.chat.id, url, caption=text)
        # bot.edit_message_text(chat_id=c.message.chat.id,
        #                     message_id=c.message.message_id,
        #                     reply_markup=,
        #                     text= )
                            
        del category().data_list[:]

        

@bot.message_handler(commands=["all"])
def start(m, res=False):
    pass



bot.polling(none_stop=True, interval=0)