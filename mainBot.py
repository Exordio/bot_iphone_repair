#author: Golubev Ivan
#Bot for receiving repair orders.
#Works through webhooks

import Conf
import linecache
import random
import math
import telebot
import requests
import json
import cherrypy


webhook_host = ''
webhook_port = 443
webhook_listen = '0.0.0.0'
webhook_SSL_cert = '/home/ubuntu/certs/webher_cert.pem'
webhook_SSL_PRIV = '/home/ubuntu/certs/webher_pkey.pem'
webhook_url_kekbase = "https://%s:%s" % (webhook_host, webhook_port)
webhook_url_path = "/%s/" % (Conf.token)

bot = telebot.TeleBot(Conf.token)


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения 
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(func=lambda message: True, commands=['start'])
def Start_Command(message):
    ans = "Здравствуйте! Вас приветствует компания “LION” - выездной ремонт IPhone и IPad по Москве и Московской области."
    #bot.send_message(message.from_user.id, ans)
    userKeyboard = telebot.types.ReplyKeyboardMarkup(True, False, True)
    userKeyboard.row('Заполнить анкету на ремонт 🛠','Прайс 💰')
    userKeyboard.row('Контакты ☎')
    userKeyboard.row('Выход')
    bot.send_message(message.chat.id, ans ,reply_markup=userKeyboard)


@bot.message_handler(func=lambda message: True, commands=['stop'])
def Stop_Command(message):
    ans = "Всего наилучшего. (Команда LION)"
    hide_userKeyboard = telebot.types.ReplyKeyboardRemove(True)
    bot.send_message(message.chat.id, ans, reply_markup=hide_userKeyboard)



