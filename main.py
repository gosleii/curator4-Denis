import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State


state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6914517822:AAFjiX94tgB5F45PnQ4d0fVkcSk_9VgTXoI",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "опрос"  # Можно менять текст
text_button_1 = "Роботехника"  # Можно менять текст
text_button_2 = "Хайтек"  # Можно менять текст
text_button_3 = "ГеоАэро"  # Можно менять текст
text_button_4 = "Биоквантум"  # Можно менять текст



menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    ),
    telebot.types.KeyboardButton(
        text_button_4,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Здравствуйте! Вас приветствует телеграмм-бот Кванториума!',  # Можно менять текст
        reply_markup=menu_keyboard)

@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id, 'Как мне к *Вам* _обращаться_?')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)


@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'Хорошо! Предлагаю Вам ознакомиться общей `информацией` о нашем[Кванториуме](http://ou151.omsk.obr55.ru/quantorium/).Для завершения регистрации напишите "Да".')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)


@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.chat.id, 'Спасибо за регистрацию!', reply_markup=menu_keyboard)  # Можно менять текст
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Запись на программы по направлению *Робототехника*: [Робо8](https://р55.навигатор.дети/program/18260-programma-robototekhnika-8-12), [Соревновательная робототехника](https://р55.навигатор.дети/program/19501-programma-sorevnovatelnaya-robototekhnika) и [Робо12](https://р55.навигатор.дети/program/18430-programma-robototekhnika-12-18-let)", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Запись на программы по направлению *Хайтек*: [Хайтек_младшая](https://р55.навигатор.дети/program/18436-khaitek-osnovy-3d-modelirovaniya-7-11-let), [Хайтек_средняя](https://р55.навигатор.дети/program/18432-3d-modelirovanie-i-prototipirovanie-12-15-let) и [Хайтек_старшая](https://р55.навигатор.дети/program/18259-programma-khaitek-3d-modelirovanie-15-18-let)", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Запись на программы по направлению *ГеоАэро*: [ГЕО](https://р55.навигатор.дети/program/18261-programma-geoaero), [Аэромоделирование](https://р55.навигатор.дети/program/18424-programma-geoaero-aeromodelirovanie) и [Пилотирование БПЛА](https://р55.навигатор.дети/program/21387-programma-geo-aero-proektirovanie-bpla)", reply_markup=menu_keyboard)  # Можно менять текст

@bot.message_handler(func=lambda message: text_button_4 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Запись на программы по направлению *Биоквантум*: [БиоХим-Мастер](https://р55.навигатор.дети/program/21399-programma-biokhim-master)", reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()

