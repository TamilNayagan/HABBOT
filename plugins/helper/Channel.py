import asyncio
from pyrogram import Client, filters
from pyrogram.types import *

# Replace this with your own channel ID
CHANNEL_ID = -1002459409813  

@Client.on_message(filters.channel & filters.media)
async def add_button(client, message):
    if message.chat.id == CHANNEL_ID:
        button = InlineKeyboardMarkup(
            [[
              InlineKeyboardButton("🔰𝗠𝗼𝘃𝗶𝗲 𝗦𝗲𝗮𝗿𝗰𝗵 𝗚𝗿𝗼𝘂𝗽🔰", url="https://t.me/+J5zlO5boIu9mZGY1"),       
           ],[
              InlineKeyboardButton("🎵𝗞𝗮𝘃𝗶𝘁𝗵𝗮𝗶 𝗔𝗻𝗱 𝗠𝘂𝘀𝗶𝗰 𝗦𝗼𝘂𝗹🎵", url="https://whatsapp.com/channel/0029Va5rjzvBVJlCi31Gg90N"))]
        
        try:
            # Try to add the button to the message
            await message.edit_reply_markup(reply_markup=button)
            await asyncio.sleep(0.5)  # Small delay to handle rapid messages
        except Exception as e:
            print(f"Failed to add button: {e}")
