from string import punctuation
from aiogram import F, types, Router, Bot
from aiogram.filters import CommandStart, Command, or_f
from sqlalchemy.ext.asyncio import AsyncSession
from filter.filter import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


restricted_words = {
    'дурак', 'идиот', 'глупец', 'тупой', 'кретин', 'мразь', 'сволочь', 'урод',
    'дебил', 'придурок', 'засранец', 'тварь', 'скотина', 'гнида', 'сука',
    'падла', 'ублюдок', 'шлюха', 'проститутка', 'блядь', 'хрен', 'чмо',
    'козёл', 'баран', 'осёл', 'мерзавец', 'жопа', 'пизда', 'мудак', 'лох',
    'гандон', 'пидор', 'гей', 'тупица', 'недоумок', 'говно', 'задница',
    'петух', 'курва', 'шваль', 'хренов', 'шалава', 'говнюк', 'козлина'
}

@user_group_router.message()
async def group_command(message: types.Message,bot:Bot):
    if message.text.lower() in restricted_words:
        await bot.send_message(bot.my_admins_list[0],f"{message.from_user.first_name} used restricted words ")
