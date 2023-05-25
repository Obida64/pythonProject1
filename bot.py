import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as cfg
import product as pr
from bd import db_start, create_profile
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from config import users, admin
logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    await db_start()

load_dotenv()
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot=bot)


#функция проверки подписки
async def check_sub_channel(channels, user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if await check_sub_channel(cfg.CHANNELS, message.from_user.id):
        await bot.send_photo(message.from_user.id, photo='https://imgur.com/1Xrf6EO', caption="С помощью данного бота можешь найти интересующие тебя плагины(гайды)\nВыбери что тебя интересует", reply_markup=nav.profileKeyboard)
    else:
        await bot.send_photo(message.from_user.id, photo="https://cpab.ru/wp-content/uploads/2021/10/win11_lock_hero_2-1024x575.jpg", caption=cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

    await create_profile(user_id=message.from_user.id)

@dp.message_handler(Command('sendall'))
async def send_all(message: Message):
    if message.chat.id == admin:
        await message.answer('Start')
        for i in users:
            await bot.send_message(i, message.text[message.text.find(' '):])
        await message.answer('Done')
    else:
        await message.answer('Error')

@dp.message_handler(Command('sendphoto'))
async def send_all(message: Message):
    if message.chat.id == admin:
        await message.answer('Start')
        for i in users:
            await bot.send_photo(i, open('2023-05-25 23.07.10.jpg', 'rb'), message.text[message.text.find(' '):])
        await message.answer('Done')
    else:
        await message.answer('Error')

@dp.message_handler()
async def find_vst(message: types.Message):
    if await check_sub_channel(cfg.CHANNELS, message.from_user.id):
        if message.text == 'VST Plugin':
            await bot.send_photo(message.from_user.id, photo="https://imgur.com/QtWNmSA", caption="Выбери свою ОС:", reply_markup=nav.profileKeyboardVST)
        if message.text == 'MacOS':
            await bot.send_photo(message.from_user.id, photo="https://imgur.com/MOvMlMC",
                                 caption="Доступные VST для MacOS\nСписок постоянно пополняется\nКликай на название откроется описание\nИщешь определенный плагин?\nнапиши в личку @tsmaksim",
                                 reply_markup=nav.inlineKB_vstMac)
        if message.text == 'WIN':
            await bot.send_photo(message.from_user.id, photo="https://imgur.com/GAAoMap",
                                 caption="Доступные VST для Windows\nСписок постоянно пополняется\nКликай на название откроется описание\nИщешь определенный плагин?\nнапиши в личку @tsmaksim",
                                 reply_markup=nav.inlineKB_vstWin)
        if message.text == 'Семплы':
            await bot.send_photo(message.from_user.id, photo="https://imgur.com/J6FHeTI", caption="Доступные Семплы\nСписок постоянно пополняется(в разработке)")
        if message.text == 'DAW':
            await bot.send_photo(message.from_user.id, photo="https://imgur.com/GXetGbU", caption="Доступные DAW\nСписок постоянно пополняется\nКликай на название откроется описание\nИщешь определенный DAW?\nнапиши в личку @tsmaksim", reply_markup=nav.inlineKB_DAW)
        if message.text == 'Гайды':
            await bot.send_photo(message.from_user.id, photo="https://imgur.com/mnB2x7E", caption="Некоторые гайды\nСписок постоянно пополняется(в разработке)")
        if message.text == 'Назад':
            await bot.send_message(message.from_user.id, 'Ты вернулся на главную', reply_markup=nav.profileKeyboard)

    else:
        await bot.send_photo(message.from_user.id, photo="https://cpab.ru/wp-content/uploads/2021/10/win11_lock_hero_2-1024x575.jpg", caption=cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())


@dp.callback_query_handler(text= "subchanneldone")
async def subchanneldone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if await check_sub_channel(cfg.CHANNELS, message.from_user.id):
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEI9KVkXhwiH9tagtPeKZa7NE606BiL5AACRTMAAgSm8ErwTFqYp2gMNS8E')
        await bot.send_message(message.from_user.id, "Ты подписался на все каналы!\nПриятного использования!", reply_markup=nav.profileKeyboard)
    else:
        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE1, reply_markup=nav.showChannels())


@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'artsync':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/MQUWC2R', caption=pr.artsync, reply_markup=nav.inLineLinkArts)
    if callback_query.data == 'artsyncv':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/7koVqLF', caption=pr.artsyncv, reply_markup=nav.inLineLinkArtsV)
    if callback_query.data == 'mongoose':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/d7L3Pet', caption=pr.mongoose, reply_markup=nav.inLineLinkMongoose)
    if callback_query.data == 'tbone':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/3CDVEPN',
                             caption=pr.tbone, reply_markup=nav.inLineLinkTbone)
    if callback_query.data == 'sublab':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/cR8rkrO',
                             caption=pr.sublab, reply_markup=nav.inLineLinkSublab)
    if callback_query.data == 'lindellaudiote100':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/r0YI6Yz',
                             caption=pr.lindellaudiote100, reply_markup=nav.inLineLinkTE100)
    if callback_query.data == 'LANDRFXSuite':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/bjbfjmG',
                             caption=pr.LANDRFXSuite, reply_markup=nav.inLineLinkLANDRFXSuite)
    if callback_query.data == 'XferRecordsSerum':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/u1EnlL9',
                             caption=pr.XferRecordsSerum, reply_markup=nav.inLineLinkSerum)
    if callback_query.data == 'SurrealMachinesImpact':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/jmLK8ij',
                             caption=pr.SurrealMachinesImpact, reply_markup=nav.inLineLinkSurrealImpact)
    if callback_query.data == 'DubMachines':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/Dtii4zw',
                             caption=pr.DubMachines, reply_markup=nav.inLineLinkDubMachines)
    if callback_query.data == 'PitchFluidBundle':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/hkM1TKv',
                             caption=pr.PitchFluidBundle, reply_markup=nav.inLineLinkPitchFluidBundle)
    if callback_query.data == 'PulsarAllPlugIns':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/sk7xx5c',
                             caption=pr.PulsarAllPlugIns, reply_markup=nav.inLineLinkPulsarAllPlugIns)
    if callback_query.data == 'Unique':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/dRYJfLm',
                             caption=pr.Unique, reply_markup=nav.inLineLinkUnique)
    if callback_query.data == 'Nektarine':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/ObMlJ3j',
                             caption=pr.Nektarine, reply_markup=nav.inLineLinkNektarine)
    if callback_query.data == 'InitialReverse':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/JsCNTzj',
                             caption=pr.InitialReverse, reply_markup=nav.inLineLinkInitialReverse)
    if callback_query.data == 'TracktionNovum':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/qfx7jmP',
                             caption=pr.TracktionNovum, reply_markup=nav.inLineLinkTracktionNovum)
    if callback_query.data == 'XferLFOTool':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/SzzaZXv',
                             caption=pr.XferLFOTool, reply_markup=nav.inLineLinkXferLFOTool)
    if callback_query.data == 'Factory':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/cS554EF',
                             caption=pr.Factory, reply_markup=nav.inLineLinkFactory)
    if callback_query.data == 'Retrologue':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/8hh2e0S',
                             caption=pr.Retrologue, reply_markup=nav.inLineLinkRetrologue)
    if callback_query.data == 'ANA2':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/PRwK2Eh',
                             caption=pr.ANA2, reply_markup=nav.inLineLinkANA2)
    if callback_query.data == 'FASTBalancer':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/YE36d0l',
                             caption=pr.FASTBalancer, reply_markup=nav.inLineLinkFASTBalancer)
    if callback_query.data == 'Scaler2':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/BBrlKyx',
                             caption=pr.Scaler2, reply_markup=nav.inLineLinkScaler2)
    if callback_query.data == 'Kick2':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/XIwZTaw',
                             caption=pr.Kick2, reply_markup=nav.inLineLinkKick2)
    if callback_query.data == 'SubBassDoctor808':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/FMCLhNr',
                             caption=pr.SubBassDoctor808, reply_markup=nav.inLineLinkSubBassDoctor808)
    if callback_query.data == 'ReplikaXT':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/o30uy7Y',
                             caption=pr.ReplikaXT, reply_markup=nav.inLineLinkReplikaXT)
    if callback_query.data == 'MassiveX':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/KeGsH54',
                             caption=pr.MassiveX, reply_markup=nav.inLineLinkMassiveX)
    if callback_query.data == 'FabFilterBundle':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/iUkf53I',
                             caption=pr.FabFilterBundle, reply_markup=nav.inLineLinkFabFilterBundle)
    if callback_query.data == 'ArturiaPigments':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/XvuMnOd',
                             caption=pr.ArturiaPigments, reply_markup=nav.inLineLinkArturiaPigments)
    if callback_query.data == 'AnaloglabV':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/oqYkbPb',
                             caption=pr.AnaloglabV, reply_markup=nav.inLineLinkAnaloglabV)
    if callback_query.data == 'AutoTuneVocalEQ':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/yKEqfrT',
                             caption=pr.AutoTuneVocalEQ, reply_markup=nav.inLineLinkAutoTuneVocalEQ)
    if callback_query.data == 'VocalCompressor':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/RCX669S',
                             caption=pr.VocalCompressor, reply_markup=nav.inLineLinkAutoTuneVocalEQ)
    if callback_query.data == 'flstudio':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/AYFI4xu',
                             caption=pr.flstudio, reply_markup=nav.inlineKB_DAW)
    if callback_query.data == 'cubase12':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/w4CYaPi',
                             caption=pr.cubase12, reply_markup=nav.inLineLinkCubase12)
    if callback_query.data == 'AbletonLive11':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/rrQyMrG',
                             caption=pr.AbletonLive11, reply_markup=nav.inLineLinkAbletonLive11)
    if callback_query.data == 'LogicPro':
        await bot.send_photo(chat_id=callback_query.from_user.id, photo='https://imgur.com/OVTNxBh',
                             caption=pr.LogicPro, reply_markup=nav.inLineLinkLogicPro)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)