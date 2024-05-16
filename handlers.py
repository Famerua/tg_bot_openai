from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello! I will help u to know ur ID. Seng me any message")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Your ID is {msg.from_user.id}")
