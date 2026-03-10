from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from keyboards.reply_keyboards import cancel_kb,confirm_kb
from aiogram.types import  ReplyKeyboardRemove
from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from .questions import questions

router_test = Router()

class Test(StatesGroup):
    answering = State()


@router_test.message(Command('test'))
async def test(message: Message, state: FSMContext):
    await state.update_data(q_index=0,score=0)
    data = await state.get_data()
    q =questions[data['q_index']]
    k = []
    for  i in q['options']:
        k.append(KeyboardButton(text=i))

    kb = ReplyKeyboardBuilder()
    kb.add(*k)

    await message.answer(text=q['question'], reply_markup=kb.as_markup())
    await state.set_state(Test.answering)

@router_test.message(Test.answering)
async def answering(message: Message, state: FSMContext):
    data = await state.get_data()
    q_index = int(data['q_index'])
    score = int(data['score'])
    q = questions[data['q_index']]
    if message.text.startswith(q['correct']):
        score += 1
    q_index += 1
    if q_index >= len(questions):
        await message.answer(text=str(score),reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    await state.update_data(q_index=q_index,score=score)
    data_new = await state.get_data()
    q1 = questions[data_new['q_index']]
    k = []
    for i in q1['options']:
        k.append(KeyboardButton(text=i))

    kb = ReplyKeyboardBuilder()
    kb.add(*k)

    await message.answer(text=q1['question'], reply_markup=kb.as_markup())

















