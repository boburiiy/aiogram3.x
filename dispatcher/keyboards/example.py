from aiogram.types import \
    InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, \
    InlineKeyboardButton, \
    KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
reply_keyboard = [
    [
        KeyboardButton(text="col 1 row 1"),
    ],
    [
        KeyboardButton(text="col 1 row 2"),
    ]
]

inline_keyboard = [
    [
        InlineKeyboardButton(text="col 1 row 1", callback_data="col_1_row_1"),
    ],
    [
        InlineKeyboardButton(text="col 1 row 2", callback_data="col_1_row_2"),
    ],
    [
        InlineKeyboardButton(text="New Button", callback_data="new_button_callback"),
    ]
]

kb2 = InlineKeyboardMarkup(
    inline_keyboard=inline_keyboard
)

kb1 = ReplyKeyboardMarkup(
    keyboard=reply_keyboard, resize_keyboard=True, input_field_placeholder="Enter your message here",
)
