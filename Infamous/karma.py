# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://files.catbox.moe/jvxj93.jpg",
]

HEY_IMG = "https://files.catbox.moe/jvxj93.jpg"

ALIVE_ANIMATION = [
    "https://files.catbox.moe/8mil2n.jpg",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ʜᴇʏ ʙᴀʙʏ, ɪᴍ ʏᴏʀ ғᴏʀɢᴇʀ ..ᴀ ᴘᴏᴡᴇʀғᴜʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍsɴᴛ ʙᴏᴛ ᴡʜᴏ ᴄᴀɴ ʜᴀɴᴅʟᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʟɪᴋᴇ ᴀɴ ᴀɴɢᴇʟ ᴀɴᴅ ʏᴇᴀʜ ɪᴍ ᴛᴏᴏ ʏᴏᴜᴛ ᴍᴏᴍᴍʏ ᴍʏ ʜᴏɴᴇʏ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="𝙎𝙐𝙈𝙈𝙊𝙉 𝙈𝙀⚡",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝙃𝙀𝙇𝙋⚡", callback_data="extra_command_handler"),
    ],
    [
        InlineKeyboardButton(text="𝘿𝙀𝙏𝘼𝙄𝙇𝙎⚡", callback_data="Miko_"),
        InlineKeyboardButton(text="𝙍𝙀𝙋𝙊⚡", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="𝙊𝙒𝙉𝙀𝙍⚡", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="𝙎𝙐𝙈𝙈𝙊𝙉 𝙈𝙀⚡",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏⚡", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="𝙊𝙒𝙉𝙀𝙍⚡", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="𝙐𝙋𝘿𝘼𝙏𝙀𝙎⚡", url="https://t.me/sukunaxsupport"),
        ib(text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏⚡", url="https://t.me/Sukunaxupdatess"),
    ],
    [
        ib(
            text="𝙎𝙐𝙈𝙈𝙊𝙉 𝙈𝙀⚡",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yor Forger* 🫧 [ㅤ](https://files.catbox.moe/jvxj93.jpg)

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
