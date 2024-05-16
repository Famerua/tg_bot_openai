import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.utils.chat_action import ChatActionMiddleware

import config
from handlers import router

# fmt: off
async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML) #разметка HTML, чтобы избежать проблем с экранированием символов
    dp = Dispatcher(storage=MemoryStorage()) #данные не сохраненные в бд будут стерты при перезапуске
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True) #удаляет все апдейты после последнего заверщения бота
    
    dp.message.middleware(ChatActionMiddleware()) #подключаем мидлвар для отправки состояний бота пользователям

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
