from pyrogram import Client, filters
from bot import app
from pyrogram.types import *
import result
from pyrogram import enums
from pyrogram.types import User, Message, InlineQueryResultPhoto, InlineQueryResult, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


caption = """
✍️ Logo Generated Successfully✅

◇───────────────◇

🚀 **Generated By** : **[LOGO GENERATE BOT 🔅](http://t.me/The_logo_generate_bot)**

🌺 **Requestor** :||** {} **||

🌷 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """
caption2 = """
✍️ Write picture Generated Successfully✅

◇───────────────◇

🚀 **Generated By** : **[LOGO GENERATE BOT 🔅](http://t.me/The_logo_generate_bot)**

🌺 **Requestor** :||** {} **||

🌷 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  
    """

caption3 = """
✍️ Wallpaper Generated Successfully✅

◇───────────────◇

🚀 **Generated By** : **[LOGO GENERATE BOT 🔅](http://t.me/The_logo_generate_bot)**

🌺 **Requestor** :||** {} **||

🌷 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  
    """

caption4 = """
✍️ Logohq Generated Successfully✅

◇───────────────◇

🚀 **Generated By** : **[LOGO GENERATE BOT 🔅](http://t.me/The_logo_generate_bot)**

🌺 **Requestor** :||** {} **||

🌷 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  
    """

HELP = """

**🖼 How To Use Me ?**

**♻️ Example:** 

/slogo NetworkTech
/slogohq NetworkTech
/swrite NetworkTech
/swall Trees
/nlogo NetworkTech
/nlogohq NetworkTech
"""


FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Network Tech 🇱🇰", url=f"https://t.me/NetworksTech") 
        ]]      
    )

@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_sticker(sticker = "CAACAgUAAxkBAAIDTmIH_UzldE-IIKD0-N_n_hrcVhzRAAKaAwACKwAB-VTV1LdMsVUFGCME")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/12155d9fd310edf3fab33.jpg",
        caption = """
🍀 hello There 

🙋‍♂️ I am Logo Generate Bot,I can 

🌺 Generating logo
🌷 Generating wallpaper
🚀 Generating 4k logo
🍀 Writing Picture
🔥 **Inline search Image**
🎯 24 horse active

🔥 Bot Commands 🔥

/logo Ex:NetworksTech
/logo2 Ex:NetworksTech
/logohq Ex:NetworksTech 
/write Ex:NetworksTech
/wall Ex:Tress

🌿 Developer : || @chamod_deshan ||

🔥 [Network Tech 🇱🇰](https://t.me/NetworksTech) Corporation ©️
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_logo_generate_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech 🇱🇰", url=f"https://t.me/NetworksTech"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech Chat 🇱🇰", url="https://t.me/Network_techchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷 Help Developer 🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(text=
                       "◇────🔍 Search Here Image 🔎────◇", switch_inline_query_current_chat=""
                    )
                ]
           ]
        )
    )


@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/12155d9fd310edf3fab33.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="<<< Back", callback_data="start_menu")]]))   


@app.on_message(filters.command("about"))
async def about_(client: Client, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_sticker(sticker = "DQACAgIAAxkDAAICu2ITEswmgapB0Se4csaQajDGqEsuAALlFAACCgKYSO2Ba4oM42CVIwQ")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/12155d9fd310edf3fab33.jpg",
        caption = """

🔥 [Network Tech 🇱🇰](https://t.me/NetworksTech) Corporation ©️
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_logo_generate_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech 🇱🇰", url=f"https://t.me/NetworksTech"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Network Tech Chat 🇱🇰", url="https://t.me/Network_techchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷 Help Developer 🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(text=
                       "◇────🔍 Search Here Image 🔎────◇", switch_inline_query_current_chat=""
                    )
                ]
           ]
        )
    )

ibn = """**🎨 Successfully Generated logo ✅**\n**🏖 This Logo was sent to the Requester by Bot Inbox 🛠**"""
    
    
@app.on_message(filters.command("ib"))
async def ib(Client, message):
    await message.reply(ibn)
    
    
