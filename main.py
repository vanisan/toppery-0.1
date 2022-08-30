from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='5421165424:AAGqJ8qtmaRap3kpLr0KpJl7jAiTU-SZjRQ')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(reply_markup=kb.greet_kb)

    button_hi = KeyboardButton('Привет! 👋')

    greet_kb = ReplyKeyboardMarkup()
    greet_kb.add(button_hi)



executor.start_polling(dp)
