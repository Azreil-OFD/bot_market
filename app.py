from ast import If
from telebot import types
import telebot
import re
from Shop_v1_1 import *
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
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
    key = types.InlineKeyboardMarkup()
    mark = []
    for i in category().data_list:
        btn1 = types.InlineKeyboardButton(text = i.title , callback_data = "category|"+f"{i.id}")
        mark.append(btn1)
    key.add(*mark)
    
    bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=key)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    key = types.InlineKeyboardMarkup()
    mark = []
    print(c)
    sd = c.data.split("|")
    s = category()
    if c.data == "menu":
        key = types.InlineKeyboardMarkup()
        key_0 = types.InlineKeyboardMarkup()
        mark = []
        for i in s.data_list:
            btn1 = types.InlineKeyboardButton(text = i.title , callback_data = "category|"+f"{i.id}")
            mark.append(btn1)
        key.add(*mark)
        mark.clear()
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="ВЫБЕРИТЕ КНОПКУ", reply_markup=key_0)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="ВЫБЕРИТЕ КНОПКУ", reply_markup=key)
        s.data_list.clear()

    elif sd[0] == "category":
        for i in products(cat_id=int(sd[1])).data_list:
            btn1 = types.InlineKeyboardButton(text = i.title , callback_data = "product|"+f"{i.id}")
            mark.append(btn1)
        btn1 = types.InlineKeyboardButton(text = "К списку категорий" , callback_data = "menu")
        mark.append(btn1)
        key.add(*mark)
        mark.clear()
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="ВЫБЕРИТЕ ТОВАР ИЗ АССОРТИМЕНТА", reply_markup=key)
    
# @bot.message_handler(commands=["category"])
# def start(m, res=False):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     category().data_list.clear()
    # category().data_list.clear()
    # bot.send_message(m.chat.id, f"очистка клавиатуры...", reply_markup=types.ReplyKeyboardRemove(selective=False))
    # bot.delete_message(m.chat.id, m.message_id + 1)
    # bot.send_message(m.chat.id, "Категории:", reply_markup=markup)

@bot.message_handler(commands=["all"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for i in products().data_list:
        btn1 = types.KeyboardButton(i.title)
        markup.add(btn1)
        print(i.title)
    products().data_list.clear()
    
    bot.send_message(m.chat.id, "Категории:", reply_markup=markup)

te = True

# @bot.message_handler(content_types=["text"])
# def handle_text(m):    
#     mass = products(cat_id= i.id).data_list
#     catMass = category().data_list
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     bot.send_message(m.chat.id, f"очистка клавиатуры...", reply_markup=types.ReplyKeyboardRemove(selective=te))

#     for i in catMass:
#         print(m.text)
#         if i.title == m.text:
#             print( i.title == m.text )
#             for b in mass:
#                 print(i.title)
#                 btn1 = types.KeyboardButton(text= i.title)
#                 markup.add(btn1)
#             bot.send_message(m.chat.id, f"Товары из категории: {m.text}", reply_markup=markup)
#             break
#     print("Конец")
bot.polling(none_stop=True, interval=0)