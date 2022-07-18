from pyrogram import filters, Client
from pyrogram.types import Message
from config import bot
from API.gspread import requestmangaapi as gsapi


class request:
    @bot.on_message(filters=filters.command(['mrequest']))
    async def on_mrequest(client: Client, message: Message):
        if message.text == "/mrequest":
            await bot.send_message(
                chat_id=message.chat.id,
                text="Command must be used like this:\n/mrequest -manga_name-",
            )

        elif '/mrequest' in message.text:
            # Calling gspread function to write request in gspread

            manga_name = message.text.split()
            manga_name.pop(0)
            manga_name = "".join(manga_name)

            first_name = message.from_user.first_name
            username = message.from_user.username

            gsapi.add_manganame_sheet1(manga_name, first_name, username)

            await bot.send_photo(
                chat_id=message.chat.id,
                caption="Your request has been recorded in our list! We might get back to you soon if we face any issues",
                photo='https://telegra.ph/file/12a63ccae479fc82fcc6e.jpg'
            )


    @bot.on_message(filters=filters.command(['crequest']))
    async def on_crequest(client: Client, message: Message):
        if message.text == "/crequest":
            await bot.send_message(
                chat_id=message.chat.id,
                text="Command must be used like this:\n/crequest -manga_url-, -channel-id-",
            )

        elif '/crequest' in message.text:
            # Calling gspread function to write request in gspread

            info = message.text.split()
            info.pop(0)
            manga_url = info[0]
            channel_id = info[1]

            first_name = message.from_user.first_name
            username = message.from_user.username

            gsapi.add_request_info_sheet2(manga_url, channel_id, first_name, username)

            await bot.send_photo(
                chat_id=message.chat.id,
                caption="Your request has been recorded in our list! We might get back to you soon if we face any issues",
                photo='https://telegra.ph/file/12a63ccae479fc82fcc6e.jpg'
            )