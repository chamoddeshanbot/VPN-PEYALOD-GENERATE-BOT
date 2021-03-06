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
đŋ Hello Dear {} 

đ I'm You Info Bot

âŗ You Id
âŗ You First Name
âŗ You Last Name
âŗ You User Name
âŗ You Picture

đ How to Use Bot Press /help Command


âī¸đŋ Dev : || @chamod_deshan ||

[Network Tech](https://t.me/NetworksTech) Corporation ÂŠī¸ """


hcaption = """
đŋ Hello Dear {} 

âââââââââââââââ
 đ Command List đ
âââââââââââââââ

/start - đ Start Bot 

/help - đ How To Use Bot 

/picture - đ¸ You Picture

/username - â You Username

/id - đ You Id

/firstname - âī¸ You Firstname

/lastname - đ You Lastname """


pcaption = """
âī¸đŋ You Info Bot đąđ°

âââââââââââââââââ

đē You Username #command(/username)

â You Id #command(/id)

đŋ You Picture #command(/picture)

đˇ You name #command(/firstname)

đ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**

âââââââââââââââââī¸  """

STARTBUTTON = InlineKeyboardMarkup(
             [
                [
                    InlineKeyboardButton("â â° á´á´á´ á´á´ á´á´ ÉĸĘá´á´á´ âą â", url=f"https://t.me/The_my_info_bot?startgroup=true")
                 ],
                 [
                    InlineKeyboardButton(" Network Tech đąđ°", url = "https://t.me/NetworksTech"),
                    InlineKeyboardButton("Network Tech Chat đąđ° ", url = "https://t.me/Network_techchat")
                 ],
                 [
                    InlineKeyboardButton("đ¸ You Picture đ¸", callback_data = "picture"),
                    InlineKeyboardButton("đŋ You Username đŋ", callback_data = "usernam")
                 ],
                 [
                    InlineKeyboardButton("đˇ You Id đˇ", callback_data = "idt"),
                    InlineKeyboardButton("â You Name â", callback_data = "first")
                 ],
                 [
                    InlineKeyboardButton("âī¸đŋ   Dev  âī¸đŋ", user_id=1901997764),
                    InlineKeyboardButton("đ    Help    đ", callback_data = "hel")
                 ],
     
             ]

        )

HELPBUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("<<<< Back ", callback_data="sta")
        ]]
  )

@app.on_message(filters.private & filters.command("status"))
async def status(client, message):
    total_users = await db.total_users_count()
    text = "**You Info Bot Status**\n"
    text += f"\n**Total Users hit start:** `{total_users}`"
    await message.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_chat_action("typing")
    await app.send_photo(message.chat.id,
        photo=f"https://telegra.ph/file/f8032003dc5dc2f542e2d.jpg",
        caption=scaption.format(message.from_user.first_name),
        reply_markup=STARTBUTTON,
        reply_to_message_id = message.message_id)

@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_chat_action("typing")
    await app.send_photo(message.chat.id,
        photo=f"https://telegra.ph/file/f8032003dc5dc2f542e2d.jpg",
        caption=hcaption.format(message.from_user.mention),
        reply_markup=HELPBUTTON,
        reply_to_message_id = message.message_id)

@app.on_message(filters.sticker)
async def emoji(client, message):
    await message.reply_chat_action("typing")
    await message.reply("đĢ **Erorr** đĢ\n\nâ­ī¸ This Host Name Is unavailable...\nđ¯ Pleas Send Valid Sni Host Name...")

