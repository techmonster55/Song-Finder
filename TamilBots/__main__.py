import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, InputUserDeactivated+

from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from config import FORCE_SUB_CHANNEL, ADMINS
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app as Bot 
from TamilBots import  LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db
from bot import Bot
from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID
from helper_func import subscribed, get_messages

START_TEXT = """ Hai {}, 
Iam a song download Bot 🙂
"""

CMDS_TEXT = """
Hey {} This are this bots power🙂
"""

ABOUT_TEXT = """
Aʙᴏᴜᴛ Mᴇ
╭──[ 🔅 Rᴇᴇʟᴏᴀᴅ Mᴇᴅɪᴀ 🔅 ]───⍟
│
├🔹Dᴇᴠᴇʟᴏᴘᴇʀ : [Nᴏʙᴏᴅʏ](https://t.me/n_ob_od_y)
│
├🔹Cʜᴀɴɴᴇʟ : [Rᴇᴇʟᴏᴀᴅ Mᴇᴅɪᴀ](https://t.me/ReeloadMedia)
│
├🔸Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : [RMCʜᴀᴛs](https://t.me/ReeloadMediaChats)
│
╰─────────[ 😎 ]────────⍟
"""
MUSIC = """ **🎧MUSIC**
You can also use this feature in group too
➩ /music <songname> or /song <songname> artist(optional)>: uploads the song in it's best quality available
You can also use these commands
"""
 
  
LYRICS = """ **🎶LYRICS🎶**
You can also use this feature in group too
➩ /lyrics <songname>: uploads the lyrics of song
"""

YOUTUBE = """  **📽️YOUTUBE📽️**
you can also use inline for search YouTube video or song
"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support📕', url=f"https://telegram.me/ReeloadMedia"), 
        InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat="")
        ],[
        InlineKeyboardButton(text="➕⚡Add ME TO YOUR GROUP⚡➕", url="t.me/RMSongsbot?startgroup=true"), 
        ],[     
        InlineKeyboardButton('HELPℹ️', callback_data ='cmds'),        
        InlineKeyboardButton('ABOUT😁', callback_data='about')        
        ]]
    )
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎧MUSIC🎧', callback_data='song'),        
        ],[
        InlineKeyboardButton('🎶LYRICS🎶', callback_data='lyrics'),
        InlineKeyboardButton('📽️YOUTUBE📽️', callback_data='youtube')
        ],[
        InlineKeyboardButton('🏠 Home', callback_data='home'),            
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME🏡', callback_data='home'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )
MUSIC_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='cmds')
        ]]
    )
SOURCE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='cmds')
        ]]
    )
YOUTUBE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat=""),
            InlineKeyboardButton('👩‍🦯 Back', callback_data='cmds')
        ]]
    )
VSONG_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='cmds')
        ]]
    )
LYRICS_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='cmds')
        ]]
    )

async def is_subscribed(filter, client, update):
    if not FORCE_SUB_CHANNEL:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True
@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text)>7:

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )
     
     
     
@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT.format(update.from_user.mention),
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "song":
        await update.message.edit_text(
            text=MUSIC,
            reply_markup=MUSIC_BUTTON,
            disable_web_page_preview=True
        )    
    elif update.data == "lyrics":
        await update.message.edit_text(
            text=LYRICS,
            reply_markup=LYRICS_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "youtube":
        await update.message.edit_text(
            text=YOUTUBE,
            reply_markup=YOUTUBE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()




        
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):    
    await update.reply_video(
        video="https://drive.google.com/uc?export=download&id=1VIGuX12MHTLhK3lyl2QSeTTxYsn6xJ34",
        caption=START_TEXT.format(update.from_user.mention),            
        reply_markup=START_BUTTONS
    )

@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_video(
        video="https://drive.google.com/uc?export=download&id=1VIGuX12MHTLhK3lyl2QSeTTxYsn6xJ34",
        caption=ABOUT_TEXT,        
        reply_markup=ABOUT_BUTTONS
    )

OWNER_ID.append(1257860541)
Bot.start()
LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()

subscribed = filters.create(is_subscribed)

Bot().run()
