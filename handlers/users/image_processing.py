from aiogram import types
from PIL import Image, ImageDraw, ImageFont
from os.path import expanduser
from aiogram.types.input_file import InputFile

from loader import dp, bot
from data.config import PHOTO_PATH

@dp.message_handler(content_types=['photo'])
async def catch_photo(message: types.Message):
    await message.answer("Give me a second_0")
    await message.photo[-1].download(destination=PHOTO_PATH)
    
@dp.message_handler(content_types=['text'])
async def catch_text(message: types.Message):
    await message.answer("Give me a second_1")
    meme_text = message.text
    image = Image.open(PHOTO_PATH)
    font_type = ImageFont.truetype('arial.ttf', size=45)
    draw = ImageDraw.Draw(image)
    width, height = Image.open(PHOTO_PATH).size
    w, h = draw.textsize(meme_text)
    draw.text(((width - w) * 0.5, (height - h) * 0.75), text=meme_text, font=font_type, fill='black')
    image.save(expanduser(PHOTO_PATH))
    photo_meme = InputFile(path_or_bytesio=PHOTO_PATH)
    await bot.send_photo(chat_id = message.from_user.id,
                        photo = photo_meme)