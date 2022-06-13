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

🌷 ➳ You Id
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

✍ You Id ➳ `{}`

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

@app.on_message(filters.command("start"))
async def start(client, message):
    await app.send_photo(message.chat.id,
        photo=f"https://telegra.ph/file/50b455f8692db9c198a70.jpg",
        caption=scaption(message.from_user.first_name),
        reply_markup=STARTBUTTON,
        reply_to_message_id = message.message_id)

@app.on_message(filters.command("help"))
async def help(client, message):
    await app.send_photo(message.chat.id,
        photo=f"https://telegra.ph/file/50b455f8692db9c198a70.jpg",
        caption=hcaption,
        reply_markup=HELPBUTTON,
        reply_to_message_id = message.message_id)

@app.on_message(filters.command("id"))
async def id(client, message):
    text = {message.from_user.id}
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=icaption(message.from_user.id),
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
    text = {message.from_username}
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=ucaption(message.from_username),
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
    text = {message.from_user.first_name}
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption(message.from_user.first_name),
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
    photoid = message.from_user.photo.big_file_id
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
