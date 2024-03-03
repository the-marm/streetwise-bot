import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from streetwise_bot import config
from streetwise_bot.handlers import routers_list
from streetwise_bot.middlewares import DbSessionMiddleware

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def main() -> None:
    engine = create_async_engine(url=config.DB_URL, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    dp.update.middleware(DbSessionMiddleware(sessionmaker))

    dp.include_routers(*routers_list)

    await dp.start_polling(bot)


try:
    asyncio.run(main())
except Exception:
    import traceback

    logger.warning(traceback.format_exc())
