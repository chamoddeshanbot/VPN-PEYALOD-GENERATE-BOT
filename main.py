import os
import asyncio
import requests
import pyrogram
from requests import get
from pyrogram import filters,Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message
import config
import mongo
from mongo import db
from pyrogram.types import CallbackQuery,InlineKeyboardMarkup, InlineKeyboardButton, Message, InputMediaPhoto

SUDO_USERS = config.SUDO_USER

app = Client(
    "ads bot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

save = {}
grouplist = 1


@app.on_message(filters.command(["start", "help"]))
async def start_command(_, message: Message):
        if await mongo.is_banned_user(message.from_user.id):
            return
        await mongo.add_served_user(message.from_user.id)
        await message.reply_text(f"""
✍️ Hello {message.from_user.mention}!!

🌺You Can Contact  @supunma  Using This BOT 💁‍♂️

========================
- ғeel ғree тo reporт вυɢѕ 🐞.
- ѕυɢɢeѕтιoɴѕ αre welcoмe 🐣.
- coɴтαcт αɴy вoт proвleм 🐍.
- αѕĸ αɴy qυeѕтιoɴѕ 🦑.
- 24 ʜᴏᴜяѕ αᴄᴛɪᴠє  ♻️.
========================

☘️[Advertise on Telegram 🚀](https://t.me/TGramADS)☘️

All of about me included  in @aboutsupun channel ✌️
""",reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("📮 Ads - BOTS 🤖", callback_data = "bots"),
                    InlineKeyboardButton("📮 Ads - Channels🔔", callback_data = "channels"),
                 ],
                 [
                    InlineKeyboardButton("📮 Ads - Groups 💬", callback_data = "groups"),
                    InlineKeyboardButton("⚒ Help", callback_data = "help"),
                 ],
                 [
                    InlineKeyboardButton("✅ Promoting Cryptocurrency 💫", url = "https://telega.io/catalog_bots/szrosebot/card"),
                 ],
             ]
            ),
                disable_web_page_preview=True,
        )

caption = """
👋 Hey There , I am [supun Assistant BOT](http://t.me/supunmabot)🙋‍♂️. Do you want to Take a Picture ? 🙈. Click The Pick Me Button Below , I will Capture you 😁

☘️ Pic Me - Capture Your Profile Picture
🎁 Logo - **Generate Logo** With Your Name
👁‍🗨 My Info - Show Your Details
🌷 Wallpapers - Generate **HD Wallpapers**
📰 Hiru News - Get current situation of Sri lanka
"""
buttons = InlineKeyboardMarkup(
             [
                [
                    InlineKeyboardButton("SZ team bots 🇱🇰", url = "https://t.me/szteambots"),
                    InlineKeyboardButton("SL Bot Zone 🇱🇰 ", url = "https://t.me/slbotzone")
                 ],
                 [
                    InlineKeyboardButton("🙋‍♂️ Pic Me 🙊", callback_data = "picme"),
                    InlineKeyboardButton("🎁 Logo For Me 🎁", callback_data = "logo")
                 ],
                 [
                    InlineKeyboardButton("🌷 Wallpapers 🌷", callback_data = "wall"),
                    InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=1467358214)
                 ],
                 [
                    InlineKeyboardButton("👁‍🗨 My Info 👁‍🗨", callback_data = "info"),
                    InlineKeyboardButton("📰 Hiru News 📰", callback_data = "hirs")
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "back"),
                 ],
             ]
)

@app.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):
    name = cmd.from_user.id
    cb_data = cmd.data
    if "back" in cb_data:
        await cmd.message.delete()
        await app.send_message(
            chat_id = name,
            text = f"""
✍️ Hello {cmd.from_user.mention}!!

🌺You Can Contact  @supunma  Using This BOT 💁‍♂️

========================
- ғeel ғree тo reporт вυɢѕ 🐞.
- ѕυɢɢeѕтιoɴѕ αre welcoмe 🐣.
- coɴтαcт αɴy вoт proвleм 🐍.
- αѕĸ αɴy qυeѕтιoɴѕ 🦑.
- 24 ʜᴏᴜяѕ αᴄᴛɪᴠє  ♻️.
========================

☘️[Advertise on Telegram 🚀](https://t.me/TGramADS)☘️

All of about me included  in @aboutsupun channel ✌️"""
,reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("📮 Ads - BOTS 🤖", callback_data = "bots"),
                    InlineKeyboardButton("📮 Ads - Channels🔔", callback_data = "channels"),
                 ],
                 [
                    InlineKeyboardButton("📮 Ads - Groups 💬", callback_data = "groups"),
                    InlineKeyboardButton("⚒ Help", callback_data = "help"),
                 ],
                 [
                    InlineKeyboardButton("✅ Promoting Cryptocurrency 💫", url = "https://telega.io/catalog_bots/szrosebot/card"),
                 ],
             ]
            ),
                disable_web_page_preview=True,
        )
    if "bots" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/e2431af5ada17d8981b54.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «Rose bot ✨» 

