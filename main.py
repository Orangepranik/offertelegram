import ctypes
import types

from libs.libslist import *
from database.basesqlite3 import *
from keyboards.keyboardd import *

API_TOKEN = '5065205436:AAFI7w3-1X53PzJs5WSIUbLfyfO8afThK98'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class News(StatesGroup):
    first_new = State()

class Mail(StatesGroup):
    message_for_mail = State()

admin_id = str(450720486)
admin_id_1 = str(1609004037)
@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer('Здравствуйте !\nМы всегда рады контенту от наших подписчиков.\nПрисылай свою историю/новость с описанием ,а так же фото/видео  и мы вскоре опубликуем её.', reply_markup=add_newss())
    id_user = message.from_user.id
    name_user = message.from_user.username
    check_user_id = cur.execute("SELECT id FROM users WHERE id=?", (message.from_user.id, )).fetchone()
    if check_user_id is None:
        cur.execute("INSERT INTO users(id,name) VALUES(?,?)", (id_user, name_user,))
    else:
        pass
    base.commit()


@dp.message_handler(text='Предложить новость')
async def firt_step(message: types.Message):
    await message.answer('Перешлите новость\nДля отмены действия введите /cancel')
    await News.first_new.set()


@dp.message_handler(state=News.first_new, content_types=["any"])
async def send_new(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.content_type == 'photo':
            data['photo'] = message.photo
            print(data['photo'][-1]['file_id'])
            if message.caption is None:
                await bot.send_photo(chat_id=admin_id, photo=data['photo'][-1]['file_id'])
                await bot.send_photo(chat_id=admin_id_1, photo=data['photo'][-1]['file_id'])
                await bot.send_photo(chat_id=message.from_user.id, photo=data['photo'][-1]['file_id'])
            else:
                data['photo_caption'] = message.caption
                await bot.send_photo(chat_id=admin_id, photo=data['photo'][-1]['file_id'], caption=data['photo_caption'])
                await bot.send_video(chat_id=message.from_user.id, video=data['video'][-1]['file_id'], caption=data['photo_caption'])
                await bot.send_photo(chat_id=admin_id_1, photo=data['photo'][-1]['file_id'], caption=data['photo_caption'])
            await message.answer("Спасибо!\n Вашу новость/историю рассмотрит администратор и если она подходит под тематику - жди её на канале ! ", reply_markup=add_newss())
        if message.content_type == 'document':
            data['document'] = message.document.file_id
            if message.caption is None:
                await bot.send_document(chat_id=admin_id, document=data['document'])
                await bot.send_document(chat_id=admin_id_1, document=data['document'])
                await bot.send_document(chat_id=message.from_user.id, document=data['document'])
            else:
                data['document_caption'] = message.caption
                await bot.send_document(chat_id=admin_id, document=data['document'], caption=data['document_caption'])
                await bot.send_document(chat_id=admin_id_1, document=data['document'], caption=data['document_caption'])
                await bot.send_document(chat_id=message.from_user.id, document=data['document'], caption=data['document_caption'])
            await message.answer("Спасибо!\n Вашу новость/историю рассмотрит администратор и если она подходит под тематику - жди её на канале ! ", reply_markup=add_newss())
        if message.content_type == 'animation':
            data['animation'] = message.animation.file_id
            if message.caption is None:
                await bot.send_animation(chat_id=admin_id, animation=data['animation'])
                await bot.send_animation(chat_id=admin_id_1, animation=data['animation'])
                await bot.send_animation(chat_id=message.from_user.id, animation=data['animation'])
            else:
                data['animation_caption'] = message.caption
                await bot.send_animation(chat_id=admin_id, animation=data['animation'], caption=data['animation_caption'])
                await bot.send_animation(chat_id=admin_id_1, animation=data['animation'], caption=data['animation_caption'])
                await bot.send_animation(chat_id=message.from_user.id, animation=data['animation'], caption=data['animation_caption'])
            await message.answer("Спасибо!\n Вашу новость/историю рассмотрит администратор и если она подходит под тематику - жди её на канале ! ", reply_markup=add_newss())
        if message.content_type == 'video':
            data['video'] = message.video.file_id
            if message.caption is None:
                await bot.send_video(chat_id=admin_id, video=data['video'])
                await bot.send_video(chat_id=admin_id_1, video=data['video'])
                await bot.send_video(chat_id=message.from_user.id, video=data['video'])
            else:
                data['video_caption'] = message.caption
                await bot.send_video(chat_id=admin_id, video=data['video'], caption=data['video_caption'])
                await bot.send_video(chat_id=admin_id_1, video=data['video'], caption=data['video_caption'])
                await bot.send_video(chat_id=message.from_user.id, video=data['video'], caption=data['video_caption'])
            await message.answer("Спасибо!\n Вашу новость/историю рассмотрит администратор и если она подходит под тематику - жди её на канале ! ", reply_markup=add_newss())
        if message.content_type == 'audio':
            await message.answer('Аудио не принимаются')
            await state.finish()
        if message.content_type == 'voice':
            data['voice'] = message.voice.file_id
            if message.caption is None:
                await bot.send_audio(chat_id=admin_id, audio=data['voice'])
                await bot.send_audio(chat_id=admin_id_1, audio=data['voice'])
                await bot.send_audio(chat_id=message.from_user.id, audio=data['voice'])
            else:
                data['voice_caption'] = message.caption
                await bot.send_audio(chat_id=admin_id, audio=data['voice'], caption=data['voice_caption'])
                await bot.send_audio(chat_id=admin_id_1, audio=data['voice'], caption=data['voice_caption'])
                await bot.send_audio(chat_id=message.from_user.id, audio=data['voice'], caption=data['voice_caption'])
            await message.answer("Спасибо!\n Вашу новость/историю рассмотрит администратор и если она подходит под тематику - жди её на канале ! ", reply_markup=add_newss())
        if message.content_type == 'text':
            data['text'] = message.text
            await bot.send_message(chat_id=admin_id, text=f"{data['text']}\nНовость предложил:{message.from_user.id}\n@{message.from_user.username}")
            await bot.send_message(chat_id=admin_id_1, text=f"{data['text']}\nНовость предложил:{message.from_user.id}\n@{message.from_user.username}")
            await bot.send_message(chat_id=message.from_user.id, text=f"{data['text']}\nНовость предложил:{message.from_user.id}\n@{message.from_user.username}")
            await message.answer("Спасибо!\n Вашу новость/историю рассмотрит администратор и если она подходит под тематику - жди её на канале ! ", reply_markup=add_newss())
        data["check"] = message
        # print(message.get("mime_type"))
        await message.answer("Ваша новость скинута админу", reply_markup=add_newss())
        # await bot.send_message(chat_id=admin_id, text=f'{data["first_new"]},\nНовость предложил:{message.from_user.id}\n@{message.from_user.username}')
        # await message.answer(data["first_new"])

        # print(data["first_new"])
        await state.finish()


@dp.message_handler(commands='sendmail')
async def start_mailing(message: types.Message):
    await Mail.message_for_mail.set()
    await message.answer('Перешлите сообщение которое хочете разослать пользователям бота')


@dp.message_handler(state=Mail.message_for_mail, content_types=["text", "sticker", "pinned_message", "photo", "audio"])
async def sending_mail(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["""message_for_mail"""] = message
        select_users = cur.execute('SELECT id FROM users WHERE name==name').fetchall()
        stat = {
            'valid': 0,
            'invalid': 0
        }
        for users in select_users:
            if users in admin_id:
                pass
            else:
                try:
                    await bot.send_message(text=data["""message_for_mail"""], chat_id=users[0])
                    stat['valid'] += 1
                except:
                    stat['invalid'] += 1
        await message.answer(f"Удачно отослано стольки пользователям: {stat['valid']}\nНе получилось отослать такому количеству пользователей: {stat['invalid']}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
