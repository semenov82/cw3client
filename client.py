#!/usr/bin/python3
# coding=utf-8
import logging
import random
import _thread
import sys
import re
import json
import os
import traceback
import config
from random import SystemRandom
from time import time, sleep
from datetime import datetime
from getopt import getopt
from getpass import getpass
from collections import deque
from telethon import TelegramClient, events, connection
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)-3s]# %(levelname)-5s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)
logging.getLogger('telethon').setLevel(level=logging.WARNING)
cryptogen = SystemRandom()
logger = logging.getLogger(__name__)
main_chat = config.main_chat
game_bot = 265204902 # Если вдруг изменится бот, поменять
game_user = 'ChatWarsBot'
helper_game = 615010125
helper_user = 'CWCastleBot'
admin_id = config.admin_id
admin_user = config.admin_user
orders_user = config.orders_user
api_hash = config.api_hash
api_id = config.api_id
ordersman = config.ordersman 
orders = ['🐢','🍁','🌹','☘️','🦇','🖤','🍆']
hero_des = '/start'
action_list = deque([])
get_info_diff = 360
phone = ''
arenarunning = True
bone = False
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
proxy_ip = 'ru.tgproxy.today'
proxy_port = 8080
secret = 'ddfb175d6d7f820cdc73ab11edbdcdbd74'
DC1_ip = '149.154.167.40'
DC_port = 443
client = TelegramClient(fss, api_id, api_hash, update_workers=3, spawn_read_thread=False, proxy=(proxy_ip, proxy_port, secret),  connection=connection.tcpmtproxy.ConnectionTcpMTProxy)
client.session.set_dc(1, DC1_ip, DC_port)
client.start()
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
logging.debug('Загружаем юзеров...')
client.get_entity(game_user)
client.get_entity(helper_user)
client.get_entity(admin_user)
while len(orders_user) > 0 and '0' not in orders_user:
    client.get_entity(orders_user.pop())
logging.debug('Загрузка завершена')
try:
    tweens = os.listdir('./configs/')
except:
    os.mkdir('./configs/')
    tweens = os.listdir('./configs/')
tween = str(client.get_me().id) + '.json'
twos = './configs/' + tween
if tween in tweens:
    logging.debug('Загружаю данные из конфига...')
    with open(twos, 'r') as file:
        data = json.loads(file.read())
    for i in data:
        lvlup = i['lvlup']
        les = i['les']
        caravan = i['caravan']
        arena = i['arena']
        rob = i['rob']
        order = i['order']
        help = i['help']
        bog = i['bog']
        gold = i['gold']
        mountval = i['mountval']
        autodef = i['autodef']
        dice = i['dice']
        lvlprof1 = i['lvlprof1']
        lvlprof2 = i['lvlprof2']
        enable_bot = i['enable_bot']
    if lvlprof1 == 'master':
        setprof1title = '⚒Мастер📦'
    elif lvlprof1 == 'esquire':
        setprof1title = '⚔️Эсквайр🛡'
    else:
        setprof1title = 'Error'
    if lvlprof2 == 'harvester':
        setprof2title = '📦Добытчик'
    elif lvlprof2 == 'smith':
        setprof2title = '⚒Кузнец'
    elif lvlprof2 == 'alchemist':
        setprof2title = '⚗️Алхимик'
    elif lvlprof2 == 'ranger':
        setprof2title = '🏹Рейнджер'
    elif lvlprof2 == 'knight':
        setprof2title = '⚔️Рыцарь'
    elif lvlprof2 == 'keeper':
        setprof2title = '🛡Хранитель' 
    else:
        setprof2title = 'Error'
    logging.debug('Загрузка завершена')