✅ Start bot: @szrosebot
⏰ Date checked: `04.06.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `2.2K`
💸 **Advertising publication cost**: `$4.80`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/szrosebot/card"),
                 ],
                 [
                    InlineKeyboardButton("Next »", callback_data = "mafia"),
                 ],
             ]
            )
        )
    if "mafia" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/01afcf727ad819fcc9a45.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «Premium Accounts BOT» 

✅ Start bot: @MafiaPremiumAccBot
⏰ Date checked: `30.05.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `1.2K`
💸 **Advertising publication cost**: `$3.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/MafiaPremiumAccBot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "bots"),
                    InlineKeyboardButton("Next »", callback_data = "lion")
                 ],
             ]
            )
        )
    if "lion" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/9349c49ce380f29b75e11.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «Lion heart Bot 🤖» 

✅ Start bot: @EHIfilebot
⏰ Date checked: `18.05.2022`   
🏷 Topic: Crypto

📊 **Active Users** : `1.5K`
💸 **Advertising publication cost**: `$3`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/MafiaPremiumAccBot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "mafia"),
                    InlineKeyboardButton("Next »", callback_data = "malith")
                 ],
             ]
))
    if "malith" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/3c19c03695399590bf538.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «☘️ SSH Creator BOT ☘️» 

✅ Start bot: @malithrukshan_bot
⏰ Date checked: `13.05.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `3.4K`
💸 **Advertising publication cost**: `$6`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/malithrukshan_bot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "lion"),
                    InlineKeyboardButton("Next »", callback_data = "dark")
                 ],
             ]
))
    if "dark" in cb_data:
        await cmd.message.delete()
        await app.send_message(
            chat_id = name,
            text = """
🗣 **Advertising on the Telegram bot** «🛰 SSH Creator BOT 🛰» 

✅ Start bot: @sbatrow_bot
⏰ Date checked: `10.05.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `1K`
💸 **Advertising publication cost**: `$3.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/sbatrow_bot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "malith"),
                    InlineKeyboardButton("Next »", callback_data = "mod")
                 ],
             ]
))
    if "mod" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/3b1c24e985cde7b238204.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «🔰 MOD Aρρ BOT 🔰» 

✅ Start bot: @MOD_APK_ROBOT
⏰ Date checked: `29.05.2022`   
🏷 Topic: Other

📊 **Active Users** : `3.0K`
💸 **Advertising publication cost**: `$6.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/MOD_APK_ROBOT/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "dark"),
                    InlineKeyboardButton("Next »", callback_data = "hiru")
                 ],
             ]
))
    if "hiru" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/2f7feaa35ff9643e48eaf.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «💬 Hıru Neɯs BOT 📥» 

✅ Start bot: @Hiru_NEWS_BOT
⏰ Date checked: `13.05.2022`   
🏷 Topic: Other

📊 **Active Users** : `2.5K`
💸 **Advertising publication cost**: `$3.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/Hiru_NEWS_BOT/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "mod"),
                    InlineKeyboardButton("Next »", callback_data = "cine")
                 ],
             ]
))
    if "cine" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/530a925d2ac17f09d113d.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «Cιηε βrσ» 

✅ Start bot: @cinesubzbot
⏰ Date checked: `02.06.2022`   
🏷 Topic: Videos and movies

📊 **Active Users** : `1.9K`
💸 **Advertising publication cost**: `$3.72`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/cinesubzbot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "hiru"),
                    InlineKeyboardButton("Next »", callback_data = "finder")
                 ],
             ]
))
    if "finder" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/b407901cf5b22a750c767.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «🎧 MUSIC ҒIΠDΣR BOT 🎵» 

✅ Start bot: @The_Shazam_BOT
⏰ Date checked: `31.01.2022`   
🏷 Topic: Music and audio

📊 **Active Users** : `5.9K`
💸 **Advertising publication cost**: `$6.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/The_Shazam_BOT/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "cine"),
                    InlineKeyboardButton("Next »", callback_data = "tost")
                 ],
             ]
))
    if "tost" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/be24e3fea0326883da659.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «🔰 TOST Gen BOT 🔰» 

✅ Start bot: @TOST_Gen_BOT
⏰ Date checked: `31.01.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `1.3K`
💸 **Advertising publication cost**: `$3.72`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/TOST_Gen_BOT/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "finder"),
                    InlineKeyboardButton("Next »", callback_data = "renew")
                 ],
             ]
))
    if "renew" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/4b9ab68789b0218e94285.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «💰 Crypto Update BOT 💵» 

✅ Start bot: @SSH_Renew_Bot
⏰ Date checked: `24.04.2022`   
🏷 Topic: Crypto

📊 **Active Users** : `1.8K`
💸 **Advertising publication cost**: `$3.72`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/SSH_Renew_Bot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "finder"),
                    InlineKeyboardButton("Next »", callback_data = "vpn")
                 ],
             ]
))
    if "vpn" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/9bec52284199e655dc496.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «💰 Crypto - ☘️ The VPN Stock BOT ☘️» 

✅ Start bot: @vpn_stock_bot
⏰ Date checked: `31.05.2022`   
🏷 Topic: Crypto

📊 **Active Users** : `8.5K`
💸 **Advertising publication cost**: `$9.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/vpn_stock_bot/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "renew"),
                    InlineKeyboardButton("Next »", callback_data = "viwe")
                 ],
             ]
))
    if "viwe" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/46e20244a26be8793f4ad.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «👁‍🗨 Views Counter BOT 🤖» 

✅ Start bot: @ViewsCounterBOT
⏰ Date checked: `08.05.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `1K`
💸 **Advertising publication cost**: `$2.40`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/ViewsCounterBOT/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "vpn"),
                    InlineKeyboardButton("Next »", callback_data = "any")
                 ],
             ]
))
    if "any" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/944eaefe562e172ff6fd8.jpg",
            caption = """
🗣 **Advertising on the Telegram bot** «💫 Any Share BOT 🤖» 

✅ Start bot: @AnyShareBOT
⏰ Date checked: `06.06.2022`   
🏷 Topic: Anonymous chats

📊 **Active Users** : `1K`
💸 **Advertising publication cost**: `$2.40`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/AnyShareBOT/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "vpn"),
                    InlineKeyboardButton("📮Buy Ads - Channels🔔", callback_data = "channels")
                 ],
             ]
))
    if "channels" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/944eaefe562e172ff6fd8.jpg",
            caption = """
🗣 **Advertising on the Telegram channel** «☘️ The VPN Stock ☘️» 

✅ Start channel: @VPN_Stock
🔔 Language: English
🎯 Topic: Cryptocurrencies

📊 **Active Users** : `6.3K`
💸 **Advertising publication cost**: `$9.60`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/VPN_Stock/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "vpn"),
                    InlineKeyboardButton("📮Buy Ads - Groups 💬", callback_data = "groups")
                 ],
             ]
))
    if "groups" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/944eaefe562e172ff6fd8.jpg",
            caption = """
