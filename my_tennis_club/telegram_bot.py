import os,django
from my_tennis_club.settings import DATABASES,INSTALLED_APPS
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_tennis_club.settings')
django.setup()
import telebot
from telebot import types # для указание типов
import word_generate as mymodule
import wact_generate as mymodule2
from dotenv import load_dotenv
# Replace ‘YOUR_API_TOKEN’ with the API token you received from the BotFather
from members.models import Journal, Errors
import datetime
# import logging
# from systemd import journal
# log = logging.getLogger('demo')
# log.addHandler(journal.JournaldLogHandler())
# log.setLevel(logging.INFO)




load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def clientId(message):
    # cid = m.chat.id
    try:
        global clientArray 
        clientArray = [ 0 , []] 
        mesg = bot.send_message(message.chat.id,'Введите id клиента:')
        bot.register_next_step_handler(mesg, loop1)
    except Exception as e:      # works on python 3.x
        print('Failed 1: %s', repr(e))
        Errors.objects.create(description=str(e))
def loop1(message):
    try:
        if message.text == 'rs':
            bot.clear_step_handler_by_chat_id(message.chat.id)
        else:
            clientArray[0] = message.text
            # bot.send_message(message.chat.id, message.text)
            mesg = bot.send_message(message.chat.id,'Введите наименование товара')
            bot.register_next_step_handler(mesg,loopGoods1)
    except Exception as e:      # works on python 3.x
        print('Failed 2: %s', repr(e))
        Errors.objects.create(description=str(e))

def loopGoods1(message):
    try:
        if message.text == 'rs':
            bot.clear_step_handler_by_chat_id(message.chat.id)
        else:
            clientArray[1].append([])
            clientArray[1][len(clientArray[1]) - 1].append(message.text)
            mesg = bot.send_message(message.chat.id,'Введите кол-во единиц товара')
            bot.register_next_step_handler(mesg,loopGoods2)
    except Exception as e:      # works on python 3.x
        print('Failed 3: %s', repr(e))
        Errors.objects.create(description=str(e))
def loopGoods2(message):
    try:
        if message.text == 'rs':
            bot.clear_step_handler_by_chat_id(message.chat.id)
        else:
            clientArray[1][len(clientArray[1]) - 1].append(message.text)

            mesg = bot.send_message(message.chat.id,'Введите цену единицы товара')
            bot.register_next_step_handler(mesg,loopGoods3)
    except Exception as e:      # works on python 3.x
        print('Failed 4: %s', repr(e))
        Errors.objects.create(description=str(e))
    
def loopGoods3(message):
    try:
        if message.text == 'rs':
            bot.clear_step_handler_by_chat_id(message.chat.id)
        else:
            clientArray[1][len(clientArray[1]) - 1].append(message.text)

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            bt1 = types.KeyboardButton('Добавить товар!')
            bt2 = types.KeyboardButton('Генероривать документ!')
            markup.add(bt1, bt2)
            msg = bot.send_message(message.chat.id, 'Выберите действия:',
                                reply_markup=markup)
            bot.register_next_step_handler(msg, switch)
    except Exception as e:      # works on python 3.x
        print('Failed 5: %s', repr(e))
        Errors.objects.create(description=str(e))

def switch(message):
    try:
        if message.text == 'rs':
            bot.clear_step_handler_by_chat_id(message.chat.id)
        else:
            chat_id = message.chat.id

            if message.text == 'Добавить товар!':
                x1 = 'Введенная строка \n'
                for x in clientArray[1][len(clientArray[1]) - 1]:
                    x1 += str(x) + '\n'
                bot.send_message(message.chat.id, x1)
                mesg = bot.send_message(message.chat.id,'Введите наименование нового товара')
                bot.register_next_step_handler(mesg,loopGoods1)

            elif message.text == 'Генероривать документ!':
                todayDate = datetime.datetime.today().strftime("%d%m%y")
                print(1, type(todayDate), todayDate)
                x1 = None

                if Journal.objects.filter(name=todayDate).exists():
                    getDay = Journal.objects.filter(name=todayDate).get()
                    x1 = int(getDay.number) + 1
                    getDay.number = x1
                    getDay.save()
                    # Journal.objects.filter(name=todayDate).update(number=(int(x1) + 1))
                else:
                    Journal.objects.create(name=todayDate, number=1)
                    x1 = 1

                bot.send_document(message.chat.id, mymodule.word_generate(clientArray, x1), visible_file_name='счет.docx')
                bot.send_document(message.chat.id, mymodule2.word_generate(clientArray, x1), visible_file_name='акт приемки.docx')

            else:
                bot.send_message(message.chat.id,'Ошибка, начните заново с команды /start !')
    except Exception as e:      # works on python 3.x
        print('', repr(e))
        bot.send_message(message.chat.id, 'Данные введены не корректно.'
                                          '\nПопробуйте еще разок, вводите данные рукой.')
        Errors.objects.create(description=str(e))
   


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Привет"):
        bot.send_message(message.chat.id, text="Привеет!)")
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..\n Я запрограммирован на следующие команды:\n /start - запуск системы генерации документов ")



bot.polling(none_stop=True)

