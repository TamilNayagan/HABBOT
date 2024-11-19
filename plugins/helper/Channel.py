import asyncio
from pyrogram import Client, filters
from pyrogram.types import *

# Replace this with your own channel ID
CHANNEL_ID = -1002460385906  

@Client.on_message(filters.channel & filters.media)
async def add_button(client, message):
    if message.chat.id == CHANNEL_ID:
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔰𝐊𝐌𝐒 𝐌𝐎𝐕𝐈𝐄𝐒 𝐒𝐄𝐀𝐑𝐂𝐇 🔎🔰", url="https://t.me/+J5zlO5boIu9mZGY1")]]
        )
        
        try:
            # Try to add the button to the message
            await message.edit_reply_markup(reply_markup=button)
            await asyncio.sleep(0.5)  # Small delay to handle rapid messages
        except Exception as e:
            print(f"Failed to add button: {e}")
