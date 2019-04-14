import os
from getpass import getpass
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
api_id = 203699
api_hash = '682323eb50adf409b423d905e432d850'
def login_user():
    phone = (input('Номер телефона: '))
    try:
        os.listdir('./sessions/')
    except:
        os.mkdir('./sessions/')
    action = "./sessions/" + phone + '.session'
    client = TelegramClient(action, api_id, api_hash, update_workers=3, spawn_read_thread=False)
    client.connect()
    client.send_code_request(phone)
    print('Внимание, если ты где-то ошибся, удали из папки sessions файл {}.session'.format(phone))
    try:
        client.sign_in(phone, input('Код из телеграмма: '))
    except SessionPasswordNeededError:
        get_pass()
    print('Успешно!')
    new_login()
def get_pass():
    try:
        password = getpass('Введи пароль: ')
        client.sign_in(password=password)
        print('Успешно!')
        new_login()
    except:
        get_pass()
def new_login():
    out = 'Ещё один аккаунт? Y(es) or N(o): '
    nextstep = input(out)
    if nextstep in ['Yes','yes','Y','y']:
        login_user()
    else:
        exit()
if __name__ == '__main__':
    login_user()