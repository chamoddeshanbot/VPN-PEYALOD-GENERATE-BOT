from pyrogram import Client, filters
import html

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from userbot.utils import lightning_cmd
import random
from config import Config
import result
from pyrogram.types import InputMediaPhoto, User, Message, InlineQueryResultPhoto, InlineQueryResult, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, Chat
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied, FloodWait
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram import filters
from telegram import Message, MessageId
from telegram.ext import CallbackContext, Filters, MessageHandler
from telegram.error import ChatMigrated
from telegram.update import Update
from pyrogram.types import Message
from pyrogram import Client
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


caption = """
✍️ User Info ✍️

◇───────────────◇

🚀 ** You Id ** ➳ `{}`

🌺 **You Name** : #press Button(my name)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """
caption2 = """
✍️ User Info ✍️

◇───────────────◇

🚀 ** You name ** ➳ {}

🌺 **You id ** : #press Button(my id)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

app = Client(
    'logo Bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
 
@app.on_message(filters.command("id"))
async def id(client, message):
  text = message.from_user.id
  photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
  await message.reply_chat_action("upload_photo")
  await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.id), reply_to_message_id = message.message_id,
               reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My name ✍", callback_data="n"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("n"))
async def n(client, message):
    text = message.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id, photo=photo, caption =caption2.format(message.from_user.mention), reply_to_message_id = message.message_id,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("n"))
async def n(client, message):
    profile = get_user_profile_photos(message.from_user.id).photos[0][-1]
    file = get_file(profile["file_id"])
    file.download(f"{user.id}.png")
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id, photo=photo, caption =caption2.format(message.from_user.mention), reply_to_message_id = message.message_id,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("info"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    replied_user_profile_photos = await borg(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "NaN"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = html.escape(replied_user.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    last_name = (
        last_name.replace("\u2060", "") if last_name else ("Last Name not found")
    )
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception as e:
        dc_id = "`Need a Profile Picture to check **this**`"
        str(e)
    caption = """<b>Extracted User info From Telegram By Black Lightning<b>
<b>🆔️User ID</b>: <code>{}</code>
<b>📎Link To Profile</b>: <a href='tg://user?id={}'>Click Here🚪</a>
<b>🗣️First Name</b>: <code>{}</code>
<b>🗣️Second Name</b>: <code>{}</code>
<b>👨🏿‍💻BIO</b>: {}
<b>🌐DC ID</b>: {}
<b>📸NO OF PSS</b> : {}
<b>🧐RESTRICTED</b>: {}
<b>✅VERIFIED</b>: {}
<b>🤖BOT</b>: {}
<b>👥Groups in Common</b>: {}
""".format(
        user_id,
        user_id,
        first_name,
        last_name,
        user_bio,
        dc_id,
        replied_user_profile_photos_count,
        replied_user.user.restricted,
        replied_user.user.verified,
        replied_user.user.bot,
        common_chats,
    )
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = event.message.id
    await borg.send_message(
        event.chat_id,
        caption,
        reply_to=message_id_to_reply,
        parse_mode="HTML",
        file=replied_user.profile_photo,
        force_document=False,
        silent=True,
    )
    await event.delete()


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id
                    or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.from_id)
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e




@app.on_callback_query(filters.regex("id"))
async def id(_,query):
    message = query.message
    await query.answer(f"🤞🏿 You Id 🏖")
    await query.message.delete()
    text = query.from_user.id
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await query.message.reply_photo(photo,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My name ✍", callback_data="n"
                    )
                ]
            ]
          )
    )
    
@app.on_callback_query(filters.regex("n"))
async def n(_,query):
    message = query.message
    await query.answer(f"🤞🏿 You Name 🏖")
    await query.message.delete()
    text = query.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await query.message.reply(caption2.format(query.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📸 My Picture 📸", callback_data="pic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✍ My Id ✍", callback_data="id"
                    )
                ]
            ]
          )
    )

@app.on_callback_query()
async def button(app, update):
      cb_data = update.data
      if "id" in cb_data:
        await update.message.delete()
        await id(app, update.message)
      elif "n" in cb_data:
        await update.message.delete()
        await n(app, update.message)
      elif "ha" in cb_data:
        await update.message.delete()

app.run()
