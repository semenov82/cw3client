# -*- coding: utf-8 -*-
import logging
import re
import sys
import os
import random
from time import time, sleep
from getopt import getopt
from getpass import getpass
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)-3s]# %(levelname)-5s [%(asctime)s] %(message)s',
                    level=logging.INFO)
logging.getLogger('telethon').setLevel(level=logging.WARNING)
api_id = 203699
api_hash = '682323eb50adf409b423d905e432d850'
cw = 265204902
game_user = 'ChatWarsBot'
phone = ''
hero_des = '/start'
atk_des = '/atk'
def_des = '/def'
last_pin = False
curret_pin = False
opts, args = getopt(sys.argv[1:], 'p:', ['phone='])
for opt, arg in opts:
    if opt in ('-p', '--phone'):
        phone = arg
try:
    nchek = os.listdir('./sessions/')
except:
    os.mkdir('./sessions/')
    nchek = os.listdir('./sessions/')
nchek1 = str(phone) + '.session'
fss = "./sessions/" + nchek1
client = TelegramClient(fss, api_id, api_hash, update_workers=3, spawn_read_thread=False,device_model='FenicuMinimalBot')
client.connect()
if not client.is_user_authorized():
    if nchek1 in nchek: # Проверяем наличие сессии, если её нет, то запрашиваем логин код
        pass 
    else:
        client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Код из телеграмма: '))
    except SessionPasswordNeededError:
        pw = getpass('Двухэтапная аутентификация включена. '
                     'Введи код: ')
        self_user = client.sign_in(password=pw)
client.start()
# Боремся с ошибкой entity 
client.get_entity(game_user)
logging.info('загрузка завершина')
@client.on(events.NewMessage)
def all_messages(event):
    global hero_des
    global atk_des
    global def_des
    global last_pin
    global curret_pin
    global castle
    regen = 'Состояние:\n(⚔️Атака|🛡Защита) (🐢|🍁|🌹|☘️|🦇|🖤|🍆)'
    regenblack = 'Состояние:\n(⚗️В лавке)'
    regenprof = '(🐢|🍁|🌹|☘️|🦇|🖤|🍆)(.{0,50}) .+ (Тортуги|Оплота|Скалы|Фермы|Ночи|Амбера|Рассвета)'
    if event.message.from_id == cw:
        if re.search('\/go', event.raw_text):
            last_pin = True
            sleep(random.randint(5, 9))
            client.send_message(cw, hero_des)
            logging.info('Караван, проверяем пин')
        elif re.search('\/pledge', event.raw_text):
            sleep(random.randint(5, 9))
            client.send_message(cw, '/pledge')
            logging.info('жмакаем pledge')
        elif re.search('\/engage', event.raw_text):
            sleep(random.randint(5, 9))
            client.send_message(cw, '/engage')
            logging.info('жмакаем engage')
        if 'Битва семи замков' in event.raw_text and last_pin:
            sleep(random.randint(3, 6))
            if re.search(regen, event.raw_text):
                curret_pin = re.search(regen, event.raw_text).group(2)
                castle = re.search(regenprof, event.raw_text).group(1)
                client.send_message(cw, '/go')
                logging.info('Пин на {} после каравана выставляем'.format(curret_pin))
            elif re.search(regenblack, event.raw_text):
                curret_pin = '/myshop_open'
                logging.info('Сидим в лавке')
            else:
                client.send_message(cw, '/go')
                logging.info('Пина нет')
        elif 'Битва семи замков' in event.raw_text:
            hero_des = event.message.reply_markup.rows[1].buttons[0].text
            atk_des = event.message.reply_markup.rows[0].buttons[0].text
        if 'Ты пытался остановить' in event.raw_text or 'Ты задержал' in event.raw_text:
            if curret_pin and last_pin:
                sleep(random.randint(2, 4))
                if curret_pin == castle:
                    logging.info('Выставляем деф обратно')
                    client.send_message(cw, def_des)
                    curret_pin = False
                    last_pin = False
                elif curret_pin == '/myshop_open':
                    logging.info('Возвращаемся в лавку')
                    client.send_message(cw, curret_pin)
                    curret_pin = False
                    last_pin = False
                else:
                    logging.info('Выставляем пин обратно {}'.format(curret_pin))
                    client.send_message(cw, atk_des)
                    sleep(random.randint(2, 4))
                    client.send_message(cw, curret_pin)
                    curret_pin = False
                    last_pin = False
            else:
                curret_pin = False
                last_pin = False
                logging.info('Караван защищён')
client.idle()
