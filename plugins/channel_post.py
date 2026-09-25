# Don't Remove Credit
# Made by @MrYKTG https://github.com/MrYKTG
# @mrxeontg @xeonbotz
# Ask Doubt on telegram @Mrxeontg
# Copyright (c) 2026 XeonBotz
# All Rights Reserved.

# channel_post.py — attaches a PERMANENT website share link to posts

from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helper.helper_func import encode, build_permanent_link


@Client.on_message(filters.channel & filters.incoming)
async def new_post(client: Client, message: Message):
    main_channel = getattr(client, "db_channel_id", client.db)

    if await client.mongodb.is_multi_db_enabled():
        extra_channels = await client.mongodb.get_db_channels()
        all_channels = [main_channel] + extra_channels
    else:
        all_channels = [main_channel]

    if message.chat.id not in all_channels:
        return
    if client.disable_btn:
        return

    # Permanent file token (never expires, lives in MongoDB)
    try:
        token = await client.mongodb.create_file_token(message.chat.id, message.id)
    except Exception:
        token = await encode(f"get-{message.id * abs(message.chat.id)}")

    # Bot-ban-proof share URL (reads config.GATEWAY_BASE_URL)
    permanent_url = build_permanent_link(token, bot_username=client.username)

    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            "🔁 Share URL",
            url=f"https://telegram.me/share/url?url={permanent_url}",
        )
    ]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