@app.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    status = await message.reply("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    text = message.text.split(None, 1)[1]
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌷 Open In Google 🌷", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏖 Send Inbox 🏖", callback_data="ib"
                    )
                ]
            ]
          )
    )
    await status.delete()

#hq logo creator
@app.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    status = await message.reply("**⚙ Generating You 4k Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You 4k Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You 4k Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    text = message.text.split(None, 1)[1]
    photo = get(f"https://single-developers.up.railway.app/logohq?name={text}").history[1].url
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await app.send_photo(message.chat.id, photo=photo, caption =caption4.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌷 Open In Google 🌷", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏖 Send Inbox 🏖", callback_data="ib"
                    )
                ]
            ]
          )
    )
    await status.delete()

#handwrite
@app.on_message(filters.command("write"))
async def on_off_antiarab(_, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    status = await message.reply("**⚙ Writing You Picture ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Writing You Picture ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Writing You Picture ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    text = message.text.split(None, 1)[1]
    API = "https://single-developers.up.railway.app/write"
    body = {     
     "text":f"{text}"     
    }
    req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)
    img = req.history[1].url
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await app.send_photo(message.chat.id, photo=img, caption =caption2.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌷 Open In Google 🌷", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏖 Send Inbox 🏖", callback_data="ib"
                    )
                ]
            ]
          )
    )
    await status.delete()

#wallpaper
@app.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    status = await message.reply("**⚙ Generating You Wallpaper ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Wallpaper ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Wallpaper ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    text = message.text.split(None, 1)[1]
    photo = get(f"https://single-developers.up.railway.app/wallpaper?search={text}").history[1].url
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await app.send_photo(message.chat.id, photo=photo, caption=caption3.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌷 Open In Google 🌷", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏖 Send Inbox 🏖", callback_data="ib"
                    )
                ]
            ]
          )
    )
    await status.delete()

@app.on_message(filters.command("nlogo"))
async def on_off_antiarab(_, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    status = await message.reply("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logo ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    text = message.text.split(None, 1)[1]
    photo = get(f"https://techzbotsapi.herokuapp.com/logo?text={text}").history[1].url
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await app.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌷 Open In Google 🌷", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏖 Send Inbox 🏖", callback_data="ib"
                    )
                ]
            ]
          )
    )
    await status.delete()

    
@app.on_message(filters.command("nlogohq"))
async def on_off_antiarab(_, message: Message):
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        await message._client.get_chat_member(int("-1001638745764"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @NetworksTech  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    status = await message.reply("**⚙ Generating You Logohq ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logohq ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("██████░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**⚙ Generating You Logohq ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("█████████████", callback_data="progress_msg")]]))
    text = message.text.split(None, 1)[1]
    photo = get(f"https://techzbotsapi.herokuapp.com/logo?square=true&text={text}").history[1].url
    await message.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
    await app.send_photo(message.chat.id, photo=photo, caption =caption4.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌷 Open In Google 🌷", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏖 Send Inbox 🏖", callback_data="ib"
                    )
                ]
            ]
          )
    )
    await status.delete()

API = "https://apibu.herokuapp.com/api/y-images?query="

button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Network Tech 🇱🇰", url=f"https://t.me/NetworksTech")
        ],
        [
            InlineKeyboardButton("🔍◇─◇Search Again◇─◇🔎", switch_inline_query_current_chat="")
        ]
    ]
    
    )


@app.on_callback_query(filters.regex("help"))
async def help(_,query):
  await query.answer(f"🏖 Bot Help 🏖")
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="<<< Back", callback_data="start")]]))


@app.on_callback_query()
async def button(app, update):
      cb_data = update.data
      if "ib" in cb_data:
        await update.message.delete()
        await ib(app, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await query.answer(f"🏖 Start Menu 🏖")
        await start(app, update.message)

@app.on_inline_query()
async def search(bot, update):
    results = requests.get(API + requests.utils.requote_uri(update.query)).json()["result"][:50]
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.capitalize(),
                description=result,
                reply_markup= button,
                caption="Netwok Tech 🇱🇰](https://t.me/NetwoksTech)  corporation ©",
                photo_url=result
            )
        )
    await update.answer(answers)

app.run()
