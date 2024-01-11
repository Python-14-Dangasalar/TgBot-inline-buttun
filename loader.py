from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp
from reply_button import start_btn
from inline_button import top_music, like_dislike


@dp.message_handler(commands=['start', 'help'])
async def start(message: Message):
    image = open('images/start.png', 'rb')
    text = (f"Assalomu-alaykum {message.from_user.full_name}👋\n"
            f"Music botga Xush kelibsiz. Kerakli bo'limni tanlang👇")
    await message.answer_photo(image, caption=text, reply_markup=start_btn)


@dp.message_handler(text='Hamdam')
async def top50(message: Message):
    print(message.text)
    text = f'1. Janze\n2. Maktabimda\n3. Odamlar nima deydi\n4. Yetmasmidi\n5. Qizil Ko\'ylak'
    await message.answer(text, reply_markup=top_music)


@dp.callback_query_handler()
async def callback_query(call: CallbackQuery):
    print(call.data)
    if call.data == 'janze':
        await call.message.answer_audio(open('Hamdam-Janze.mp3', 'rb'), reply_markup=like_dislike)
        await call.answer(cache_time=10)
    elif call.data == 'maktab':
        await call.message.answer_audio(open('maktabimda.mp3', 'rb'))
        await call.answer(cache_time=10)


@dp.callback_query_handler()
async def callback_query_2(call: CallbackQuery):
    if call.data == 'dislike':
        await call.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
