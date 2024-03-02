from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message) -> None:
    if message.from_user:
        await message.answer(f"Hello, {message.from_user.first_name}!")
    else:
        await message.answer("Hello!")
