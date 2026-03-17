from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile,CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_query_users import orm_add_user
from text.messages import START_TEXT,ABOUT_TEXT,HELP_TEXT
from keyboards.inline_keyboard import start_keyboard,return_menu
from  filter.filter import IsAdmin

router_admin = Router()
router_admin.message.filter(IsAdmin())

@router_admin.message(Command("admin"))
async def admin_command_start(message:Message):
    print(message)
    await message.answer(text="welcome to admin")

