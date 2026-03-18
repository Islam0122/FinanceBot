from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile,CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_query_users import orm_add_user
from text.messages import START_TEXT,ABOUT_TEXT,HELP_TEXT
from keyboards.inline_keyboard import start_keyboard,return_menu
from  filter.filter import IsAdmin
from .parser_functions import get_movies,search_movies
parser_admin = Router()

@parser_admin.message(F.text.startswith("/movies"))
async def admin_command_start(message:Message):
    movie =  ""
    for i in message.text.split()[1:-1]:
        movie += i+" "
    print(movie)
    movies = search_movies(movie)
    for i in movies:
        from aiogram.utils.keyboard import InlineKeyboardBuilder
        from aiogram.types import InlineKeyboardButton


        builder = InlineKeyboardBuilder()
        builder.add(
                InlineKeyboardButton(text="smotret", url=i["url"]),
            )
        await message.answer(text=i['url'],reply_markup=builder.as_markup())