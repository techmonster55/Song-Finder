from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app as Bot 
from TamilBots import  LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db


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
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
SOURCE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='about')
        ]]
    )
YOUTUBE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat=""),
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
VSONG_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
LYRICS_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
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
      elif update.data == "help":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
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
