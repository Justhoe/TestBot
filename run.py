import asyncio

from aiogram import Bot, Dispatcher
from aiogram import CommandStart
from aiogram import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