@app.on_message(filters.text)
async def tex(client, message):
    await message.reply_chat_action("typing")
    text = message.text
    mention = message.from_user.mention
    status = await message.reply("đĄ Connection To The **Evozi** ...",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("10%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("đĄ Connection To The **Evozi** ....",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("10%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("đĄ Connection To The **Evozi** ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("26%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("đĄ Connection To The **Evozi** ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("51%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("đĄ Connection To The **Evozi** ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("70%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("đĄ Connection To The **Evozi** ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("99%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("**â Evozi Connected Successfully ..**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("â°â°â°â°â°â°â°", callback_data="progress_msg")]]))
    await status.edit("**â Evozi Connected Successfully ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("â°â°â°â°â°â°â°", callback_data="progress_msg")]]))
    await status.edit("**â Evozi Connected Successfully .....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("â°â°â°â°â°â°â°", callback_data="progress_msg")]]))
    await status.edit("**â Generating You Payload ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("10%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("**â Generating You Payload ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("25%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("**â Generating You Payload .....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("25%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("**â Generating You Payload ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("56%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("**â Generating You Payload ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("89%âââââââââââââ", callback_data="progress_msg")]]))
    await status.edit("**â Generating You Payload ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("99%âââââââââââââ", callback_data="progress_msg")]]))
    payload = f"â SUCCESSFULLY GENERATED â\n\nâ­ī¸ You Host Name : âŗ `{text}`\n\nâž You Payload : âŗ `CONNECT [host_port] [protocol][crlf]Host: {text}[crlf]X-Online-Host: {text}[crlf]X-Forward-Host: {text}[crlf]X-Forwarded-For: {text}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Referer: {text}[crlf]Upgrade: websocket[crlf][crlf]`\n\nđˇ Requestor : âŗ {mention}\nâī¸đŋ Generated By : âŗ [THE EVOZI BOT](https://t.me/The_Evozi_bot)\n\n[Network Tech đąđ°](https://t.me/NetworksTech) Corporation ÂŠī¸"
    await status.edit(payload,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đģ Send Inbox đģ", callback_data="ib"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âī¸  Close  âī¸", callback_data="close"
                    )
                ]
            ]
          )
    )
@app.on_message(filters.forwarded & filters.private)
async def fd(client, message):
    await message.reply_chat_action("typing")
    text =f"Forward Id : {message.forward_from_chat.id}"
    idt = message.forward_from_chat.id
    photo = get(f"https://single-developers.up.railway.app/logo?name={text}").history[1].url
    icaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nâ Channel Id âŗ `{idt}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=icaption.format(message.chat.id),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ You Id Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đŋ My User Name đŋ", callback_data="usernam"
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
    icaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nâ Group Id âŗ `{gdt}`\n\nâ You Id âŗ `{idt}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=icaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ You Id Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đŋ My User Name đŋ", callback_data="usernam"
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
    ucaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nđē You Username âŗ `{ted}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=ucaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ You User Name Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "â My Name â", callback_data="first"
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
    ucaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nđē You Username âŗ `{ted}`\n\nâ Group Username âŗ `{ged}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=ucaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ You User Name Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "â My Name â", callback_data="first"
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
    fcaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nđē Group Name âŗ `{text}`\n\nâ You Name âŗ `{idy}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ You Name Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ¸ My Picture đ¸", callback_data="picture"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("firstname") & filters.private)
async def firstname(client, message):
    await message.reply_chat_action("typing")
    idy = message.from_user.first_name
    photo = get(f"https://single-developers.up.railway.app/logo?name={idy}").history[1].url
    fcaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nâ You Name âŗ `{idy}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
    await message.reply_chat_action("upload_photo")
    await app.send_photo(message.chat.id,
        photo=photo,
        caption=fcaption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ You Name Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ¸ My Picture đ¸", callback_data="picture"
                    )
                ]
            ]
          )
    )

@app.on_message(filters.command("lastname"))
async def firstname(client, message):
    await message.reply_chat_action("typing")
    text = message.from_user.last_name
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
                        "đ You Name Logo đ", url=f"{photo}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "đ¸ My Picture đ¸", callback_data="picture"
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
                        "đˇ You Id đˇ", callback_data="idt"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "â My name â", callback_data="first"
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
            await cmd.answer("đ¸ You Profile Photo")
            photoid = cmd.from_user.photo.big_file_id  
            photo = await app.download_media(photoid)
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=pcaption), reply_markup=STARTBUTTON)
            if os.path.exists(photo):os.remove(photo)
        except Exception as e:
            print(str(e))
            if os.path.exists(photo):os.remove(photo)
      elif "usernam" in cb_data:
        try:
            await cmd.answer(f"đŋ You User Name âŗ {cmd.from_user.username}")
            ted = cmd.from_user.username
            photo = get(f"https://single-developers.up.railway.app/logo?name={ted}").history[1].url
            ucaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nđē You Username âŗ `{ted}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=ucaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "idt" in cb_data:
        try:
            await cmd.answer(f"đŋ You Id âŗ {cmd.from_user.id}")
            ted = cmd.from_user.id
            photo = get(f"https://single-developers.up.railway.app/logo?name={ted}").history[1].url
            icaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nđē You id âŗ `{ted}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=icaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "first" in cb_data:
        try:
            await cmd.answer(f"đŋ You firstname âŗ {cmd.from_user.first_name}")
            ted = cmd.from_user.first_name
            photo = get(f"https://single-developers.up.railway.app/logo?name={ted}").history[1].url
            fcaption =f"âī¸đŋ You Info Bot đąđ°\n\nâââââââââââââââââ\n\nđē You id âŗ `{ted}`\n\nđ¤đŋ **Powered By **  : **[Network Tech đąđ°](https://t.me/NetworksTech)**\n\nâââââââââââââââââī¸"
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=fcaption), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "hel" in cb_data:
        try:
            await cmd.answer(f"đˇ Bot Help")
            await cmd.edit_message_media(InputMediaPhoto(media=f"https://telegra.ph/file/f8032003dc5dc2f542e2d.jpg", caption=hcaption.format(cmd.from_user.mention)), reply_markup=HELPBUTTON)
        except Exception as e:
            print(str(e))
      elif "sta" in cb_data:
        try:
            await cmd.answer(f"đ Bot menu")
            await cmd.edit_message_media(InputMediaPhoto(media=f"https://telegra.ph/file/f8032003dc5dc2f542e2d.jpg", caption=scaption.format(cmd.from_user.mention)), reply_markup=STARTBUTTON)
        except Exception as e:
            print(str(e))
      elif "close" in cb_data:
        try:
            await cmd.answer(f"âī¸ Close Menu âī¸")
            await cmd.message.delete()
        except Exception as e:
            print(str(e))

app.run()