🗣 **Advertising on the Telegram channel** «☘️ The SSH Store ☘️» 

✅ Start channel: @SSH_Store
🔔 Language: English
🎯 Topic: Cryptocurrencies

📊 **Active Users** : `8.8K`
💸 **Advertising publication cost**: `$7.20`"""
,reply_markup = InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("Buy Now💰", url = "https://telega.io/catalog_bots/SSH_Store/card"),
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "channels"),
                 ],
             ]
))
    if "help" in cb_data:
        await cmd.message.delete()
        await app.send_photo(
            chat_id = name,
            photo = "https://telegra.ph/file/7ee0596d607666e88cc0d.jpg",
            caption = """
👋 Hey There , I am [supun Assistant BOT](http://t.me/supunmabot)🙋‍♂️. Do you want to Take a Picture ? 🙈. Click The Pick Me Button Below , I will Capture you 😁

☘️ Pic Me - Capture Your Profile Picture
🎁 Logo - **Generate Logo** With Your Name
👁‍🗨 My Info - Show Your Details
🌷 Wallpapers - Generate **HD Wallpapers**
📰 Hiru News - Get current situation of Sri lanka
"""
,reply_markup = InlineKeyboardMarkup(
             [
                [
                    InlineKeyboardButton("SZ team bots 🇱🇰", url = "https://t.me/szteambots"),
                    InlineKeyboardButton("SL Bot Zone 🇱🇰 ", url = "https://t.me/slbotzone")
                 ],
                 [
                    InlineKeyboardButton("🙋‍♂️ Pic Me 🙊", callback_data = "picme"),
                    InlineKeyboardButton("🎁 Logo For Me 🎁", callback_data = "logo")
                 ],
                 [
                    InlineKeyboardButton("🌷 Wallpapers 🌷", callback_data = "wall"),
                    InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=1467358214)
                 ],
                 [
                    InlineKeyboardButton("👁‍🗨 My Info 👁‍🗨", callback_data = "info"),
                    InlineKeyboardButton("📰 Hiru News 📰", callback_data = "hirs")
                 ],
                 [
                    InlineKeyboardButton("« Back", callback_data = "back"),
                 ],
             ]
))
    if "picme" in cb_data:
        try:
            await cmd.answer("⚒ Capture started...Creating Your dp")
            photoid = cmd.from_user.photo.big_file_id  
            photo = await app.download_media(photoid)
            await cmd.edit_message_media(InputMediaPhoto(media=photo, caption=caption), reply_markup=buttons)
            if os.path.exists(photo):os.remove(photo)
        except Exception as e:
            print(str(e))
            if os.path.exists(photo):os.remove(photo)  
    if "logo" in cb_data:
          try:
            await cmd.answer("⚒ Creating Your logo..")
            req = requests.get(f"https://host.single-developers.software/logo?name={cmd.from_user.first_name}".replace(' ','%20'))
            await cmd.edit_message_media(InputMediaPhoto(media=req, caption=caption), reply_markup=buttons)
          except Exception as e:
            print(str(e))
    if "wall" in cb_data:
         try:
            await cmd.answer("⚒ Creating Your wallpaper..")
            API = 'https://host.single-developers.software/logo?name=%20'
            req = requests.post(API).history[1].url
            await cmd.edit_message_media(InputMediaPhoto(media=req, caption=caption), reply_markup=buttons)
         except Exception as e:
            print(str(e))
    if "hirs" in cb_data:
          try:
            await cmd.answer("📡 News Updateing...")
            api = get("https://single-developers.up.railway.app/hirunews?type=main").json()
            title = api["title"]
            textss = api["text"]
            img = api["img"]
            date = api["date"]
            url = api["url"]
            await cmd.edit_message_media(InputMediaPhoto(media=img, caption=f"""
🏷 **{title}**

📮 {textss}

⏰ Date : {date}

[🔔View In Website]({url})
"""), reply_markup=buttons)
    
          except Exception as e:
            print(str(e))
    if "info" in cb_data:
          try:
            await cmd.answer(f"User Id:{cmd.from_user.id}\nName:{cmd.from_user.first_name}",show_alert=True)
          except Exception as e:
            print(str(e))

@app.on_message(
        filters.command("mode") & filters.user([1483482076,1467358214])
    )
async def mode_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        usage = "**Usage:**\n\n/mode [group | private]\n\n**Group**: All the incoming messages will be forwarded to Log group.\n\n**Private**: All the incoming messages will be forwarded to the Private Messages of SUDO_USERS"
        if len(message.command) != 2:
            return await message.reply_text(usage)
        state = message.text.split(None, 1)[1].strip()
        state = state.lower()
        if state == "group":
            await mongo.group_on()
            await message.reply_text(
                "Group Mode Enabled. All the incoming messages will be forwarded to LOG Group"
            )
        elif state == "private":
            await mongo.group_off()
            await message.reply_text(
                "Private Mode Enabled. All the incoming messages will be forwarded to Private Message of all SUDO_USERs"
            )
        else:
            await message.reply_text(usage)

@app.on_message(
        filters.command("block") & filters.user([1483482076,1467358214])
    )
async def block_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        if message.reply_to_message:
            if not message.reply_to_message.forward_sender_name:
                return await message.reply_text(
                    "Please reply to forwarded messages only."
                )
            replied_id = message.reply_to_message_id
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                print(e)
                return await message.reply_text(
                    "Failed to fetch user. You might've restarted bot or some error happened. Please check logs"
                )
            if await mongo.is_banned_user(replied_user_id):
                return await message.reply_text("Already Blocked")
            else:
                await mongo.add_banned_user(replied_user_id)
                await message.reply_text("Banned User from The Bot")
        else:
            return await message.reply_text(
                "Reply to a user's forwarded message to block him from using the bot"
            )

@app.on_message(
        filters.command("unblock") & filters.user([1483482076,1467358214])
    )
async def unblock_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        if message.reply_to_message:
            if not message.reply_to_message.forward_sender_name:
                return await message.reply_text(
                    "Please reply to forwarded messages only."
                )
            replied_id = message.reply_to_message_id
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                print(e)
                return await message.reply_text(
                    "Failed to fetch user. You might've restarted bot or some error happened. Please check logs"
                )
            if not await mongo.is_banned_user(replied_user_id):
                return await message.reply_text("Already UnBlocked")
            else:
                await mongo.remove_banned_user(replied_user_id)
                await message.reply_text(
                    "Unblocked User from The Bot"
                )
        else:
            return await message.reply_text(
                "Reply to a user's forwarded message to unblock him from the bot"
            )

@app.on_message(
        filters.command("stats") & filters.user([1483482076,1467358214])
    )
async def stats_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        served_users = len(await mongo.get_served_users())
        blocked = await mongo.get_banned_count()
        text = f""" 
**Stats:**

**Served Users:** {served_users} 
**Blocked Users:** {blocked}"""
        await message.reply_text(text)

@app.on_message(
        filters.command("broadcast") & filters.user([1483482076,1467358214])
    )
async def broadcast_func(_, message: Message):
        if db is None:
            return await message.reply_text(
                "MONGO_DB_URI var not defined. Please define it first"
            )
        if message.reply_to_message:
            x = message.reply_to_message.message_id
            y = message.chat.id
        else:
            if len(message.command) < 2:
                return await message.reply_text(
                    "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
                )
            query = message.text.split(None, 1)[1]

        susr = 0
        served_users = []
        susers = await mongo.get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                await app.forward_messages(
                    i, y, x
                ) if message.reply_to_message else await app.send_message(
                    i, text=query
                )
                susr += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                pass
        try:
            await message.reply_text(
                f"**Broadcasted Message to {susr} Users.**"
            )
        except:
            pass

@app.on_message(filters.private & ~filters.edited)
async def incoming_private(_, message):
        user_id = message.from_user.id
        if await mongo.is_banned_user(user_id):
            return
        if user_id == 1467358214:
            if message.reply_to_message:
                if (
                    message.text == "/unblock"
                    or message.text == "/block"
                    or message.text == "/broadcast"
                ):
                    return
                replied_id = message.reply_to_message_id
                try:
                    replied_user_id = save[replied_id]
                except Exception as e:
                    print(e)
                try:
                    return await app.copy_message(
                        replied_user_id,
                        message.chat.id,
                        message.message_id,
                    )
                except Exception as e:
                    print(e)
        else:
            if await mongo.is_group():
                try:
                    forwarded = await app.forward_messages(
                        config.LOG_GROUP_ID,
                        message.chat.id,
                        message.message_id,
                    )
                    save[forwarded.message_id] = user_id
                except:
                    pass
            else:
                try:
                        forwarded = await app.forward_messages(
                            1467358214, message.chat.id, message.message_id
                        )
                        save[forwarded.message_id] = user_id
                except:
                    pass

@app.on_message(
        filters.group & ~filters.edited & filters.user([1483482076,1467358214]),
        group=grouplist,
    )
async def incoming_groups(_, message):
        if message.reply_to_message:
            if (
                message.text == "/unblock"
                or message.text == "/block"
                or message.text == "/broadcast"
            ):
                return
            replied_id = message.reply_to_message_id
            if not message.reply_to_message.forward_sender_name:
                return await message.reply_text(
                    "Please reply to forwarded messages only."
                )
            try:
                replied_user_id = save[replied_id]
            except Exception as e:
                print(e)   
            try:
                return await app.copy_message(
                    replied_user_id,
                    message.chat.id,
                    message.message_id,
                )
            except Exception as e:
                print(e)

app.run()
