import random
from aiogram import Bot, Dispatcher
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.filters import CommandStart, Text
import os
import dotenv
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from environs import Env

env = Env()
env.read_env()

API_TOKEN = env('BOT_TOKEN')

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)],
    [KeyboardButton(text=str(i)) for i in range(7, 9)]]

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
