import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
import os
import dotenv
dotenv.load_dotenv()
# Instead of BOT TOKEN HERE, you need to insert your bot token,
# received from @BotFather
BOT_TOKEN: str = os.getenv('BOT_TOKEN')

# Create object bot and dispatcher
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Number of attempts available to the user in the game
ATTEMPTS: int = 5

# Dictionary that will store users data
users: dict = {}


# A function that returns a random integer from 1 to 100
def get_random_number() -> int:
    return random.randint(1, 100)


# This handler will fire on the "/start" command
@dp.message(Command(commands=['start']))
async def procesor_start_command(message: Message):
    await message.answer('Hay\nLets go play the game "Guess the number!!"')
    # If the users just launched the bot and it is not in the dictionary userss - add it to the dictionary
    if message.from_user.id not in users:
        users[message.from_user.id] ={'in_game': False,
                                       'secret_number': None,
                                       'attempts': None,
                                       'total_games': 0,
                                       'wins': 0}


# This handler will fire on the "/help" command
@dp.message(Command(commands=['help']))
async def procesor_help_command(message: Message):
    await message.answer(f'Game rules:\n\nI guess a number from 1 to 100, '
                          f'and you need to guess it\nYou have {ATTEMPTS} '
                          f'attempts\n\nCommands available:\n/help - rules '
                          f'games and list of commands\n/cancel - quit the game\n'
                          f'/stat - view statistics\n\nLet\'s play a game?')


# This handler will fire on the "/stat" command
@dp.message(Command(commands=['stat']))
async def procesor_stat_command(message: Message):
    await message.answer(f'Total game play: {users[message.from_user.id]["total_games"]}\n'
                         f'Play win: {users[message.from_user.id]["wins"]}')


# This handler will fire on the "/cancel" command
@dp.message(Command(commands=['cancel']))
async def procesor_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer(f'You exit game. If you want to play game again, write to me again')
        users[message.from_user.id]['in_game'] = False
    else:
        await message.answer(f'And we are not playing with you anyway. Maybe let\'s play once?')


# This handler will fire on the users's consent to play the game

@dp.message(Text(text=['Yes', 'Yep', 'Y', 'Play', 'Want play'], ignore_case=True))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Hurrah!\n\nI guessed a number from 1 to 100, try to guess!')
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = ATTEMPTS
    else:
        await message.answer(
            'While we are playing the game, I can only respond to numbers from 1 to 100 with /cancel and /stat commands')


# This handler will trigger when the users refuses to play the game
@dp.message(Text(text=['No', 'Not', 'Won\'t play'], ignore_case=True))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Sorry :( If you want to play - just write about it')
    else:
        await message.answer(
            'We are playing with you right now. Please send numbers from 1 to 100')


# This handler will fire when the users sends numbers from 1 to 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def processor_numbers_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            await message.answer('Wohoooooooooo!!!! You guessed the number! Can we play some more?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            await message.answer('My number is less')
            users[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            await message.answer('My number is more')
            users[message.from_user.id]['attempts'] -= 1

        if users[message.from_user.id]['attempts'] == 0:
            await message.answer(
                f'Sorry, you have no more attempts left. You lost :(. My number was {users[message.from_user.id]["secret_number"]}')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
    else:
        await message.answer('We are not playing yet. You want to play?')


# This handler will work on any other messages
@dp.message()
async def procesor_other_answers(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer("We're playing with you now. Please send numbers from 1 to 100")
    else:
        await message.answer("I'm a pretty limited bot, let's just play a game?")


if __name__ == '__main__':
    dp.run_polling(bot)
