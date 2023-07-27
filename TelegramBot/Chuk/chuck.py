from aiogram import Bot, Dispatcher
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
import requests

chuck_joke_categories = requests.get('https://api.chucknorris.io/jokes/categories').json()



# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6303185352:AAECZ7vk1ZS60d4d02HpT3G6arOvqPa3iUU'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
buttons: list[InlineKeyboardButton] = [InlineKeyboardButton(text=i,callback_data=i) for i in chuck_joke_categories]
buttons[0] = InlineKeyboardButton(text='random', callback_data='random')
kb_builder.row(*buttons, width=2)
keyboard = kb_builder.as_markup()

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки. Нажми на любую!',
                         reply_markup=keyboard)

@dp.callback_query(Text(text=['random']))
async def random_chuck_joke(callback: CallbackQuery):
    chuck_random_joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
    await callback.message.answer(f'Random Chuck joke\n{chuck_random_joke}')
    await callback.answer()


@dp.callback_query()
async def press_category(callback: CallbackQuery):
    chuck_joke = requests.get(f'https://api.chucknorris.io/jokes/random?category={callback.data}').json()['value']
    await callback.message.answer(f'joke-category: {callback.data}\n{chuck_joke}')
    await callback.answer()

if __name__ == '__main__':
    dp.run_polling(bot)