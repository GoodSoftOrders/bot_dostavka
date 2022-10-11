from pyexpat.errors import messages
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)

import keyboards as kb
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def main_menu(message: types.Message):
    await message.reply("Привет! Выбери нужную кнопку:", reply_markup=kb.main_menu)

@dp.message_handler(text="Вернуться в главное меню")
async def back_menu(message: types.Message):
    await message.reply("Привет! Выбери нужную кнопку:", reply_markup=kb.main_menu)

@dp.message_handler(text="Меню")
async def menu(message: Message):
    await message.reply("Выбери категорию еды", reply_markup=kb.menu_kb)

@dp.message_handler(commands=['admin'])
async def admin_menu(message: types.Message):
    await message.reply("Приветствую, владыка всея кухни!", reply_markup=kb.admin_kb)

async def on_startup(_):
    print('Бот Вышел в Онлайн')

if __name__ == '__main__':
    executor.start_polling(dp)