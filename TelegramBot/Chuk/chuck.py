import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, Message, CallbackQuery, BotCommand
import requests
from environs import Env

#You should create an .env file in the folder with the chuck.py file and paste this -> BOT_TOKEN=YOUR_TOKEN_TELEGRAM_BOT
env = Env()
env.read_env()
API_TOKEN = env.str('BOT_TOKEN')

# Create object Bot and Dispatcher
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Start Keyboard
kb_builder_start: InlineKeyboardBuilder = InlineKeyboardBuilder()
random_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Random Joke Chuck',
    callback_data='random_button_pressed')
categories_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Categories Joke Chuck',
    callback_data='categories_button_pressed')
kb_builder_start.row(*[random_button, categories_button], width=2)
keyboard_start = kb_builder_start.as_markup()

# Keyboard which category
chuck_joke_categories = requests.get('https://api.chucknorris.io/jokes/categories').json()
kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
buttons: list[InlineKeyboardButton] = [InlineKeyboardButton(text=i, callback_data=i) for i in chuck_joke_categories]
kb_builder.row(*buttons, width=2)
keyboard = kb_builder.as_markup()


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Start bot which will send a joke'),
        BotCommand(command='/help',
                   description='What are doing bot'),
        BotCommand(command='/random',
                   description='Random chuck joke'),
        BotCommand(command='/categories',
                   description='Select a joke category')]
    await bot.set_my_commands(main_menu_commands)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='This is a joke bot from Chuck Norris.\n\nThese are inline buttons. Click on any one!', reply_markup=keyboard_start)


@dp.message(Command(commands=['help']))
async def command_help(message: Message):
    await message.answer(
        "This bot is sending you a chuck norris joke\nYou can choose a random joke or from the categories you like.")


@dp.message(Command(commands=['categories']))
async def random_chuck_joke(message: Message):
    await message.answer(text=f'Select a category for the joke',
                         reply_markup=keyboard)


@dp.message(Command(commands=['random']))
async def random_chuck_joke(message: Message):
    chuck_random_joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
    await message.answer(f'Random Chuck joke\n{chuck_random_joke}')


@dp.callback_query(lambda c: c.data == "random_button_pressed")
async def press_random_button(callback: CallbackQuery):
    chuck_random_joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
    await callback.message.answer(f'Random Chuck joke\n{chuck_random_joke}')
    await callback.answer()


@dp.callback_query(lambda c: c.data == "categories_button_pressed")
async def press_categories_button(callback: CallbackQuery):
    await callback.message.answer(text='Select a category for the joke', reply_markup=keyboard)
    await callback.answer()


@dp.callback_query()
async def press_category(callback: CallbackQuery):
    chuck_joke = requests.get(f'https://api.chucknorris.io/jokes/random?category={callback.data}').json()['value']
    await callback.message.answer(f'joke-category: {callback.data}\n{chuck_joke}')
    await callback.answer()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


