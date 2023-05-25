from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNELS
from aiogram.dispatcher.filters import Text

profileKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
profileKeyboard.add('VST Plugin', 'Семплы')
profileKeyboard.add('DAW', 'Гайды')

profileKeyboardVST = ReplyKeyboardMarkup(resize_keyboard=True)
profileKeyboardVST.add('MacOS', 'WIN')
profileKeyboardVST.add('Назад')


def showChannels():
    keyboard = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keyboard.insert(btn)
    btnDoneSubs = InlineKeyboardButton(text="Проверить✅", callback_data="subchanneldone")
    keyboard.insert(btnDoneSubs)
    return keyboard

#кнопки плагинов
#vst
inlineKB_vstMac = InlineKeyboardMarkup(row_width=2)
inlineKB_vstMac.add(InlineKeyboardButton("Arturia Synthi V(Mac)", callback_data='artsyncv'),
                 InlineKeyboardButton("Arturia Synclavier V(Mac)", callback_data='artsync'),
                 InlineKeyboardButton("Mongoose(Mac)", callback_data='mongoose'),
                 InlineKeyboardButton("T-Bone(Mac)", callback_data='tbone'),
                 InlineKeyboardButton("FAW SubLab(Mac)", callback_data='sublab'),
                 InlineKeyboardButton("Lindell TE-100(Mac)", callback_data='lindellaudiote100'),
                 InlineKeyboardButton("LANDR FX Suite(Mac)", callback_data='LANDRFXSuite'),
                 InlineKeyboardButton("Xfer Serum(Mac)", callback_data='XferRecordsSerum'),
                 InlineKeyboardButton("Surreal Impact(Mac)", callback_data='SurrealMachinesImpact'),
                 InlineKeyboardButton("Dub Machines(Mac)", callback_data='DubMachines'),
                 InlineKeyboardButton("Pitch Fluid Bundle(Mac)", callback_data='PitchFluidBundle'),
                 InlineKeyboardButton("Pulsar All Plug-Ins(Mac)", callback_data='PulsarAllPlugIns'),
                 InlineKeyboardButton("Unique(Mac)", callback_data='Unique'),
                 InlineKeyboardButton("Nektarine(Mac)", callback_data='Nektarine'),
                 InlineKeyboardButton("Initial Reverse(Mac)", callback_data='InitialReverse'),
                 InlineKeyboardButton("Tracktion Novum(Mac)", callback_data='TracktionNovum'),
                 InlineKeyboardButton("Xfer LFOTool(Mac)", callback_data='XferLFOTool'),
                 InlineKeyboardButton("Factory(Mac)", callback_data='Factory'),
                 InlineKeyboardButton("Retrologue(Mac)", callback_data='Retrologue'),
                 InlineKeyboardButton("ANA 2(Mac)", callback_data='ANA2'),
                 InlineKeyboardButton("FAST Balancer(Mac)", callback_data='FASTBalancer'),
                 InlineKeyboardButton("Scaler 2(Mac)", callback_data='Scaler2'),
                 InlineKeyboardButton("Kick 2(Mac)", callback_data='Kick2'),
                 InlineKeyboardButton("SubBassDoctor808(Mac)", callback_data='SubBassDoctor808'),
                 InlineKeyboardButton("Replika XT(Mac)", callback_data='ReplikaXT'),
                 InlineKeyboardButton("Massive X(Mac)", callback_data='MassiveX'),
                 InlineKeyboardButton("FabFilter Bundle(Mac)", callback_data='FabFilterBundle'),
                 InlineKeyboardButton("Arturia Pigments(Mac)", callback_data='ArturiaPigments'),
                 InlineKeyboardButton("Analog lab V(Mac)", callback_data='AnaloglabV'),
                 InlineKeyboardButton("Auto-Tune Vocal EQ(Mac)", callback_data='AutoTuneVocalEQ'),
                 InlineKeyboardButton("Vocal Compressor(Mac)", callback_data='VocalCompressor'))

inlineKB_vstWin = InlineKeyboardMarkup(row_width=2)
inlineKB_vstWin.add(InlineKeyboardButton("В разработке", url='https://www.youtube.com/@not_friendly'))


#daw
inlineKB_DAW = InlineKeyboardMarkup(row_width=2)
inlineKB_DAW.add(InlineKeyboardButton("FL Studio 20(Mac)", callback_data='flstudio'),
                 InlineKeyboardButton("Cubase Pro 12(Mac)", callback_data='cubase12'),
                 InlineKeyboardButton("Ableton Live 11(Mac)", callback_data='AbletonLive11'),
                 InlineKeyboardButton("Logic Pro(Mac)", callback_data='LogicPro'))

