from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.utils import executor

bot = Bot(token='5421165424:AAGqJ8qtmaRap3kpLr0KpJl7jAiTU-SZjRQ')

dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message : types.Message):

    chat_id = message.chat.id
    text = f'Hello, {message.from_user.full_name}'

    await bot.send_message(chat_id=chat_id, text=text)



executor.start_polling(dp)
