import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message  # Тип сообщения

import AI
from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота





# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет! Я твой друг. Можешь кидать мне картинки")  # Отвечаем на полученное сообщение


@dp.message(F.photo)
async def do_answer(message: Message):
    answer = AI.generate_answer()
    if answer:
        await message.answer(answer)


@dp.message(F.text)
async def write(message: Message):
    await message.answer('зачем ты мне пишешь? лучше скинь мем')
@dp.message(text = ("го_в_доту?"))
async def DOTA_2(message: Message):
    await message.answer("Пошли Брат")

async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')