#ссылки на плагины


inLineLinkArtsV = InlineKeyboardMarkup(row_width=2)
inLineLinkArtsV.add(InlineKeyboardButton("Скачать плагин", url="https://files.sberdisk.ru/s/0V6reI4F9pdEg2I"))

inLineLinkArts = InlineKeyboardMarkup(row_width=2)
inLineLinkArts.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/2kaYRaH005puBh_2DohmQxBhPcz6K6KYpDgK6A9-N8XSLszxxeU"))

inLineLinkMongoose = InlineKeyboardMarkup(row_width=2)
inLineLinkMongoose.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/ym5bYOVvMGUni0ARRELTWdIHJbda-y8qsnFYKj_cf6AH_kIMWyA"))

inLineLinkTbone = InlineKeyboardMarkup(row_width=2)
inLineLinkTbone.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/gyOxCYjj1K7VYV8ZHb5nP8IlK5n3KqsUPKQVthdimZhLlaergUs"))

inLineLinkSublab = InlineKeyboardMarkup(row_width=2)
inLineLinkSublab.add(InlineKeyboardButton("Скачать плагин", url="https://files.sberdisk.ru/s/XUXRzI0lQQOsysN"))

inLineLinkTE100 = InlineKeyboardMarkup(row_width=2)
inLineLinkTE100.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/qcMkyjZE2KLBxb7LMsx3_QR7V39bZunh9Iiepa4Gx7vAV58HNc0"))

inLineLinkLANDRFXSuite = InlineKeyboardMarkup(row_width=2)
inLineLinkLANDRFXSuite.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/dSLyiDt6FZOdLNMlfrYUK_xPVuulXgLhHNudZ-M2rNRQg1bWHbM"))

inLineLinkSerum = InlineKeyboardMarkup(row_width=2)
inLineLinkSerum.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/Eez-1sbAwgoaXBoSN62RCXQW6cOeH0_J3vxWI0Ug26VeeupnN-Y"))

inLineLinkSurrealImpact = InlineKeyboardMarkup(row_width=2)
inLineLinkSurrealImpact.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/rLWcmbMj1MVSruD-t3m4IhVtniqsyK4ijxR0o3ffzTOodSyrXqw"))

inLineLinkDubMachines = InlineKeyboardMarkup(row_width=2)
inLineLinkDubMachines.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/JiZiz1-3TCjRnnNAEuydOujprCsykKEeV-kIxQQjj7dSURtuevI"))

inLineLinkPitchFluidBundle = InlineKeyboardMarkup(row_width=2)
inLineLinkPitchFluidBundle.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/yZqw6hN14qChkayV8HoJasKncn99ofifejhHkGy53diyFzqNuqM"))

inLineLinkPulsarAllPlugIns = InlineKeyboardMarkup(row_width=2)
inLineLinkPulsarAllPlugIns.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/IKwCWJAo79IDB9CNDPtVf7u6e4zfhq_UB-enT2mkwxGuMFdlX0M"))

inLineLinkUnique = InlineKeyboardMarkup(row_width=2)
inLineLinkUnique.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/RQ6T5Wn9bmF_ryofj0o99OaLECREdGnq5yZcrdUPto3n7ryYLF4"))

inLineLinkNektarine = InlineKeyboardMarkup(row_width=2)
inLineLinkNektarine.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/qZvXPF3oIhPP1hLiRTBaQkJpY_MsRtrtrL1GsE4TDsNqbwOyDfM"))

inLineLinkInitialReverse = InlineKeyboardMarkup(row_width=2)
inLineLinkInitialReverse.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/2F1mSkUIwBuc7ESdFuQhCKg0M0lT_D22XR89GU34hsPi15wLJ0o"))

inLineLinkTracktionNovum = InlineKeyboardMarkup(row_width=2)
inLineLinkTracktionNovum.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/7-ZMgJDfp9vQx9TrtWIKW3PiPl3pslRnSDXGT0lQF6YGotK6weE"))

inLineLinkXferLFOTool = InlineKeyboardMarkup(row_width=2)
inLineLinkXferLFOTool.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/OCoE-E8iAVrbsRxBz5HAxJbIVlo-fc8mmGJGHMj_8tp2k8BeE04"))

inLineLinkFactory = InlineKeyboardMarkup(row_width=2)
inLineLinkFactory.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/RSQC92DQwfq8pjXvtEzGC9TY0G69M12kqowCRvwWi0L_ZGjq1jo"))

