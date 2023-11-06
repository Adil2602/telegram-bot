from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def get_start(message:Message):
    await message.answer(f"Здраствуйте, {message.from_user.first_name}")




