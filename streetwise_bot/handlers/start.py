from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from streetwise_bot.services.user import insert_or_ignore_user

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message, session: AsyncSession) -> None:
    if message.from_user:
        await message.answer(f"Hello, {message.from_user.first_name}!")
        await insert_or_ignore_user(
            session,
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
        )
    else:
        await message.answer("Hello!")
