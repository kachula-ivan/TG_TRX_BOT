import asyncio

import logging

import config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.http.client.commands import start
from database.app import db
from database.migrations import user


TOKEN = config.TOKEN

DB_URL = f'postgresql://{config.PG_USER}:{config.PG_PASSWORD}@{config.PG_HOST}/{config.PG_DATABASE}'

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def on_startup():
    await db.set_bind(DB_URL)
    await db.gino.create_all()
    print('PostgreSQL START')
    print('Bot ONLINE')


async def on_shutdown():
    await db.pop_bind().close()


async def main() -> None:
    try:
        dp.include_routers(start.router)

        dp.startup.register(on_startup)

        await dp.start_polling(bot)

    except KeyboardInterrupt:
        logging.info("Bot has been stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Goodbye!')
        pass
