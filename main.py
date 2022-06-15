from pyrogram import Client, filters
from config import Config
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from requests import get
import os

app = Client(
    'My Info Bot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

scaption = """
🌿 Hello Dear {} 

🍀 I'm You Info Bot

➳ You Id
➳ You First Name
➳ You Last Name
➳ You User Name
➳ You Picture

🏖 How to Use Bot Press /help Command


✌️🏿 Dev : || @chamod_deshan ||

[Network Tech](https://t.me/NetworksTech) Corporation ©️ """


hcaption = """
🌿 Hello Dear {} 

◇─────────────◇
 📚 Command List 📚
◇─────────────◇

/start - 🏝 Start Bot 

/help - 🙋 How To Use Bot 

/picture - 📸 You Picture

/username - ✍ You Username

/id - 📝 You Id

/firstname - ✏️ You Firstname

/lastname - 📚 You Lastname """


pcaption = """
✌️🏿 You Info Bot 🇱🇰

◇───────────────◇

🌺 You Username #command(/username)

✍ You Id #command(/id)

🌿 You Picture #command(/picture)

🌷 You name #command(/firstname)

🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

STARTBUTTON = InlineKeyboardMarkup(
             [
                [
                    InlineKeyboardButton("➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_my_info_bot?startgroup=true")
                 ],
                 [
                    InlineKeyboardButton(" Network Tech 🇱🇰", url = "https://t.me/NetworksTech"),
                    InlineKeyboardButton("Network Tech Chat 🇱🇰 ", url = "https://t.me/Network_techchat")
                 ],
                 [
                    InlineKeyboardButton("📸 You Picture 📸", callback_data = "picture"),
                    InlineKeyboardButton("🌿 You Username 🌿", callback_data = "usernam")
                 ],
                 [
                    InlineKeyboardButton("🌷 You Id 🌷", callback_data = "idt"),
                    InlineKeyboardButton("✍ You Name ✍", callback_data = "first")
                 ],
                 [
                    InlineKeyboardButton("✌️🏿   Dev  ✌️🏿", user_id=1901997764),
                    InlineKeyboardButton("🆘    Help    🆘", callback_data = "hel")
                 ],
     
             ]

        )

HELPBUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("<<<< Back ", callback_data="sta")
        ]]
  )

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_chat_action("typing")
    await app.send_photo(message.chat.id,
        photo=f"https://telegra.ph/file/50b455f8692db9c198a70.jpg",
        caption=scaption.format(message.from_user.first_name),
        reply_markup=STARTBUTTON,
        reply_to_message_id = message.message_id)

@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_chat_action("typing")
    await app.send_photo(message.chat.id,
        photo=f"https://telegra.ph/file/50b455f8692db9c198a70.jpg",
        caption=hcaption.format(message.from_user.mention),
        reply_markup=HELPBUTTON,
        reply_to_message_id = message.message_id)

@app.on_message(filters.command("id") & filters.private)
async def id(client, message):
    await message.reply_chat_action("typing")
    text =f"You Id : {message.from_user.id}"
    idt = message.from_user.id
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    icaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n✍ You Id ➳ `{idt}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=icaption.format(message.chat.id),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You Id Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My User Name ", callback_data="user"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("id") & filters.group)
async def id(client, message):
    await message.reply_chat_action("typing")
    text =f"G : {message.chat.id}\n\nY : {message.from_user.id}"
    idt = message.from_user.id
    gdt = message.chat.id
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    icaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n✍ Group Id ➳ `{gdt}`\n\n✍ You Id ➳ `{idt}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=icaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You Id Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My User Name ", callback_data="user"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("username") & filters.private)
async def username(client, message):
    await message.reply_chat_action("typing")
    text =f"You : {message.from_user.username}"
    ted = message.from_user.username
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    ucaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n🌺 You Username ➳ `{ted}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=ucaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You User Name Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My Name ", callback_data="user"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("username") & filters.group)
async def username(client, message):
    await message.reply_chat_action("typing")
    text =f"G : {message.chat.username}\n\nY : {message.from_user.username}"
    ted = message.from_user.username
    ged = message.chat.username
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    ucaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n🌺 You Username ➳ `{ted}`\n\n✍ Group Username ➳ `{ged}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=ucaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You User Name Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My Name ", callback_data="user"
                    )
                ]
            ]
          )
    )


@app.on_message(filters.command("firstname") & filters.group)
async def firstname(client, message):
    await message.reply_chat_action("typing")
    text = message.chat.title
    idy = message.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    fcaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n🌺 Group Name ➳ `{text}`\n\n✍ You Name ➳ `{idy}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You Name Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My Picture ", callback_data="pic"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("firstname") & filters.private)
async def firstname(client, message):
    await message.reply_chat_action("typing")
    idy = message.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    fcaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n✍ You Name ➳ `{idy}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You Name Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My Picture ", callback_data="pic"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("lastname"))
async def firstname(client, message):
    await message.reply_chat_action("typing")
    text = message.chat.last_name
    if not text:
     await message.reply("not found")
     return
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption.format(message.chat.last_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You Name Logo", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My Picture ", callback_data="pic"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("picture"))
async def picture(client, message):
    await message.reply_chat_action("typing")
    photoid = message.chat.photo.big_file_id
    photo = await client.download_media(photoid)
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=pcaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "You Id", callback_data="id"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " My User Name ", callback_data="user"
                    )
                ]
            ]
          )
    )

@app.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):
      cb_data = cmd.data
      if "picture" in cb_data:
        try:
            await cmd.answer("📸 You Profile Photo")
            photoid = cmd.from_user.photo.big_file_id  
            photo = await app.download_media(photoid)
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=pcaption), reply_markup=STARTBUTTON)
            if os.path.exists(photo):os.remove(photo)
        except Exception as e:
            print(str(e))
            if os.path.exists(photo):os.remove(photo)
      elif "usernam" in cb_data:
        try:
            await cmd.answer(f"🌿 You User Name ➳ {cmd.from_user.username}")
            ted = cmd.from_user.username
            photo = get(f"https://single-developers.up.railway.app/logo?name={ted}").history[1].url
            ucaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n🌺 You Username ➳ `{ted}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=ucaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "idt" in cb_data:
        try:
            await cmd.answer(f"🌿 You Id ➳ {cmd.from_user.id}")
            ted = cmd.from_user.id
            photo = get(f"https://single-developers.up.railway.app/logo?name={ted}").history[1].url
            icaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n🌺 You id ➳ `{ted}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=icaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "first" in cb_data:
        try:
            await cmd.answer(f"🌿 You firstname ➳ {cmd.from_user.first_name}")
            ted = cmd.from_user.first_name
            photo = get(f"https://single-developers.up.railway.app/logo?name={ted}").history[1].url
            fcaption =f"✌️🏿 You Info Bot 🇱🇰\n\n◇───────────────◇\n\n🌺 You id ➳ `{ted}`\n\n🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**\n\n◇───────────────◇️"
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=fcaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "hel" in cb_data:
        try:
            await cmd.answer(f"🌷 Bot Help")
            await cmd.edit_message_media(InputMediaPhoto(media=f"https://telegra.ph/file/50b455f8692db9c198a70.jpg", caption=hcaption), reply_markup=HELPBUTTON)
        except Exception as e:
            print(str(e))
      elif "sta" in cb_data:
        try:
            await cmd.answer(f"🍀 Bot menu")
            await cmd.edit_message_media(InputMediaPhoto(media=f"https://telegra.ph/file/50b455f8692db9c198a70.jpg", caption=scaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))

app.run()
