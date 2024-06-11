from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# API_TOKEN:str = 'YOUR_BOT_TOKEN'
API_TOKEN:str = "YOUR_TOKEN"
dp:Dispatcher = Dispatcher()
bot:Bot = Bot(token=API_TOKEN)

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name is Echo-bot!\nMy name is Echo-bot')

@dp.message(Command(commands=['help']))
async def process_start_command(message: Message):
    await message.answer('Write me something in response and I will send you your message')

@dp.message()
async def send_echo(message: Message):
    await message.answer(text=message.text)


async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

dp.message.register(send_photo_echo, F.photo)

if __name__ == '__main__':
    dp.run_polling(bot)