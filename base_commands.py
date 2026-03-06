from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from reply_keyboards import start_keyboard
router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.reply(
        "👋 Добро пожаловать в Finance Bot\n"
        "Этот бот помогает учитывать доходы и расходы.",
        reply_markup=start_keyboard
    )
