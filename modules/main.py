import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from aiohttp import web

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://text-leech-bot-for-render.onrender.com/")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await asyncio.sleep(3600)  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
    
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
       f"𝐇𝐞𝐥𝐥𝐨 ❤️\n\n◆〓◆ ❖ 𝐖𝐃 𝐙𝐎𝐍𝐄 ❖ ™ ◆〓◆\n\n❈ I Am A Bot For Download Links From Your **.TXT** File And Then Upload That File Om Telegram So Basically If You Want To Use Me First Send Me ⟰ /upload Command And Then Follow Few Steps..", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✜ 𝐉𝐨𝐢𝐧 𝐔𝐩𝐃𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✜" ,url=f"https://t.me/TARGETALLCOURSE") ],
                    [
                    InlineKeyboardButton("✜ CR CHOUDHARY ❤️ ✜" ,url="https://t.me/free_course2_bot") ],
                    [
                    InlineKeyboardButton("🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋" ,url="https://t.me/TARGETALLCOURSE") ]                               
            ]))


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐭 ♦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["upload"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐀 𝐓𝐱𝐭 𝐅𝐢𝐥𝐞 𝐒𝐞𝐧𝐝 𝐇𝐞𝐫𝐞 ⏍')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

path = f"./downloads/{m.chat.id}"

try:
    with open(x, "r") as f:
        content = f.read()
    content = content.split("\n")
    links = []
    for i in content:
        links.append(i.split("://", 1))
    os.remove(x)
except Exception as e:
    await m.reply_text(f"∝ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭.\nError: {str(e)}")
    os.remove(x)
    return

await editable.edit(f"∝ 𝐓𝐨𝐭𝐚𝐥 𝐋𝐢𝐧𝐤 𝐅𝐨𝐮𝐧𝐝: 🔗 **{len(links)}**\n\n𝐒𝐞𝐧𝐝 𝐅𝐫𝐨𝐦 𝐖𝐡𝐞𝐫𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐈𝐧𝐢𝐭𝐚𝐥 𝐢𝐬 **1**")
input0: Message = await bot.listen(editable.chat.id)
raw_text = input0.text
await input0.delete(True)

await editable.edit("∝ 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞")
input1: Message = await bot.listen(editable.chat.id)
raw_text0 = input1.text
await input1.delete(True)

await editable.edit("∝ 𝐄𝐧𝐭𝐞𝐫 𝐄𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧 🎬\n☞ 144,240,360,480,720,1080\nPlease Choose Quality")
input2: Message = await bot.listen(editable.chat.id)
raw_text2 = input2.text
await input2.delete(True)

try:
    if raw_text2 == "144":
        res = "256x144"
    elif raw_text2 == "240":
        res = "426x240"
    elif raw_text2 == "360":
        res = "640x360"
    elif raw_text2 == "480":
        res = "854x480"
    elif raw_text2 == "720":
        res = "1280x720"
    elif raw_text2 == "1080":
        res = "1920x1080" 
    else:
        res = "UN"
except Exception as e:
    res = "UN"
    await m.reply_text(f"∝ 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐪𝐮𝐚𝐥𝐢𝐭𝐲 𝐢𝐬 𝐢𝐧𝐯𝐚𝐥𝐢𝐝. Error: {str(e)}")

await editable.edit("✏️ Now Enter A Caption to add caption on your uploaded file")
input3: Message = await bot.listen(editable.chat.id)
raw_text3 = input3.text
await input3.delete(True)
highlighter = f"️ ⁪⁬⁮⁮⁮"
MR = raw_text3 if raw_text3 != 'Robin' else highlighter

await editable.edit("🌄 Now send the Thumb url\nEg » https://graph.org/file/419c60736fbac058c9e50.jpg\n\n Or if don't want thumbnail send = no")
input6: Message = await bot.listen(editable.chat.id)
raw_text6 = input6.text
await input6.delete(True)
await editable.delete()

thumb = raw_text6
if thumb.startswith("http://") or thumb.startswith("https://"):
    getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
    thumb = "thumb.jpg"
elif thumb.lower() == "no":
    thumb = None
else:
    thumb = None

if len(links) == 1:
    count = 1
else:
    count = int(raw_text)

try:
    for i in range(count - 1, len(links)):
        V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
        url = "https://" + V

        # Handle special cases
        if "visionias" in url:
            async with ClientSession() as session:
                async with session.get(url, headers={'User-Agent': 'Mozilla/5.0'}) as resp:
                    text = await resp.text()
                    url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

        elif 'videos.classplusapp' in url:
            url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'your-token'}).json()['url']

        elif '/master.mpd' in url:
            id = url.split("/")[-2]
            url = f"https://d26g5bnklkwsh4.cloudfront.net/{id}/master.m3u8"

        name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
        name = f'{str(count).zfill(3)}) {name1[:60]}'

        # yt-dlp quality selection
        ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]" if "youtu" in url else f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
        cmd = f'yt-dlp -o "{name}.mp4" "{url}"' if "jw-prod" in url else f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

        # More stylish error handling
        try:
            cc = (
                f"**🎥 Video ID:** `{str(count).zfill(3)}`\n"
                f"**📂 File Name:** `{name}.mkv`\n"
                f"**📚 Batch:** `{raw_text0}`\n\n"
                f"📢 **Join our channel for updates!**"
            )
            cc1 = (
                f"**📁 PDF ID:** `{str(count).zfill(3)}`\n"
                f"**📂 File Name:** `{name}.pdf`\n"
                f"**📚 Batch:** `{raw_text0}`\n\n"
                f"📢 **Join our channel for updates!**"
            )

            buttons = InlineKeyboardMarkup([[InlineKeyboardButton("📢 Join Channel", url="https://t.me/TARGETALLCOURSE")]])

            if "drive" in url:
                try:
                    ka = await helper.download(url, name)
                    copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                    count += 1
                    os.remove(ka)
                    time.sleep(1)
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue
            elif ".pdf" in url:
                try:
                    cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                    download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                    os.system(download_cmd)
                    copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                    count += 1
                    os.remove(f'{name}.pdf')
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue
            else:
                Show = f"❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📝 𝐍𝐚𝐦𝐞 » `{name}\n⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**🔗 𝐔𝐑𝐋 »** `{url}`"
                prog = await m.reply_text(Show)
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await prog.delete(True)
                await helper.send_vid(bot,m, cc, filename, thumb, name, prog)
                count += 1
                time.sleep(1)

        except Exception as e:
            await m.reply_text(
                f"⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐫𝐮𝐩𝐭𝐞𝐝\n{str(e)}\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
            )
            continue

except Exception as e:
    await m.reply_text(f"⌘ 𝐄𝐫𝐫𝐨𝐫 𝐨𝐜𝐜𝐮𝐫𝐞𝐝: {str(e)}")
    
await m.reply_text("✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞!")

print("""
█░█░█ █▀█ █▀█ █▀▄ █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀     ▄▀█ █▀ █░█ █░█ ▀█▀ █▀█ █▀ █░█   ░ █▀▀
▀▄▀▄▀ █▄█ █▄█ █▄▀ █▄▄ █▀▄ █▀█ █▀░ ░█░     █▀█ ▄█ █▀█ █▄█ ░█░ █▄█ ▄█ █▀█   ▄ █▄█""")
print("""✅ 𝐃𝐞𝐩𝐥𝐨𝐲 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅""")
print("""✅ 𝐁𝐨𝐭 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 ✅""")

bot.run()
if __name__ == "__main__":
    asyncio.run(main())
