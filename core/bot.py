from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import os

bot = Bot(token=os.environ['BOT_TOKEN'])
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
