from pyrogram import Client, filters
from config import Config
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from requests import get

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

icaption = """
✌️🏿 You Info Bot 🇱🇰

◇───────────────◇

✍ Group Id ➳ `{}`

✍ You Id ➳ `{idt}`

🌺 You Name #command(/firstname)

🌿 You Picture #command(/picture)

🌷 You Username #command(/username)

🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """


ucaption = """
✌️🏿 You Info Bot 🇱🇰

◇───────────────◇

🌺 You Username ➳ `{}`

✍ You Id #command(/id)

🌿 You Picture #command(/picture)

🌷 You name #command(/firstname)

🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

fcaption = """
✌️🏿 You Info Bot 🇱🇰

◇───────────────◇

🌺 You Firstname ➳ {}

✍ You Id #command(/id)

🌿 You Picture #command(/picture)

🌷 You Username #command(/username)

🤘🏿 **Powered By **  : **[Network Tech 🇱🇰](https://t.me/NetworksTech)**

◇───────────────◇️  """

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
                    InlineKeyboardButton("📸 You Picture 📸", callback_data = "picme"),
                    InlineKeyboardButton("🌿 You Username 🌿", callback_data = "logo")
                 ],
                 [
                    InlineKeyboardButton("🌷 You Id 🌷", callback_data = "wall"),
                    InlineKeyboardButton("✍ You Name ✍", user_id=1901997764)
                 ],
                 [
                    InlineKeyboardButton("✌️🏿   Dev  ✌️🏿", callback_data = "info"),
                    InlineKeyboardButton("🆘    Help    🆘", callback_data = "hirs")
                 ],
     
             ]

        )

HELPBUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("<<<< Back ", callback_data="start")
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
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
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
    text =f"G : {message.chat.id}\n\nY: {message.from_user.id}"
    idt = message.from_user.id
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
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

@app.on_message(filters.command("username"))
async def username(client, message):
    await message.reply_chat_action("typing")
    text =f"Username : {message.from_user.username}"
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=ucaption.format(message.chat.username),
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


@app.on_message(filters.command("firstname"))
async def firstname(client, message):
    await message.reply_chat_action("typing")
    text = message.chat.first_name
    if not text:
     await message.reply("not found")
     return
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption.format(message.chat.first_name),
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

app.run()
