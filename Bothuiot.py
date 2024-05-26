import telebot # импортируем библиотеки
bot = telebot.Telebot('7105119247:AAE2aQ6c6geFINoLVGKgMRowjKTwjJtRm5s') #вводим токен
from telebot import types # импортировать типы
@bot.message_handler(comands=['start']) #стартовая команда
def startBot(message): 
    markup = types.InlineKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    bot.send_message(message.from_user.id, "Привет, задрот! Уже отработал смену?", reply_markup=markup)
    btn1 = types.KeyboardButton("Да)")
    btn2 = types.KeyboardButton ("Нет(")
    markup.add (btn1, btn2)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #Да (пизда)
    if message.text == 'Да)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Заказать альтушку на госуслугах')
        btn2 = types.KeyboardButton('Выпить пиво')
        btn3 = types.KeyboardButton('Играть всю ночь в Доту')
        btn4 = types.KeyboardButton('Рыдать в подушку')
        btn5 = types.KeyboardButton('Съехать от родителей')
        markup.add (btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "Какие планы на сегодня?", reply_markup=markup)
    elif message.text == 'Заказать альтушку на госуслугах':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn1 = types.InlineKeyboardButton(text='Нажми, чтобы чтобы заказать альтушку', url='https://esia.gosuslugi.ru/login/')
        bot.send_message(message.from_user.id, 'Нажми, чтобы чтобы заказать альтушку' + '[ссылке]https://esia.gosuslugi.ru/login/', parse_mode='Markdown')
        markup.add(btn1)
    elif message.text == 'Выпить пиво':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Балтика 9 - очень хороший выбор", reply_markup=markup)
     elif message.text == 'Играть всю ночь в Доту':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Так ты точно никогда не съедешь от родителей", reply_markup=markup)
    elif message.text == 'Рыдать в подушку':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Малыш, может стоит всё таки заказать альтушку?", reply_markup=markup)
    elif message.text == 'Съехать от родителей':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Боже, да кого ты обманываешь...", reply_markup=markup)   
    #Нет 
    elif message.text == 'Нет(':
        bot.send_message(message.from_user.id, "Пидора ответ", reply_markup=markup)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
     #Small talk
    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Саламалейкум')

    elif message.text == 'привет!':
        bot.send_message(message.from_user.id, 'Здорово, брат')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'Салам')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Устал на заводе')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'Устал на заводе')

    elif message.text == 'Что делаешь?':
        bot.send_message(message.from_user.id, 'Плачу в туалете завода')

    elif message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Плачу в туалете завода')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'Устал на заводе')
    
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
   