inLineLinkRetrologue = InlineKeyboardMarkup(row_width=2)
inLineLinkRetrologue.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/EvVitoIpbXF3f-md-_LuEAnriAK30bqlDXRbeIHOeM2k9deJymM"))

inLineLinkANA2 = InlineKeyboardMarkup(row_width=2)
inLineLinkANA2.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/z-nO9hgI8vy4K3yhvishb7I_R-wgbEabwWqDe_vIKOjYgcrQR7Y"))

inLineLinkFASTBalancer = InlineKeyboardMarkup(row_width=2)
inLineLinkFASTBalancer.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/Bd8OyfvcfedbfTa3CI6DDpXwB9M3s9ex1h8lrb4Eh8uBAMfcjzo"))

inLineLinkScaler2 = InlineKeyboardMarkup(row_width=2)
inLineLinkScaler2.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/oAvK-Z1rOb8gB1fN9G1NlHBj_SUN77swiHNDHjjejXwQiI7APcg"))

inLineLinkKick2 = InlineKeyboardMarkup(row_width=2)
inLineLinkKick2.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/HKhhb4oZAuIH0zSA-WyquWcfhozYIEawqA-98PVUfPbTZcTWvWA"))

inLineLinkSubBassDoctor808 = InlineKeyboardMarkup(row_width=2)
inLineLinkSubBassDoctor808.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/TuXEfWdK4C3Ys8EcgXCZx72o5bPB0YBcto1nFIh6BJGYxqty8dw"))

inLineLinkReplikaXT = InlineKeyboardMarkup(row_width=2)
inLineLinkReplikaXT.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/krwhf6EVVMjAuhJ9RyL6mbEjrDimugrrHlbMlPi65d313ciA8sU"))

inLineLinkMassiveX = InlineKeyboardMarkup(row_width=2)
inLineLinkMassiveX.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/9GY2_YCv6iYUrOR9_rLOmHILFsni6NKnBdcSh2EgFA8NcHuC4-s"))

inLineLinkFabFilterBundle = InlineKeyboardMarkup(row_width=2)
inLineLinkFabFilterBundle.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/c2tQXmQCnBF76ZsOoKdvjmnTtGAbf6NINd_XJa-nhVpBrsYnUSg"))

inLineLinkArturiaPigments = InlineKeyboardMarkup(row_width=2)
inLineLinkArturiaPigments.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/Y8jCh4vjZzNYNQV4b-Awi1eiVPXUma-jvFIkPFhGJY1k1fnHEzg"))

inLineLinkAnaloglabV = InlineKeyboardMarkup(row_width=2)
inLineLinkAnaloglabV.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/ASib4LQZjARdQfuqwEKFmIzAdOpOOtV0fxF5Nc3xU1KfnV6x_wk"))

inLineLinkAutoTuneVocalEQ = InlineKeyboardMarkup(row_width=2)
inLineLinkAutoTuneVocalEQ.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/cV_Tjz8ExWcKb0ZvRXXHGGmuqV9_I4bFI8bialg67-Nc-rOqRbM"))

inLineLinkAutoTuneVocalEQ = InlineKeyboardMarkup(row_width=2)
inLineLinkAutoTuneVocalEQ.add(InlineKeyboardButton("Скачать плагин", url="https://vk.com/s/v1/doc/Z76WV0MA7TZIKaVF3dZ_0jLy7q-pheS_y45uIs0ZK6ZpD4CyU-g"))

inLineLinkFLStudio = InlineKeyboardMarkup(row_width=2)
inLineLinkFLStudio.add(InlineKeyboardButton("Скачать DAW", url="https://vk.com/doc154826112_620562991"))

inLineLinkCubase12 = InlineKeyboardMarkup(row_width=2)
inLineLinkCubase12.add(InlineKeyboardButton("Скачать DAW", url="https://vk.com/s/v1/doc/xivV1JrHEDp21UO31AmynHM7Ez5iJSnmZzUSd1GnfZxEiNBZx64"))

inLineLinkAbletonLive11 = InlineKeyboardMarkup(row_width=2)
inLineLinkAbletonLive11.add(InlineKeyboardButton("Скачать DAW", url="https://vk.com/s/v1/doc/JzXDalQPRG7ErcLO2eBswMtHJbs5YX8lPSbfS2CDoW_tAa7E9wI"))

inLineLinkLogicPro = InlineKeyboardMarkup(row_width=2)
inLineLinkLogicPro.add(InlineKeyboardButton("Скачать DAW", url="https://vk.com/s/v1/doc/Go5X4qGz9rs-e7gfsR2Uneml_pJVk61L4NzQjsFACrbYUq3V_sI"))
