from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command('menu'))
async def show(message: Message):
    await message.answer("Выберите стул", reply_markup=menu)


@dp.message_handler(Text(equals=["Я постою", "Второй стул",
                                 "Первый стул"]))
async def get_chair(message: Message):
    await message.answer(f'Ты выбрал {message.text}. Мудрый выбор',
                         reply_markup=ReplyKeyboardRemove())
