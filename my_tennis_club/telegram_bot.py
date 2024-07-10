import os,django
from my_tennis_club.settings import DATABASES,INSTALLED_APPS
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_tennis_club.settings')
django.setup()
import telebot
from telebot import types # для указание типов
import word_generate as mymodule
from dotenv import load_dotenv
# Replace ‘YOUR_API_TOKEN’ with the API token you received from the BotFather


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# Define a command handler
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, 'Введите имя клиента:')

#     bot.reply_to(message, message.text)
#     # bot.send_document(message.chat.id, 'https://kopi34.ru/file/home/samokleyky.png')
#     bot.send_document(message.chat.id, mymodule.word_generate(), visible_file_name='report.docx')
#     # return send_file(file_stream, as_attachment=True, attachment_filename='report_'+user_id+'.docx')

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
def loop1(message):
    try:
        clientArray[0] = message.text
        # bot.send_message(message.chat.id, message.text)
        mesg = bot.send_message(message.chat.id,'Введите наименование товара')
        bot.register_next_step_handler(mesg,loopGoods1)
    except Exception as e:      # works on python 3.x
        print('Failed 2: %s', repr(e))
def loopGoods1(message):
    try:
        clientArray[1].append([])
        clientArray[1][len(clientArray[1]) - 1].append(message.text)

        mesg = bot.send_message(message.chat.id,'Введите кол-во единиц товара')
        bot.register_next_step_handler(mesg,loopGoods2)
    except Exception as e:      # works on python 3.x
        print('Failed 3: %s', repr(e))
def loopGoods2(message):
    try:
        clientArray[1][len(clientArray[1]) - 1].append(message.text)

        mesg = bot.send_message(message.chat.id,'Введите цену единицы товара')
        bot.register_next_step_handler(mesg,loopGoods3)
    except Exception as e:      # works on python 3.x
        print('Failed 4: %s', repr(e))
    
def loopGoods3(message):
    try:
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

def switch(message):
    try:
        chat_id = message.chat.id

        if message.text == 'Добавить товар!':
                mesg = bot.send_message(message.chat.id,'Введите наименование товара')
                bot.register_next_step_handler(mesg,loopGoods1)

        elif message.text == 'Генероривать документ!':
            bot.send_document(message.chat.id, mymodule.word_generate(clientArray), visible_file_name='report.docx')

        else:
            bot.send_message(message.chat.id,'Ошибка, начните заново с команды /start !')
    except Exception as e:      # works on python 3.x
        print('Failed to upload to ftp: %s', repr(e))
   




# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#      if call.message:
#         if call.data == "help":
#             bot.send_message(call.message.chat.id, "Hi \n\n Welcome To TweenRoBOT \n\n Please Choose One :)")
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Coming Soon :D")
#      if call.message:
#         if call.data == "amir":
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="TweenRoBOT Created By @This_Is_Amir And Written In Python")
#      if call.message:
#         if call.data == "sticker":
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=":D")
#             # r = redis.hget('file_id',call.message.chat.id)
#             bot.send_sticker(call.message.chat.id, '{}'.format(r))
#      if call.message:
#         if call.data == "document":
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=":D")
#             # r = redis.hget('file_id',call.message.chat.id)
#             bot.send_document(call.message.chat.id, '{}'.format(r))
#      if call.message:
#         if call.data == "video":
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=":D")
#             # r = redis.hget('file_id',call.message.chat.id)
#             bot.send_video(call.message.chat.id, '{}'.format(r))
#      if call.message:
#         if call.data == "photo":
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=":D")
#             # r = redis.hget('file_id',call.message.chat.id)
#             bot.send_photo(call.message.chat.id, '{}'.format(r))
#      if call.message:
#         if call.data == "Audio":
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text=":D")
#             # r = redis.hget('file_id',call.message.chat.id)
#             bot.send_audio(call.message.chat.id, '{}'.format(r))


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "? Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("? Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")



bot.polling(none_stop=True)

