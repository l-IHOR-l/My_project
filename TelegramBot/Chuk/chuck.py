import requests
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

BOT_TOKEN: str = '6303185352:AAECZ7vk1ZS60d4d02HpT3G6arOvqPa3iUU'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()



@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    url_random_chuck: str = 'https://api.chucknorris.io/jokes/random'
    random_chuck: str = requests.get(url_random_chuck).json()['value']
    await message.answer(random_chuck)

@dp.message(Command(commands=['help']))
async def process_start_help(message: Message):
    await message.answer('random chuck joke')

@dp.message()
async def process_other_text_answers(message: Message):
    await message.answer('I don\'t know what you\'re talking about')


if __name__ == '__main__':
    dp.run_polling(bot)
