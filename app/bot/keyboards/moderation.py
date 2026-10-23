from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def moderation_keyboard(post_id: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='✅ Схвалити',
                    callback_data=f'approve:{post_id}'
                ),
                InlineKeyboardButton(
                    text='🔄 Перегенерувати',
                    callback_data=f'regenerate:{post_id}'
                )
            ],
            [
                InlineKeyboardButton(
                    text='✏️ Редагувати',
                    callback_data=f'edit:{post_id}'
                ),
                InlineKeyboardButton(
                    text='❌ Відхилити',
                    callback_data=f'reject:{post_id}'
                )
            ]
        ]
    )

    return keyboard