else:
    logging.info('Новый твинк! создаю хранилище...')
    open(twos, 'tw', encoding='utf-8') # Настройки по умолчанию
    enable_bot = True
    lvlup = True
    les = True
    caravan = False
    order = True
    rob = True
    arena = True
    help = False 
    bog = False
    mountval = False
    autodef = True
    dice = False
    lvlprof1 = 'master'
    setprof1title = '⚒Мастер📦'
    lvlprof2 = 'harvester'
    setprof2title = '📦Добытчик'
    basejson = [{
    'enable_bot': enable_bot,
    'phone': phone,
    'username': client.get_me().username,
    'castle': 0,
    'gold': 0,
    'deff': 0,
    'atk': 0,
    'lvl': 0,
    'lvlup': lvlup,
    'les': les,
    'caravan': caravan,
    'rob': rob,
    'arena': arena,
    'order': order,
    'help': help,
    'bog': bog,
    'mountval': mountval,
    'autodef': autodef,
    'dice': dice,
    'lvlprof1': lvlprof1,
    'lvlprof2': lvlprof2,
}]
    with open (twos, 'w') as file:
        json.dump(basejson, file, indent=2, ensure_ascii=False)
    # первый запуск, начинаем общение с хелпером
    client.send_message(helper_game, '/start')

def worker():
    global get_info_diff
    global lt_info
    global enable_bot
    global hero_des
    lt_info = 0
    while True:
        try:
            if time() - lt_info > get_info_diff and enable_bot:
                lt_info = time()
                get_info_diff = cryptogen.randint(420, 900)
                client.send_message(game_bot, hero_des)
                continue # Параметр get_info_diff можно менять в любой момент
            if len(action_list): # задаёт промежуток обновления профиля
                if enable_bot:
                    move = action_list.popleft()
                    logging.debug('отправляем ' + str(move))
                    client.send_message(game_bot, move)
                else:
                    logging.debug('Проёбываемся в отключке хыхыхы')
            sleep_time = cryptogen.randint(5, 8)
            sleep(sleep_time)
        except Exception as e:
            logging.exception(e)
