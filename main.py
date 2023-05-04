import os

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv

from keyboards import main_keyboard

load_dotenv()

bot_token = os.getenv("TOKEN")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message) -> None:
    user_name = message.from_user.first_name
    await message.answer(f"Привет, {user_name}!!", reply_markup=main_keyboard())


@dp.message_handler(Text(equals="кошечка"))
async def send_cat(message: types.Message) -> None:
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_url = response.json()[0]["url"]
    await bot.send_photo(message.chat.id, cat_url, caption="на котика", reply_markup=main_keyboard())


@dp.message_handler(Text(equals="собачка"))
async def send_dog(message: types.Message) -> None:
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    dog_url = response.json()[0]["url"]
    await bot.send_photo(message.chat.id, dog_url, caption="на песика", reply_markup=main_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp)