import random
import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

MISHI = [
"https://telegra.ph/file/81aa2cd542ffe2beca305.jpg",
"https://telegra.ph/file/3fbc8004d3d46bf37ae8a.jpg",
"https://telegra.ph/file/e18b44b1a24feadcc67ce.jpg",
"https://telegra.ph/file/3ed786ad4494b5474594a.jpg",
"https://telegra.ph/file/b96d9b78484bbb7e60b17.jpg",
"https://telegra.ph/file/ea16aa7f31ddea6160c35.jpg",
"https://telegra.ph/file/8a7bfd8be8dcc506b1ed8.jpg",
"https://telegra.ph/file/e680fb684eda5320f139b.jpg",
"https://telegra.ph/file/093ddc7abc382d7088bb2.jpg",
"https://telegra.ph/file/cb601b52914fd7afc5e97.jpg",
"https://telegra.ph/file/4fb9db7007e5bebdde78c.jpg",
"https://telegra.ph/file/98ca2a134994684d979d4.jpg",
"https://telegra.ph/file/473605b2bb418f986352c.jpg",
"https://graph.org/file/8dcccaaa09c3ec38d9c75.jpg",
"https://graph.org/file/74d2385efc329c13c11e9.jpg",
"https://graph.org/file/d818146f35f6a439a7a7f.jpg",
"https://graph.org/file/d1d68eaaa8aecc68f8387.jpg",
"https://graph.org/file/257fe1ec8828b836c70f7.jpg",
"https://graph.org/file/8b044edab3d3173544439.jpg",
"https://graph.org/file/8ed87bfd7c0b3dbdd1bf5.jpg",
"https://graph.org/file/1a33887db1a3b5dee1b0a.jpg",
"https://graph.org/file/04ea07e42660988229834.jpg",
"https://graph.org/file/abb6b4bb00e2751bc9f54.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="▪️ᴜᴘᴅᴀᴛᴇ▪️", url=f"https://t.me/SHIVANSH474"),
        InlineKeyboardButton(text="▪️ꜱᴜᴘᴘᴏʀᴛ▪️", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="🔸ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ🔸",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("🤍")
    await asyncio.sleep(0.2)
    await accha.edit("🖤")
    await asyncio.sleep(0.1)
    await accha.edit("🧡")
    await asyncio.sleep(0.1)
    await accha.edit("💻")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        random.choice(MISHI),
        caption=f"""**ꕤ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}](f"t.me/{BOT_USERNAME}") ꕤ**\n\nꕤ **ʟɪʙʀᴀʀʏ ➛** `{lver}`\nꕤ **ᴛᴇʟᴇᴛʜᴏɴ ➛** `{tver}`\nꕤ **ᴘʏʀᴏɢʀᴀᴍ ➛** `{pver}`\nꕤ **ᴘʏᴛʜᴏɴ ➛** `{pyver()}`\n\nꕤ **ᴍᴀᴅᴇ ʙʏ ➛** [sʜɪᴠᴀɴsʜ-xᴅ](tg://user?id={OWNER_ID})""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
    
__mod_name__ = "ᴀʟɪᴠᴇ"
__help__ = """
 ❖ /alive ➛ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs.
 ❖ /ping ➛ ᴄʜᴋ ᴘɪɴɢ sᴛᴀᴛᴜs.
 ❖ /pingall ➛ ᴄʜᴋ ᴘɪɴɢ sᴛᴀᴛᴜs ᴏғ ᴀʟʟ ᴍᴏᴅᴜʟᴇs.
 """
    