@bot.message_handler(func=lambda message: True, content_types=['text'])
def react_Text_Message(message):
    global XX
    global varj
    if (message.text == "Прайс 💰"):
        userKeyboard = telebot.types.ReplyKeyboardMarkup(True, False, True)
        userKeyboard.row('iPhone', 'iPad')
        userKeyboard.row('Вернуться в меню')
        XX = "Прайс"
        bot.send_message(message.from_user.id, "Вас интересуют цены на iPhone или iPad?", reply_markup=userKeyboard)
    if ((message.text == "iPhone") and (XX == "Прайс")):
        userKeyboard = telebot.types.ReplyKeyboardMarkup(True, False, True)
        userKeyboard.row('iPhone 5,5c,5s')
        userKeyboard.row('iPhone SE')
        userKeyboard.row('iPhone 6', 'iPhone 6 Plus')
        userKeyboard.row('iPhone 6S', 'iPhone 6S Plus')
        userKeyboard.row('iPhone 7', 'iPhone 7 Plus')
	userKeyboard.row('iPhone 8','iPhone 8 Plus')
	userKeyboard.row('iPhone X')
        userKeyboard.row('Вернуться в меню')
        XX = "iPhone"
        bot.send_message(message.from_user.id, "Выберите прайс на интересующее вас устройство кнопкой ниже :)", reply_markup=userKeyboard)

    if ((message.text == "iPad") and (XX == "Прайс")):
        userKeyboard = telebot.types.ReplyKeyboardMarkup(True, False, True)
        userKeyboard.row('iPad 2','iPad 3')
        userKeyboard.row('iPad 4')
        userKeyboard.row('iPad mini','iPad mini 2')
        userKeyboard.row('iPad mini 3','iPad mini 4')
        userKeyboard.row('iPad Air','iPad Air 2')
        userKeyboard.row('iPad Pro 9,7','iPad Pro 12,9')
        userKeyboard.row('Вернуться в меню')
        XX = "iPad"

        bot.send_message(message.from_user.id, "Выберите прайс на интересующее вас устройство кнопкой ниже :)", reply_markup=userKeyboard)

    if ((message.text == "iPhone 5,5c,5s") and (XX == "iPhone")):
        bot.send_message(message.from_user.id, "Прайс лист на ремонт:\niPhone 5,5c,5s :\n\n"
                                               "Замена дисплея / экрана (копия оригинального качества): 2300₽\n"
                                               "Замена дисплея / экрана (оригинал): 3600₽\n"
                                               "Замена корпуса: 2200₽\n"
                                               "Замена аккумулятора: 1800₽\n"
                                               "Замена основной камеры: 1800₽\n"
                                               "Замена передней камеры: 1700₽\n"
                                               "Замена кнопки Home: 1500₽\n"
                                               "Замена кнопки включения: 1700₽\n"
                                               "Замена кнопок громкости: 1700₽\n"
                                               "Замена кнопки переключения вибро: 1700₽\n"
                                               "Замена полифонического динамика: 1700₽\n"
                                               "Замена слухового динамика: 1600₽\n"
                                               "Замена микрофона: 1700₽\n"
                                               "Замена разъема зарядки: 1700₽\n"
                                               "Замена разъема наушников: 1700₽\n"
                                               "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone SE") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                               "iPhone SE:\n"
                                               "Замена дисплея / экрана (оригинал): 3600₽\n"
                                                "Замена корпуса: 2200₽\n"
                                                "Замена аккумулятора: 1800₽\n"
                                                "Замена основной камеры: 2000₽\n"
                                                "Замена передней камеры: 1800₽\n"
                                                "Замена кнопки Home: 1700₽\n"
                                                "Замена кнопки включения: 1800₽\n"
                                                "Замена кнопок громкости: 1800₽\n"
                                                "Замена кнопки переключения вибро: 1800₽\n"
                                                "Замена полифонического динамика: 1700₽\n"
                                                "Замена слухового динамика: 1600₽\n"
                                                "Замена микрофона: 1700₽\n"
                                                "Замена разъема зарядки: 1700₽\n"
                                                "Замена разъема наушников: 1700₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone 6") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                                "iPhone 6:\n"
                                                "Замена дисплея / экрана (копия оригинального качества): 3700₽\n"
                                                "Замена дисплея / экрана (оригинал): 5500₽\n"
                                                "Замена корпуса: 3600₽\n"
                                                "Замена аккумулятора: 2200₽\n"
                                                "Замена основной камеры: 2000₽\n"
                                                "Замена передней камеры: 2000₽\n"
                                                "Замена кнопки Home: 2000₽\n"
                                                "Замена кнопки включения: 2000₽\n"
                                                "Замена кнопок громкости: 2000₽\n"
                                                "Замена кнопки переключения вибро: 2000₽\n"
                                                "Замена полифонического динамика: 2000₽\n"
                                                "Замена слухового динамика: 1700₽\n"
                                                "Замена микрофона: 2000₽\n"
                                                "Замена разъема зарядки: 2000₽\n"
                                                "Замена разъема наушников: 2000₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone 6 Plus") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                                "iPhone 6 Plus:\n"
                                                "Замена дисплея / экрана (копия оригинального качества): 4700₽\n"
                                                "Замена дисплея / экрана (оригинал): 5900₽\n"
                                                "Замена корпуса: 3500₽\n"
                                                "Замена аккумулятора: 2300₽\n"
                                                "Замена основной камеры: 2200₽\n"
                                                "Замена передней камеры: 2100₽\n"
                                                "Замена кнопки Home: 2000₽\n"
                                                "Замена кнопки включения: 2000₽\n"
                                                "Замена кнопок громкости: 2000₽\n"
                                                "Замена кнопки переключения вибро: 2000₽\n"
                                                "Замена полифонического динамика: 1900₽\n"
                                                "Замена слухового динамика: 1900₽\n"
                                                "Замена микрофона: 2000₽\n"
                                                "Замена разъема зарядки: 2000₽\n"
                                                "Замена разъема наушников: 2000₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone 6S") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                                "iPhone 6S:\n"
                                                "Замена дисплея / экрана (копия оригинального качества): 5500₽\n"
                                                "Замена дисплея / экрана (оригинал): 7400₽\n"
                                                "Замена корпуса: 3800₽\n"
                                                "Замена аккумулятора: 2400₽\n"
                                                "Замена основной камеры: 3000₽\n"
                                                "Замена передней камеры: 2300₽\n"
                                                "Замена кнопки Home: 2000₽\n"
                                                "Замена кнопки включения: 2000₽\n"
                                                "Замена кнопок громкости: 2000₽\n"
                                                "Замена кнопки переключения вибро: 2000₽\n"
                                                "Замена полифонического динамика: 2400₽\n"
                                                "Замена слухового динамика: 2000₽\n"
                                                "Замена микрофона: 2400₽\n"
                                                "Замена разъема зарядки: 2400₽\n"
                                                "Замена разъема наушников: 2400₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone 6S Plus") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                                "iPhone 6S Plus\n"
                                                "Замена дисплея / экрана (копия оригинального качества): 6400₽\n"
                                                "Замена дисплея / экрана (оригинал): 9700₽\n"
                                                "Замена корпуса: 4200₽\n"
                                                "Замена аккумулятора: 2500₽\n"
                                                "Замена основной камеры: 3100₽\n"
                                                "Замена передней камеры: 3400₽\n"
                                                "Замена кнопки Home: 2000₽\n"
                                                "Замена кнопки включения: 2100₽\n"
                                                "Замена кнопок громкости: 2100₽\n"
                                                "Замена кнопки переключения вибро: 2100₽\n"
                                                "Замена полифонического динамика: 2400₽\n"
                                                "Замена слухового динамика: 2000₽\n"
                                                "Замена микрофона: 2500₽\n"
                                                "Замена разъема зарядки: 2500₽\n"
                                                "Замена разъема наушников: 2500₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone 7") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                                "iPhone 7\n"
                                                "Замена дисплея / экрана (копия оригинального качества): 7900₽\n"
                                                "Замена дисплея / экрана (оригинал): 11100₽\n"
                                                "Замена корпуса: 6800₽\n"
                                                "Замена аккумулятора: 2900₽\n"
                                                "Замена основной камеры: 4600₽\n"
                                                "Замена передней камеры: 4600₽\n"
                                                "Замена кнопки включения: 4100₽\n"
                                                "Замена кнопок громкости: 4100₽\n"
                                                "Замена кнопки переключения вибро: 2100₽\n"
                                                "Замена полифонического динамика: 2900₽\n"
                                                "Замена слухового динамика: 2900₽\n"
                                                "Замена микрофона: 4500₽\n"
                                                "Замена разъема зарядки: 4500₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
    if ((message.text == "iPhone 7 Plus") and (XX == "iPhone")):
        bot.send_message(message.from_user.id,
                                                "iPhone 7 Plus\n"
                                                "Замена дисплея / экрана (копия оригинального качества): 9000₽v"
                                                "Замена дисплея / экрана (оригинал): 14000₽\n"
                                                "Замена корпуса: 7200₽\n"
                                                "Замена аккумулятора: 3000₽\n"
                                                "Замена основной камеры: 8400₽v"
                                                "Замена передней камеры: 6300₽\n"
                                                "Замена кнопки включения: 6700₽\n"
                                                "Замена кнопок громкости: 6700₽\n"
                                                "Замена кнопки переключения вибро: 6700₽\n"
                                                "Замена полифонического динамика: 6300₽\n"
                                                "Замена слухового динамика: 3100₽\n"
                                                "Замена микрофона: 6700₽\n"
                                                "Замена разъема зарядки: 6700₽\n"
                                                "Наклеить защитное стекло: 800₽\n\n")
 if ((message.text == "iPhone 8") and (XX == "iPhone")):
        bot.send_message(message.from_user.id, 
						"iPhone 8\n"
						"Замена дисплея / экрана оригинал: 19.700

    if ((message.text == "iPad 2") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                               "iPad 2:\n"
                                               "Замена стекла дисплея / экрана: 4100₽\n"
                                                "Замена дисплея / экрана: 6200₽\n"
                                                "Замена аккумулятора: 4200₽\n\n"
                                                "При оформлении заказа следует уточнить у оператора цену за услугу.")
    if ((message.text == "iPad 3") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                                "iPad 3:\n"
                                                "Замена стекла дисплея / экрана: 4100₽\n"
                                                "Замена дисплея / экрана: 6200₽\n"
                                                "Замена аккумулятора: 4200₽)\n\n")
    if ((message.text == "iPad 4") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                                 "iPad 4:\n"
                                                 "Замена стекла дисплея / экрана: 4100₽\n"
                                                 "Замена дисплея / экрана: 6200₽\n"
                                                 "Замена аккумулятора: 4200₽\n\n")
    if ((message.text == "iPad mini") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                            "iPad mini:\n"
                                            "Замена стекла дисплея / экрана: 4000₽\n"
                                            "Замена дисплея / экрана: 6600₽\n"
                                            "Замена аккумулятора: 3800₽\n\n")
    if ((message.text == "iPad mini 2") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                             "iPad mini 2:\n"
                                             "Замена стекла дисплея / экрана: 4200₽\n"
                                             "Замена дисплея / экрана: 7400₽\n"
                                             "Замена аккумулятора: 4300₽\n\n")
    if ((message.text == "iPad mini 3") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                             "iPad mini 3:\n"
                                             "Замена стекла дисплея / экрана: 5400₽\n"
                                             "Замена дисплея / экрана: 7400₽\n"
                                             "Замена аккумулятора: 4500₽\n\n")
    if ((message.text == "iPad mini 4") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                            "iPad mini 4:\n"
                                            "Замена дисплея / экрана: 16300₽\n\n")
    if ((message.text == "iPad Air") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                            "iPad Air:\n"
                                             "Замена стекла дисплея / экрана: 4900₽\n"
                                             "Замена дисплея / экрана: 8500₽\n"
                                             "Замена аккумулятора: 5200₽\n\n")
    if ((message.text == "iPad Air 2") and (XX == "iPad")):
        bot.send_message(message.from_user.id,
                                            "iPad Air 2:\n"
                                            "Замена дисплея / экрана: 17300₽\n"
                                            "Замена аккумулятора: 6200₽\n\n")
    if ((message.text == "iPad Pro 9,7") and (XX == "iPad")):
        bot.send_message(message.from_user.id,"iPad Pro 9,7:\n Замена дисплея / экрана: 16700₽\n\n")
    if ((message.text == "iPad Pro 12,9") and (XX == "iPad")):
        bot.send_message(message.from_user.id,"iPad Pro 12,9:\n Замена дисплея / экрана: 29700₽\n\n")

    if (message.text == "Вернуться в меню"):
        XX = ""
        Start_Command(message)

    if (message.text == "Заполнить анкету на ремонт 🛠"):
        ans = "Заполните анкету по образцу:\n\n1. Название устройства \n2. Краткое описание проблемы\n3. Контактный телефон\n Всё в одно сообщение. (Важно отмечать пункты 1. 2. 3.)"
        XX = "Anketa"
        hide_userKeyboard = telebot.types.ReplyKeyboardRemove(True)
        bot.send_message(message.chat.id, ans, reply_markup=hide_userKeyboard)
    if ((("1." in message.text) or ("2." in message.text) or ("3." in message.text)) and (XX == "Anketa")):
        bot.send_message(message.chat.id, "Заявка успешно оформлена, вскоре с вами свяжется свободный оператор.\nПо любым вопросам звонить:\nСергей: +7 (925) 833-40-56\nКирилл:  +7 (985) 696-99-98 ")
        bot.send_message(242912995,"Получена новая заявка от @"+message.from_user.username+"\n Содержание:\n"+message.text)
        bot.send_message(431353666,
                         "Получена новая заявка от @" + message.from_user.username + "\n Содержание:\n" + message.text)
        bot.send_message(436527656,"Получена новая заявка от @" + message.from_user.username + "\n Содержание:\n" + message.text)
        XX = ""
        Start_Command(message)

    if (message.text == "Контакты ☎"):
        bot.send_message(message.chat.id, "Контакты\nСергей: +7 (925) 833-40-56\nКирилл:  +7 (985) 696-99-98")

    if (message.text == "Выход"):
        Stop_Command(message)

bot.remove_webhook()

bot.set_webhook(url=webhook_url_kekbase + webhook_url_path, certificate=open(webhook_SSL_cert, 'r'))
cherrypy.config.update({
    'server.socket_host': webhook_listen,
    'server.socket_port': webhook_port,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': webhook_SSL_cert,
    'server.ssl_private_key': webhook_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), webhook_url_path, {'/':{}})
