from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='➕ Додати URL',
                    callback_data='add_url'
                )
            ],
            [
                InlineKeyboardButton(
                    text='📰 Переглянути новини',
                    callback_data='view_news'
                )
            ]
        ]
    )

    return keyboard

def cancel_button(text: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f'❌ {text}',
                    callback_data='cancel_url'
                )
            ]
        ]
    )

    return keyboard