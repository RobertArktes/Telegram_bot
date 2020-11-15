from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import buy_callback


choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Чай",
                                          callback_data=buy_callback.new(
                                              item_name="tea")
                                      ),
                                      InlineKeyboardButton(
                                          text="Ванну",
                                          callback_data=buy_callback.new(
                                              item_name="bath")
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Нет.",
                                          callback_data=buy_callback.new(
                                              item_name="no")
                                      )
                                  ]
                              ])

rickRolling_keyboard = InlineKeyboardMarkup()

RICKROLLINK = "https://youtu.be/dQw4w9WgXcQ"

rickRolling_link = InlineKeyboardButton(text="У меня есть для тебя кое-что другое",
                                        url=RICKROLLINK)

rickRolling_keyboard.insert(rickRolling_link)
