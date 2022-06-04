from pyrogram import Client, filters
import random
from typing import Union
from config import Config
from logo import generate_logo
from logo import get_wallpapers, get_unsplash
from pyrogram.types import *
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
✍️ User Info Bot 🇱🇰

◇───────────────◇

🚀 ** You Id ** ➳ `{}`

🌺 **You Name** : #press Button(my name)

🌿 **My Picture ** : #press Button(my picture)

🤞🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """
caption2 = """
✍️ User Info Bot 🇱🇰

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
                        "✍ My name ✍", callback_data="name"
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
 
@app.on_callback_query(filters.regex("id"))
async def id(_,query):
    message = query.message
    await query.answer(f"🏖 You Id 🏖")
    text = message.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await query.message.send_photo(message.chat.id, photo=photo, caption =caption2.format(message.from_user.mention), reply_to_message_id = message.message_id,
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
    await query.message.delete()


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
