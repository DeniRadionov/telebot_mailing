import telebot
from telebot import types
import os
import json
#API tg bot Нужно вставить свой и никому не говорить!
bot = telebot.TeleBot('API') #your api tg bot
#Открываем json пользователей бота , где есть их id

file_path = 'path' #file path json
if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, 'r') as file:
        data = json.load(file)
else:
    data = {}

#записываем в словарь их id
hash_table = {}
for key, value in data.items():
    hash_table[int(key)] = value

#id admin, нужно вставить свой
id_admin = 1111111 #your id in tg
#id групп
id_groups = [-1001683227281] #id groups https://telegramid.info/index.php
@bot.message_handler(commands=['start'])
def in_join_json_true(message):
    if not message.chat.id in hash_table.keys():
        hash_table[message.chat.id] = message.chat.id
        with open(file_path, 'w') as file:
            json.dump(hash_table, file)
    print('start')





@bot.message_handler(commands=['ls'])
def ls(message):
    if id_admin == message.chat.id:
        if not message.chat.id in hash_table.keys():
            hash_table[message.chat.id] = message.chat.id
            with open(file_path, 'w') as file:
                json.dump(hash_table, file)
        verb = message.text.split()
        mes = ' '.join(verb[1:])
        for key in hash_table:
            if key > 0:
                bot.send_message(key, mes, parse_mode='html')
    print(hash_table)


@bot.message_handler(commands=['chats'])
def ls(message):
    if id_admin == message.chat.id:
        if not message.chat.id in hash_table.keys():
            hash_table[message.chat.id] = message.chat.id
            with open(file_path, 'w') as file:
                json.dump(hash_table, file)
        verb = message.text.split()
        mes = ' '.join(verb[1:])
        for key in hash_table:
            if key < 0:
                bot.send_message(key, mes, parse_mode='html')

@bot.message_handler(commands=['groups'])
def ls(message):
    if id_admin == message.chat.id:
        if not message.chat.id in hash_table.keys():
            hash_table[message.chat.id] = message.chat.id
            with open(file_path, 'w') as file:
                json.dump(hash_table, file)
        verb = message.text.split()
        mes = ' '.join(verb[1:])
        for key in id_groups:
            if key < 0:
                bot.send_message(key, mes, parse_mode='html')

bot.polling(none_stop=True)