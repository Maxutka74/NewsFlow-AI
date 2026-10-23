from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.bot.keyboards.main import cancel_button
from app.bot.states.editing import EditPost

router_moderation = Router()

@router_moderation.callback_query(F.data.startswith('approve:'))
async def approve(callback: CallbackQuery):
    await callback.answer()
    post_id = callback.data.split(':')[1]
    pass

@router_moderation.callback_query(F.data.startswith('regenerate:'))
async def regenerate(callback: CallbackQuery):
    await callback.answer()
    post_id = callback.data.split(':')[1]
    pass

@router_moderation.callback_query(F.data.startswith('edit:'))
async def edit(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    post_id = callback.data.split(':')[1]
    await state.update_data(edit=post_id)
    await callback.message.answer(
        '✏️ Редагування новини\n\n'
        '📝 Напишіть, що саме потрібно змінити в новині.\n'
        'Наприклад: скоротити текст, змінити заголовок або стиль викладу.', reply_markup=cancel_button('Скасувати редагування')
    )
    await state.set_state(EditPost.edit)

@router_moderation.message(EditPost.edit)
async def edit_post(message: Message, state: FSMContext):
    data = await state.get_data()
    post_id = data['edit']
    text_change = message.text
    if not text_change:
        await message.answer('Надішліть текстову інструкцію')
        return
    await message.answer(
        '✅ Інструкцію для редагування отримано!\n'
        '🤖 Вона буде використана для оновлення новини після підключення AI.'
    )
    await state.clear()

@router_moderation.callback_query(EditPost.edit, F.data == 'cancel_url')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer('Редагування скасовано')

@router_moderation.callback_query(F.data.startswith('reject:'))
async def reject(callback: CallbackQuery):
    await callback.answer()
    post_id = callback.data.split(':')[1]
    pass

