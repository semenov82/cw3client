# -*- coding: utf-8 -*-
import config
import telebot
import logging
import os
import json
import re
from telebot import types
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)-3s]# %(levelname)-5s [%(asctime)s] %(message)s',
                    level=logging.INFO)
bot = telebot.TeleBot(config.token)
main_chat = config.main_chat
admin_id = config.admin_id
ordersman = config.ordersman
@bot.message_handler(commands=["start"])
def start(message):
    logging.info('Бота стартанул - '+str(message.from_user.first_name))
    if message.from_user.id == admin_id:
        out = '''
Приветствую тебя, мой повелитель.
На данный момент я знаю {} твинков, для навигации используй кнопки.
'''.format(len(os.listdir('./configs/')))
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('📈Статистика', callback_data='stats')
        # button2 = types.InlineKeyboardButton('🤖Твинки', callback_data='tween')
        keyboard.row(button1)
        bot.send_message(message.chat.id, out, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda c: True)
def inlin(c):
    if c.data == 'stats':
        lvl = 0
        atk = 0
        deff = 0
        gold = 0
        tort = 0 # 🐢
        list = 0 # 🍁
        roza = 0 # 🌹
        klev = 0 # ☘️
        rat  = 0 # 🦇
        love = 0 # 🖤
        bacl = 0 # 🍆
        users1 = os.listdir('./configs/')
        users = []
        while len(users1) > 0:
            t2 = users1.pop()
            t1 = re.sub('.json', '', t2)
            users.append(t1)
        while len(users) > 0:
            user = users.pop()
            user += '.json'
            jsons = './configs/' + user
            udata = []
            udata = json.load(open(jsons, 'r'))
            udata = udata.pop()
            udata = sorted(udata.items(),reverse=True)
            while len(udata) > 0:
                cur = udata.pop()
                key = cur[0]
                value = cur[1]
                if key == 'lvl':
                    lvl += value
                elif key == 'atk':
                    atk += value
                elif key == 'deff':
                    deff += value
                elif key == 'gold':
                    gold += value
                elif key == 'castle':
                    if value == 'Тортуги':
                        tort += 1 
                    elif value == 'Амбера':
                        list += 1
                    elif value == 'Рассвета':
                        roza += 1
                    elif value == 'Оплота':
                        klev += 1
                    elif value == 'Ночи':
                        rat  += 1
                    elif value == 'Скалы':
                        love += 1
                    elif value == 'Фермы':
                        bacl += 1
            out = '''
Общая статистика фермы:
🏅Уровень: {}
⚔️Атака: {}
🛡Защита: {}
💰Золото: {}
Количество твинков в замках:
🐢 {}   🍁 {}
🌹 {}   ☘️ {}
🦇 {}   🖤 {}
    🍆 {}
'''.format(lvl,atk,deff,gold,tort,list,roza,klev,rat,love,bacl)
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('📈Статистика', callback_data='stats')
        # button2 = types.InlineKeyboardButton('🤖Твинки', callback_data='tween')
        keyboard.row(button1)
        bot.edit_message_text(out, c.message.chat.id, c.message.message_id, reply_markup=keyboard)
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
     bot.polling(none_stop=True)