import logging
from aiogram import Bot, Dispatcher, types, executor
from vars import tg_token, water_names
from scrap import search_post, lastposts

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tg_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Последние 10 постов', callback_data='last10'))
    for key in water_names.keys():
        keyboard.add(types.InlineKeyboardButton(text=f'{key}', callback_data=f'{key}'))
    await message.answer('Выберите водоем', reply_markup=keyboard)


@dp.callback_query_handler()
async def send_random_value(call: types.CallbackQuery):
    if call.data == 'last10':
        msgs = lastposts()
        for val in reversed(msgs):
            await call.message.answer(val)
    elif call.data in water_names.keys():
        key = water_names.get(call.data)
        msgs = search_post(key)
        for val in reversed(msgs):
            await call.message.answer(val)
    else:
        await call.message.answer("Error!!!")


@dp.message_handler(commands=['last10'])
async def last10(message: types.Message):
    msgs = lastposts()
    for val in reversed(msgs):
        await message.answer(val)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
