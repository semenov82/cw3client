# Chat-Wars-Bot
### Внимание!
Телеграм ввёл некоторые новые правила, теперь он может удалить аккаунт без предупреждения<br />
чтобы избежать этого, нужен аккаунт, хотя бы полгода активный, тогда СКОРЕЕ ВСЕГО (но это не точно)<br />
бана можно избежать<br />
З.Ы<br />
Телега банит за спам, но можно получить разбан на аккаунт (проверено)<br />
Пишите на `recover@telegram.org` для разбана, они проведут проверку<br />
если аккаунт действительно никогда не был в спаме, то аккаунт разбанят и бот будет работать нормально<br />

Бот для текстовой мморпг Chat Wars 3 в Telegram 0.9.1 Beta<br />
Если вы обновляете бота, удалите всё из папки configs<br />
Ишью писать [сюда](https://github.com/Feno4ka/Chat-Wars-Bot-3)<br />
##### З.Ы
~~За денежку подержу ваш акк на своём сервере или настрою вам сервер~~. Принимаю благодарности на карту 5321 3045 3235 3809 (рокетбанк) Ваш [@Fenicu](https://t.me/Fenicu)

#### Гайд как создать свою фермочку [тут](http://git.fenicu.men/Fenicu/Chat-Wars-Bot-3/src/branch/master/guide.md)<br />

#### Работающие функции бота:
  - ходить на битвы по пину/автодеф
  - ходить в лес/корованы/арена/болото/долина
  - защищать корованы и деревни
  - качает рандомные статы/заранее заданный класс
  - играть в кости
  - при потере доступа к аккаунту пришлёт код в чат
  - принимает трейды в @CWCastleBot
  - подсчёт статистики фермы
#### Минимальный бот:
    нажимает /go, /pledge, /engage<br />
    если был пин или кузнец был в лавке, он пойдёт по нужному пину или обратно в лавку<br />
    чтобы его запустить, настраивать конфиг не нужно, запускается так: `python3 minimal.py -p number` Где number - номер телефона
#### Как запустить:<br />
  1) Устанавливаем pip3: `apt-get install python3-pip`<br />
  2) Устанавливаем пакеты `pip3 install 'requests==2.19.1'`<br />
  2) Устанавливаем telethon `pip3 install 'telethon==0.19.1'`<br />
  3) Качаем этот клиент (`git clone http://git.fenicu.men/Fenicu/Chat-Wars-Bot-3.git`)<br />
  4) В папке с проектом создать папки configs и sessions<br />
  5) Заходим на сайт https://my.telegram.org логинимся, создаём любое приложение и копируем api_id и api_hash (нужно 1 раз сделать)<br />
  6) Заполняем файл config по рекомендациям внутри конфига<br />
  7) Запускаем `python3 client.py -p number` Где number - номер телефона в любом формате<br />
  8) Для работы бота помощника установим бот АПИ `pip3 install pyTelegramBotAPI` создаём через @BotFather бота и в конфиг впишем токен<br />
  9) Для запуска бота помощника запустим скрипт `python3 helper.py` (polling)<br />
#### Использование:<br />
  - Создайте приватный чат с твинками, добавьте их всех в этот чат
  - Добавьте вашего бота помощника по ферме (если вы его сделали)
  - Добавьте бота/человека которого указали ордером
  - Для ручной настройки бота введите в чат команду #help и бота покажут как ими управлять
  - Для ведения статистики админ должен написать команду /start в бота помощника по ферме