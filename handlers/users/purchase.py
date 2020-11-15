from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp
from keyboards.inline.choice_buttons import choice, rickRolling_keyboard
from keyboards.inline.callback_data import buy_callback


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="Чай? Ванна? Или ничего? \n",
                        reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="tea"))
async def chose_tea(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Чай значит... Хороший выбор!")


@dp.callback_query_handler(buy_callback.filter(item_name="bath"))
async def chose_tea(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Хорошо, но горячую воду отключили")


@dp.callback_query_handler(buy_callback.filter(item_name="no"))
async def chose_tea(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Ладно...", reply_markup=rickRolling_keyboard)