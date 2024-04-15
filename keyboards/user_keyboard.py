from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_row1 = [
        KeyboardButton(text="📑 Декларація"),
        KeyboardButton(text="👨‍⚕️ Запис"),
    ]
    keyboard.add(*buttons_row1)
    buttons_row2 = [
        KeyboardButton(text="❔ Поставити питання"),
    ]
    keyboard.add(*buttons_row2)
    return keyboard


def get_confirmation_markup():
    confirm_markup = InlineKeyboardMarkup(row_width=2)
    confirm_markup.add(
        InlineKeyboardButton(text="Так ✅", callback_data="confirm_yes"),
        InlineKeyboardButton(text="Ні ❌", callback_data="confirm_no")
    )
    return confirm_markup

def get_declaration_data_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('Надіслати номер телефону📞', request_contact=True))
    markup.add(KeyboardButton('🔙 Назад'))
    return markup

def get_back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('🔙 Назад'))
    return markup

