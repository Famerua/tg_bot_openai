from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

# fmt: off
menu = [
    [InlineKeyboardButton(text='Генерировать текст', callback_data='generate_text'), 
    InlineKeyboardButton(text='Генерировать изображение', callback_data='generate_image')], 
    [InlineKeyboardButton(text='Купить токены', callback_data='buy_tokens'),
    InlineKeyboardButton(text='Баланс', callback_data='balance')],
    [InlineKeyboardButton(text='Партнерская программа', callback_data='ref'),
    InlineKeyboardButton(text='Бесплатные токены', callback_data='free_tokens')],
    [InlineKeyboardButton(text='Помощь', callback_data='help')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu) #создание клавиатуры с помощью двумерного спика
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выйти в меню')]], resize_keyboard=True)
ieit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Выйти в меню', callback_data='menu')]])


# создание клавиатуры с помощью Builder

# builder = InlineKeyboardBuilder()
# for i in range(15):
#     builder.button(text=f”Кнопка {i}”, callback_data=f”button_{i}”)
# builder.adjust(2)
# await msg.answer(“Текст сообщения”, reply_markup=builder.as_markup())
