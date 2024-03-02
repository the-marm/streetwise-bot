import asyncio
import logging

from aiogram import Bot, Dispatcher

from streetwise_bot import config
from streetwise_bot.handlers import routers_list

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(*routers_list)

    await dp.start_polling(bot)


try:
    asyncio.run(main())
except Exception:
    import traceback
    logger.warning(traceback.format_exc())
