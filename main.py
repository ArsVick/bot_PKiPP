from config import *
from dicts import *
from telebot import types
import telebot

bot = telebot.TeleBot(token)
book, point, name, number, start_markup = None, None, None, None, None
vocab = ru_dict
phrases = ru_book
answers = ru_answers


@bot.message_handler(func=lambda message: True, commands=['start', 'help'])
def send_welcome(message: types.Message):
    global start_markup
    start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(phrases[-4])
    item2 = types.KeyboardButton(phrases[-3])
    item3 = types.KeyboardButton(phrases[-2])
    item4 = types.KeyboardButton(phrases[-1])
    start_markup.add(item1, item3, item4, item2)
    bot.send_message(message.from_user.id, answers[0], reply_markup=start_markup)


def back(message: types.Message):
    bot.send_message(message.from_user.id, "Ok", reply_markup=start_markup)


def booking(message: types.Message):
    book_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item0 = types.KeyboardButton(phrases[0])
    item1 = types.KeyboardButton(phrases[1])
    item2 = types.KeyboardButton(phrases[2])
    item3 = types.KeyboardButton(phrases[3])
    item4 = types.KeyboardButton(phrases[4])
    item5 = types.KeyboardButton(phrases[5])
    item6 = types.KeyboardButton(phrases[6])
    item7 = types.KeyboardButton(phrases[7])
    item8 = types.KeyboardButton(phrases[8])
    item9 = types.KeyboardButton(phrases[9])
    item10 = types.KeyboardButton(phrases[10])
    item11 = types.KeyboardButton(phrases[11])
    item12 = types.KeyboardButton(phrases[12])
    item13 = types.KeyboardButton(phrases[13])
    item14 = types.KeyboardButton(phrases[14])
    item15 = types.KeyboardButton(phrases[15])
    item16 = types.KeyboardButton(phrases[16])
    book_markup.add(item1, item2, item13, item4, item6, item7, item3, item15).add(item8, item9).add(item10, item14).add(
        item0).add(item5).add(item11).add(item12, item16)
    bot.send_message(message.from_user.id, answers[1], reply_markup=book_markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def repeat_all_messages(message: types.Message):
    global book, point, phrases, answers, vocab
    if message.text == '🏴󠁧󠁢󠁥󠁮󠁧󠁿EN':
        phrases = en_book
        answers = en_answers
        vocab = en_dict
        send_welcome(message)
    elif message.text == '🇷🇺RU':
        phrases = ru_book
        answers = ru_answers
        vocab = ru_dict
        send_welcome(message)
    elif message.text == phrases[-2]:
        booking(message)
    elif message.text == phrases[0]:
        menu_tmg = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        menu_tmg.add(types.KeyboardButton(text=phrases[16]))
        menu_tmg.add(types.KeyboardButton(text=phrases[20]))
        menu_tmg.add(types.KeyboardButton(text=phrases[21]))
        book = message.text
        bot.send_message(message.chat.id, answers[2], reply_markup=menu_tmg)
    elif message.text == phrases[1]:
        menu_sport = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        menu_sport.add(types.KeyboardButton(text=phrases[16]))
        menu_sport.add(types.KeyboardButton(text=phrases[17]))
        menu_sport.add(types.KeyboardButton(text=phrases[18]))
        menu_sport.add(types.KeyboardButton(text=phrases[19]))
        book = message.text
        bot.send_message(message.from_user.id, answers[3], reply_markup=menu_sport)
    elif message.text == phrases[2]:
        menu_ege = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        menu_ege.add(types.KeyboardButton(text=phrases[16]))
        menu_ege.add(types.KeyboardButton(text=phrases[22]))
        menu_ege.add(types.KeyboardButton(text=phrases[23]))
        book = message.text
        bot.send_message(message.chat.id, answers[4], reply_markup=menu_ege)
    elif message.text == phrases[3]:
        menu_lang = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        menu_lang.add(types.KeyboardButton(text=phrases[16]))
        menu_lang.add(types.KeyboardButton(text=phrases[24]))
        menu_lang.add(types.KeyboardButton(text=phrases[25]))
        book = message.text
        bot.send_message(message.chat.id, answers[5], reply_markup=menu_lang)
    elif message.text == phrases[4]:
        menu_train = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        menu_train.add(types.KeyboardButton(text=phrases[16]))
        menu_train.add(types.KeyboardButton(text=phrases[26]))
        menu_train.add(types.KeyboardButton(text=phrases[27]))
        menu_train.add(types.KeyboardButton(text=phrases[28]))
        menu_train.add(types.KeyboardButton(text=phrases[29]))
        book = message.text
        bot.send_message(message.chat.id, answers[6], reply_markup=menu_train)
    elif message.text == phrases[16]:
        back(message)
    elif message.text in phrases[17:30]:
        point = message.text
        bot.send_message(message.from_user.id, answers[7])
        bot.register_next_step_handler(message, get_name)
    elif message.text in phrases[5:16]:
        book = message.text
        point = '-'
        bot.send_message(message.chat.id, answers[7])
        bot.register_next_step_handler(message, get_name)
    elif message.text.lower() in vocab.keys():
        bot.send_message(message.chat.id, vocab.get(message.text.lower()))
    else:
        bot.send_message(message.chat.id, answers[-2])


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, answers[8])
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number
    number = message.text
    bot.send_message(id, f'Новая запись!\nУслуга : {book}, Категория : {point}, Имя : {name}, Телефон : {number}')
    bot.send_message(message.chat.id, answers[-1], reply_markup=start_markup)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
