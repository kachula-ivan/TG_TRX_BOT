import asyncio

import logging
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.http.client.commands import start

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


async def main() -> None:
    try:
        bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

        dp.include_routers(start.router)

        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logging.info("Bot has been stopped")


if __name__ == "__main__":
    print('Bot ONLINE')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Goodbye!')
        pass
