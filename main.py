from aiogram import Bot, Dispatcher, types, executor
import os

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот Expert Автозапчасти. Напиши, что нужно подобрать.")

if __name__ == '__main__':
    executor.start_polling(dp)