@client.on(events.NewMessage)
def all_messages(event):
    global enable_bot
    global help
    global bog
    global autodef
    global mountval
    global les
    global caravan
    global arena
    global lvlup
    global rob
    global order
    global gold
    global arenarunning
    global littleinfo
    global castle
    global name
    global dice
    global level
    global bone
    global dmg
    global deff
    global status
    global endurance
    global endurancemax
    global last_msg
    global hero_msg
    global atk_des
    global def_des
    global hero_des
    global setprof1
    global setprof2
    if event.message.from_id == game_bot and not enable_bot and rob and re.search('\/go', event.raw_text):
        sleep(cryptogen.randint(5, 9))
        client.send_message(game_bot, '/go') # Через 5-9 секунд ебашим караван даже если бот выключен
        logging.info('Отправляем /go')
    elif event.message.from_id == game_bot and enable_bot:
        logging.info('Получили сообщение от чв')
        # logging.info(event) # если боишься, что изменили кнопки - раскоменть и через терминал посмотри кнопки
        # logging.info(event.message.reply_markup.rows[0].buttons[0].text)
        last_msg = event.raw_text
        if 'Битва семи замков' in event.raw_text:
            hero_msg = event.raw_text
            hero_des = event.message.reply_markup.rows[1].buttons[0].text
            atk_des = event.message.reply_markup.rows[0].buttons[0].text
            def_des = event.message.reply_markup.rows[0].buttons[1].text
            if 'Жми /level_up' in event.raw_text:
                if lvlup:
                    logging.info('Лвлап, качаем')
                    action_list.append('/level_up')
                else:
                    logging.info('Лвлап, но выключен((')
            castle = re.search('(.{1})(.{0,50}) .+ (Тортуги|Оплота|Скалы|Фермы|Ночи|Амбера|Рассвета)', event.raw_text).group(1)
            castlename = re.search('(.{1})(.{0,50}) .+ (Тортуги|Оплота|Скалы|Фермы|Ночи|Амбера|Рассвета)', event.raw_text).group(3)
            names = re.search('(.{1})(.{0,50}) .+ (Тортуги|Оплота|Скалы|Фермы|Ночи|Амбера|Рассвета)', event.raw_text).group(2)
            name = castle+names
            endurance = int(re.search('Выносливость: (\d+)', event.raw_text).group(1))
            endurancemax = int(re.search('Выносливость: (\d+)/(\d+)', event.raw_text).group(2))
            gold = int(re.search('💰(-?[0-9]+)', event.raw_text).group(1))
            dmg = int(re.search('⚔Атака: (\d+) 🛡Защита: (\d+)', event.raw_text).group(1))
            deff = int(re.search('⚔Атака: (\d+) 🛡Защита: (\d+)', event.raw_text).group(2))
            level = int(re.search('🏅Уровень: (\d+)', event.raw_text).group(1))
            status = re.search('Состояние:\n(.*)', event.raw_text).group(1)
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                i['castle'] = castlename
                i['gold'] = gold
                i['lvl'] = level
                i['atk'] = dmg
                i['deff'] = deff
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            if re.search('Битва семи замков через (\d+) (мин\.!|минуты!|минуту!)', event.raw_text):
                TimeToBattle = int(re.search('Битва семи замков через (\d+) (мин\.!|минуты!|минуту!)', event.raw_text).group(1))
                if TimeToBattle <= 25 and '⚔Атака' not in status: # за 25 минут до битвы перестаём чёта делать
                    status = 'До битвы осталось {} мин.'.format(TimeToBattle)
                    if autodef:
                        button = event.message.reply_markup.rows[0].buttons[1].text
                        action_list.append(button)
                    else:
                        logging.info('Автодеф выключен, ждём битвы')
                else:
                    logging.info('{} мин. до битвы'.format(TimeToBattle))
            if status == '🛌Отдых' or '🛡Защита' in status:
                buttonquest = event.message.reply_markup.rows[0].buttons[2].text
                buttoncastle = event.message.reply_markup.rows[1].buttons[1].text
                if les or mountval or bog or caravan:
                    if endurance > 1 and not caravan: # Всегда будем оставлять 1 стамину для ручного задания
                        logging.info('Идём за квестом')
                        action_list.append(buttonquest)
                    elif endurance > 2 and caravan:
                        logging.info('Идём за квестом')
                        action_list.append(buttonquest)
                if arena or dice:
                    if arena and endurance <= 1 and gold >= 5 and arenarunning and level >= 5:
                        logging.info('Идём на арену')
                        action_list.append(buttonquest)
                    elif dice and endurance <= 1 and gold >=10 and not bone:
                        logging.info('Идём в кости')
                        bone = True
                        action_list.append(buttoncastle)
                else:
                    status = '💤Делать нечего'
                    logging.info('Делать нечего')
            else:
                logging.info('Статус: ' + status + ' ждём')
        elif re.search('(В лесу всякое может случиться|Проклятый лес, населенный зловещими существами.)', event.raw_text):
            if re.search('📯Арена 🔒', event.raw_text):
                arenarunning = False
                logging.info('Арена недоступна')
            else:
                arenarunning = True
            if les and endurance > 1:
                button = event.message.reply_markup.rows[0].buttons[0].text
                action_list.append(button)
                endurance -= 1
                status = '🌲В лесу'
                logging.info('Пошли в лес')
            elif caravan and endurance > 2 and level >= 5:
                button = event.message.reply_markup.rows[0].buttons[1].text
                action_list.append(button)
                endurance -= 1
                status = '🗡Грабим'
                logging.info('Пошли в корованы')
            elif arena and endurance <= 1 and gold >= 5 and arenarunning and level >= 5:
                if level < 20:
                    button = event.message.reply_markup.rows[1].buttons[0].text
                elif level >=20:
                    button = event.message.reply_markup.rows[2].buttons[0].text
                action_list.append(button)
                status = '📯Идём на арену'
                logging.info('Пошли на арену')
            elif mountval and endurance > 1 and level >= 20:
                button = event.message.reply_markup.rows[1].buttons[1].text
                action_list.append(button)
                endurance -= 1
                status = '⛰️В долине'
                logging.info('Пошли в долину')
            elif bog and endurance > 1 and level >= 20:
                button = event.message.reply_markup.rows[1].buttons[0].text
                action_list.append(button)
                endurance -= 1
                status = '🍄В болоте'
                logging.info('Пошли в болото')
            else:
                status = '💤Делать нечего'
                logging.info('Делать нечего')
        elif re.search('Таверна работает по вечерам', event.raw_text) and bone and dice:
            if re.search('(🌙Ночь|🌙Вечер)', event.raw_text):
                logging.info('Идём играть в кости')
                button = event.message.reply_markup.rows[0].buttons[1].text
                action_list.append(button)
            else:
                bone = False
                logging.info('Таверна закрыта, никаких костей')
        elif 'азартных воинов:' in event.raw_text and bone and dice:
            bone = False
            button = event.message.reply_markup.rows[0].buttons[1].text
            action_list.append(button)
            status = '🎲Играем в кости'
            logging.info('🎲Играем в кости')
        elif '🎲Вы бросили кости на стол:' in event.raw_text:
            if re.search('{}: .* \((\d+)\)\n.*\((\d+)\)'.format(name), event.raw_text):
                me = int(re.search('{}: .* \((\d+)\)\n.*\((\d+)\)'.format(name), event.raw_text).group(1))
                notme = int(re.search('{}: .* \((\d+)\)\n.*\((\d+)\)'.format(name), event.raw_text).group(2))
            elif re.search('.*\((\d+)\)\n{}: .* \((\d+)\)'.format(name), event.raw_text):
                me = int(re.search('.*\((\d+)\)\n{}: .* \((\d+)\)'.format(name), event.raw_text).group(2))
                notme = int(re.search('.*\((\d+)\)\n{}: .* \((\d+)\)'.format(name), event.raw_text).group(1))
            if me > notme:
                gold += 20
                logging.info('Победили в костях!, золото: {}'.format(gold))
                if dice and gold >= 10:
                    logging.info('Идём ещё раз в кости')
                    action_list.append('🎲Играть в кости')
                else:
                    logging.info('Ну можно было бы и ещё сходить..')
            elif me < notme:
                gold -= 20
                logging.info('Проиграли в костях, эх бля')
                if dice and gold >= 10:
                    logging.info('Идём ещё раз в кости')
                    action_list.append('🎲Играть в кости')
                else:
                    if gold < 10:
                        logging.info('Не хватает {} золота для костей'.format(10-gold))
                    else:
                        logging.info('Ну можно было бы и ещё сходить..')
            elif me == notme:
                logging.info('Ничья??')
                action_list.append(hero_des)
        elif re.search('\/go', event.raw_text) and rob:
            sleep(cryptogen.randint(5, 160))
            client.send_message(game_bot, '/go') # Через 5-160 секунд ебашим караван
            logging.info('Отправляем /go')
        elif re.search('\/pledge', event.raw_text):
            action_list.append('/pledge')
            logging.info('Принимаем предложение деревни')
        elif re.search('\/engage', event.raw_text):
            action_list.append('/engage')
            logging.info('атакуем моба!')
        elif re.search('\/tributes', event.raw_text):
            action_list.append('/tributes')
            logging.info('Пожинаем плоды деревни')
        elif re.search('(\/skill_.*|\/learn_.*)', event.raw_text) and lvlup:
            skills = random.choice(re.findall(r'(\/skill_.*|\/learn_.*)', event.raw_text))
            action_list.append(skills) # Качаем рандомный скилл
            logging.info('Качаем ' + skills)
        elif re.search('Code \d+ to authorize (.*)\.', event.raw_text):
            if re.search('Code \d+ to authorize (.*)\.', event.raw_text).group(1) == helper_user:
                client.forward_messages(helper_user, event.message.id, event.message.from_id)
                logging.info('Пересылаем код авторизации в хелпера')
        elif 'У тебя нет денег, чтобы оплатить вход.' in event.raw_text:
            logging.info('Денег на арену нет')
            gold = 0
        elif 'Арена закрыта на ночь.' in event.raw_text:
            logging.info('Арена закрыта на ночь, отключаю')
            arenarunning = False
        elif 'Подходящий соперник не найден, попробуй позже.' in event.raw_text:
            logging.info('Не нашли противника, печалька')
            gold += 5
        elif 'Цена за вход: 5💰' in event.raw_text:
            arena_last = re.search('Поединков сегодня: (\d+)\/(\d+)', event.raw_text).group(1)
            arena_all = re.search('Поединков сегодня: (\d+)\/(\d+)', event.raw_text).group(2)
            if arena_last < arena_all and arenarunning:
                logging.info('Пошли на арену')
                button = event.message.reply_markup.rows[0].buttons[1].text
                action_list.append(button)
                gold -= 5
            else:
                arenarunning = False
                logging.info('Арена на сегодня всё')
                button = event.message.reply_markup.rows[1].buttons[1].text
                action_list.append(button)
        elif 'Рейтинги обновлены' in event.raw_text:
            logging.info('Арена ВСЁ')
            action_list.append(hero_des)
        elif 'Жажда крови одолела тебя, ты пошел на Арену.' in event.raw_text:
            status = '📯На арене'
            logging.info('Поиск противника')
            
        elif re.search('Получено: \d+ опыта and \d+ золотых монет', event.raw_text) or \
            'Прогуливаясь неподалеку' in event.raw_text or 'Ночная прохлада обволакивала тебя' in event.raw_text or \
            'Walking through the swamp' in event.raw_text or 'На улице стояла прекрасная погода' in event.raw_text or \
            'Притомившись от долгой прогулки' in event.raw_text or 'Mrrrrgl mrrrgl mrrrrrrgl mrrrgl.' in event.raw_text:
            logging.info('завершили квест')
            action_list.append(hero_des)
            
        elif 'You are not a little boy anymore' in event.raw_text and lvlup:
            if setprof1 == 'master':
                button = event.message.reply_markup.rows[0].buttons[0].text
                action_list.append(button)
            elif setprof1 == 'esquire':
                button = event.message.reply_markup.rows[1].buttons[0].text
                action_list.append(button)
            if main_chat != 0:
                client.send_message(main_chat, 'Прокачали профу {}'.format(button))
            logging.info('Прокачали профу {}'.format(button))
        elif "You served your castle bravely and honourably" in event.raw_text \
            or "you're done with your apprenticeship, but now it’s time to decide your path" in event.raw_text:
            if setprof2 == 'alchemist':
                button = event.message.reply_markup.rows[0].buttons[0].text
                action_list.append(button)
            elif setprof2 == 'harvester':
                button = event.message.reply_markup.rows[0].buttons[1].text
                action_list.append(button)
            elif setprof2 == 'smith':
                button = event.message.reply_markup.rows[1].buttons[0].text
                action_list.append(button)
            elif setprof2 == 'knight':
                button = event.message.reply_markup.rows[1].buttons[0].text
                action_list.append(button)
            elif setprof2 == 'ranger':
                button = event.message.reply_markup.rows[0].buttons[1].text
                action_list.append(button)
            elif setprof2 == 'keeper':
                button = event.message.reply_markup.rows[0].buttons[0].text
                action_list.append(button)
            logging.info('Прокачали профу {}'.format(button))
            if main_chat != 0:
                client.send_message(main_chat, 'Прокачали профу {}'.format(button))
    elif event.message.from_id == helper_game and help:
        if '🇺🇸 Select your language' in event.raw_text:
            sleep(1)
            client.send_message(helper_game, '🇷🇺 Русский')
        elif 'Готово! Русский установлен.' in event.raw_text:
            sleep(1)
            client.send_message(helper_game, '👤Я')
        elif re.search('(\/grantProfile)', event.raw_text):
            sleep(1)
            client.send_message(helper_game, '/grantProfile')
        elif re.search('(\/auth)', event.raw_text):
            sleep(1)
            client.send_message(helper_game, '/auth')
        elif 'Отличная работа! Вы были успешно авторизованы' in event.raw_text:
            sleep(1)
            client.send_message(helper_game, '/update')
        elif 'Вы не предоставили доступ /grantHelp' in event.raw_text:
            sleep(1)
            client.send_message(helper_game, '/grantTrade')
        elif 'Спасибо! Регистрация завершена.' in event.raw_text:
            sleep(2)
            client.send_message(helper_game, '/settings')
            sleep(2)
            client.send_message(helper_game, '/sett_showintop')
            sleep(2)
            client.send_message(helper_game, '/sett_msg_profile')
            sleep(2)
            client.send_message(helper_game, '/sett_msg_report')
            sleep(2)
            client.send_message(helper_game, '/sett_msg_ex_notification')
            sleep(2)
            client.send_message(helper_game, '/sett_msg_stock')
            sleep(2)
            client.send_message(helper_game, '/grantTrade')
        elif '⚖️Exchange slot' in event.raw_text:
            item = re.search('([a-zA-Z]{0,}) (\d+) x (\d+)💰 = (\d+)💰', event.raw_text).group(1)
            min = int(re.search('([a-zA-Z]{0,}) (\d+) x (\d+)💰 = (\d+)💰', event.raw_text).group(3))
            if min <= gold:
                client(GetBotCallbackAnswerRequest(event.message.to_id,event.message.id,data=event.message.reply_markup.rows[1].buttons[0].data))
                logging.info('Покупаем {}'.format(item))
            else:
                logging.info('Для покупки не хватает {} голда'.format(min-gold))
        elif 'Вы смогли купить' in event.raw_text:
            buys = re.search('Вы смогли купить: (.*)', event.raw_text).group(1)
            logging.info('Покупаем '+buys)
            client.send_message(main_chat, 'Купили на бирже: {}'.format(buys))
        elif 'Мда, не густо золотишка...' in event.raw_text or 'Маловато золотишка' in event.raw_text:
            logging.info('Мало денег')
            gold = 0
    elif event.message.from_id in ordersman and not admin_id:
        logging.info('Получили сообщение от ордера')
        if event.raw_text in orders and order:
            corder = re.search('(🐢|🍁|🌹|☘️|🦇|🖤|🍆)', event.raw_text).group(1)
            if corder == castle:
                action_list.append(def_des)
            else:
                action_list.append(atk_des)
                action_list.append(corder)
            logging.info('Пин '+corder)
    elif event.message.from_id == admin_id:
        global setprof1title
        global setprof2title
        logging.info('Получили админское сообщение')
        # logging.info(event)
        if event.raw_text in orders and order:
            corder = re.search('(🐢|🍁|🌹|☘️|🦇|🖤|🍆)', event.raw_text).group(1)
            if corder == castle:
                action_list.append(def_des)
            else:
                action_list.append(atk_des)
                action_list.append(corder)
            logging.info('Пин '+corder)
        elif '#custom' in event.raw_text:
            comm = re.search('#custom (.*)', event.raw_text).group(1)
            client.send_message(event.message.to_id, f"Команда {comm} отправляется")
            action_list.append(comm)
        elif re.search('(\/g_def|\/g_atk) (.*)', event.raw_text):
            out = 'Отправляемся!\n{}'.format(event.raw_text)
            client.send_message(event.message.to_id, out)
            client.send_message(game_bot, event.raw_text)
        elif re.search('#ex_create ([a-zA-Z]{1,20}) (\d+)', event.raw_text):
            item = re.search('#ex_create ([a-zA-Z]{1,20}) (\d+)', event.raw_text).group(1)
            price = int(re.search('#ex_create ([a-zA-Z]{1,20}) (\d+)', event.raw_text).group(2))
            out = 'Запрос на покупку {} по {} за шт.'.format(item,price)
            out1 = '/ex_create' + ' ' + item + ' ' + str(price)
            client.send_message(helper_game, out1)
            client.send_message(event.message.to_id, out)
            logging.info(out)
        elif event.raw_text == '#last_msg':
            client.send_message(event.message.to_id, last_msg)
            logging.info(last_msg)
        elif event.raw_text == '#hero':
            client.send_message(event.message.to_id, hero_msg)
            logging.info(hero_msg)
        elif event.raw_text == '#info':
            littleinfo = '''
{}
🏅Уровень: {}
Статы: ⚔️{} 🛡{}
🔋Выносливость: {}/{}
💰Золото: {}
Состояние:  {}
'''.format(name,level,dmg,deff,endurance,endurancemax,gold,status)
            client.send_message(event.message.to_id, littleinfo)
            logging.info(littleinfo)
        elif event.raw_text == '#status':
            getstatus = '''
⚡️Бот включен: {12}
📯Арена: {2}
🌲Лес: {0}
⛰️Долина: {6}
🍄Болото: {7}
🐫Караваны: {1}
🗡Стоп караванов: {3}
🌟Лвлапы: {10}
⚒Первая профа: {11}
⚒Вторая профа: {13}
🏳️‍🌈Приказы: {4}
🤝Помощник: {5}
🛡АвтоДеф: {8}
🎲Кости: {9}
'''.format(les,caravan,arena,rob,order,help,mountval,bog,autodef,dice,lvlup,setprof1title,enable_bot,setprof2title)
            client.send_message(event.message.to_id, getstatus)
            logging.info(getstatus)
        elif event.raw_text == '#les':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if les:
                    i['les'] = False
                    les = False
                    client.send_message(event.message.to_id, 'Лес выключен')
                else:
                    i['les'] = True
                    les = True
                    client.send_message(event.message.to_id, 'Лес включён')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#caravan':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if caravan:
                    i['caravan'] = False
                    caravan = False
                    client.send_message(event.message.to_id, 'Караваны выключены')
                else:
                    i['caravan'] = True
                    caravan = True
                    client.send_message(event.message.to_id, 'Караваны включены')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#arena':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if arena:
                    i['arena'] = False
                    arena = False
                    client.send_message(event.message.to_id, 'Арена выключена')
                else:
                    i['arena'] = True
                    arena = True
                    client.send_message(event.message.to_id, 'Арена включена')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#rob':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if rob:
                    i['rob'] = False
                    rob = False
                    client.send_message(event.message.to_id, 'Остановка караванов выключена')
                else:
                    i['rob'] = True
                    rob = True
                    client.send_message(event.message.to_id, 'Остановка караванов включёна')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#trade':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if help:
                    i['help'] = False
                    help = False
                    client.send_message(event.message.to_id, 'Трейды с @CWCastleBot выключены')
                else:
                    i['help'] = True
                    help = True
                    client.send_message(event.message.to_id, 'Трейды с @CWCastleBot включены')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#mountval':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if mountval:
                    i['mountval'] = False
                    mountval = False
                    client.send_message(event.message.to_id, 'Долина выключена')
                else:
                    i['mountval'] = True
                    mountval = True
                    client.send_message(event.message.to_id, 'Долина включена')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#bog':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if bog:
                    i['bog'] = False
                    bog = False
                    client.send_message(event.message.to_id, 'Болото выключено')
                else:
                    i['bog'] = True
                    bog = True
                    client.send_message(event.message.to_id, 'Болото включено')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#order':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if order:
                    i['order'] = False
                    order = False
                    client.send_message(event.message.to_id, 'Пины выключены')
                else:
                    i['order'] = True
                    order = True
                    client.send_message(event.message.to_id, 'Пины включены')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#lvlup':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if lvlup:
                    i['lvlup'] = False
                    lvlup = False
                    client.send_message(event.message.to_id, 'Лвлап выключен')
                else:
                    i['lvlup'] = True
                    lvlup = True
                    client.send_message(event.message.to_id, 'Лвлап включен')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#autodef':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if autodef:
                    i['autodef'] = False
                    autodef = False
                    client.send_message(event.message.to_id, 'АвтоДеф выключен')
                else:
                    i['autodef'] = True
                    autodef = True
                    client.send_message(event.message.to_id, 'АвтоДеф включен')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#dice':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if dice:
                    i['dice'] = False
                    dice = False
                    client.send_message(event.message.to_id, 'Игра в кости выключена')
                else:
                    i['dice'] = True
                    dice = True
                    client.send_message(event.message.to_id, 'Игра в кости включена')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif '#lvlprof1' in event.raw_text:
            if 'master' in  event.raw_text:
                setprof1 = 'master'
                setprof1title = '⚒Мастер📦'
                txt = 'Первая профа выбрана: {}'.format(setprof1title)
            elif 'esquire' in  event.raw_text:
                setprof1 = 'esquire'
                setprof1title = '⚔️Эсквайр🛡' 
                txt = 'Первая профа выбрана: {}'.format(setprof1title)
            else:
                setprof1 = 'master'
                setprof1title = '⚒Мастер📦'
                txt = 'Нужно выбрать master или esquire `#lvlprof1 master`'
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                i['lvlprof1'] = setprof1
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            client.send_message(event.message.to_id, txt)
        elif '#lvlprof2' in event.raw_text:
            if 'alchemist' in  event.raw_text:
                setprof2 = 'alchemist'
                setprof2title = '⚗️Алхимик'
            elif 'harvester' in  event.raw_text:
                setprof2 = 'harvester'
                setprof2title = '📦Добытчик' 
            elif 'smith' in  event.raw_text:
                setprof2 = 'smith'
                setprof2title = '⚒Кузнец' 
            elif 'keeper' in  event.raw_text:
                setprof2 = 'keeper'
                setprof2title = '🛡Хранитель' 
            elif 'ranger' in  event.raw_text:
                setprof2 = 'ranger'
                setprof2title = '🏹Рейнджер' 
            elif 'knight' in  event.raw_text:
                setprof2 = 'knight'
                setprof2title = '⚔️Рыцарь' 
            else:
                setprof2 = 'harvester'
                setprof2title = '📦Добытчик'
                txt = 'Нужно выбрать alchemist|harvester|smith|keeper|ranger|knight `#lvlprof2 harvester`'
            txt = 'Вторая профа выбрана: {}'.format(setprof2title)
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                i['lvlprof2'] = setprof2
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            client.send_message(event.message.to_id, txt)
        elif event.raw_text == '#set_bot':
            with open(twos, 'r') as file:
                data = json.loads(file.read())
            for i in data:
                if enable_bot:
                    i['enable_bot'] = False
                    enable_bot = False
                    client.send_message(event.message.to_id, 'Бот выключен')
                else:
                    i['enable_bot'] = True
                    enable_bot = True
                    client.send_message(event.message.to_id, 'Бот включен')
            with open(twos, 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        elif event.raw_text == '#help':
            out = '''Управление твинками:
`#set_bot` - включить\выключить бота
`#info` - показать малый профиль
`#hero` - показать обычный профиль
`#status` - показать состояния переключателей
`#lvlup` - Вкл\Выкл рандомной прокачки лвла
`#les` - Вкл\Выкл леса
`#mountval` - Вкл\Выкл долины
`#bog` - Вкл\Выкл болота
`#caravan` - Вкл\Выкл караванов
`#arena` - Вкл\Выкл арены
`#rob` - Вкл\Выкл нажатия **/go**
`#trade` - Вкл\Выкл трейдов с **@CWCastleBot**
`#order` - Вкл\Выкл пинов
`#autodef` - Вкл\Выкл АвтоДеф
`#ex_create item price` - покупать из **@CWCastleBot** item по цене price
`#dice` - Вкл\Выкл игру в кости
`#last_msg` - Последнее сообщение от чв
`#lvlprof1 master/esquire` - выбрать первую профу
`#lvlprof2 alchemist|harvester|smith|keeper|ranger|knight` - выбрать вторую профу
'''
            client.send_message(event.message.to_id, out)
    elif event.message.from_id == 777000:
        logging.info('Получили сервисное сообщение')
        if 'Your login code' in event.raw_text:
            code = int(re.search('Your login code: (\d+)', event.raw_text).group(1))
            logging.info('Login code: '+str(code))
            code -= 1
            if main_chat == 0:
                client.send_message(admin_user, 'Логин код: {0}\nЧтобы он подошёл - выполните: {0} + 1 и введите результат в тг'.format(code))
            else:
                client.send_message(main_chat, 'Логин код: {0}\nЧтобы он подошёл - выполните: {0} + 1 и введите результат в тг'.format(code))
if __name__ == '__main__':
    _thread.start_new_thread(worker, ())
    client.idle()
