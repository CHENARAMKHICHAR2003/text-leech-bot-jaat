import os
import sys
import time
import asyncio
import requests
from aiohttp import ClientSession, web
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from subprocess import getstatusoutput

# Bot configuration
API_ID = "your_api_id"
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
WEBHOOK = False
PORT = 8080

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
    return web.json_response("https://yourboturl.com/")

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
        f"✨ **Welcome to WD Zone** ✨\n\nI am your download and upload bot. Please use the commands below to interact with me!\n\n"
        f"🛠️ **/upload**: Upload your links\n"
        f"💬 **/help**: Get help on how to use the bot\n"
        f"📣 **/setchannel**: Set a channel for updates\n\n"
        f"➕ **Join the Update Channel** ➕",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🛸 Join Update Channel 🛸", url="https://t.me/TARGETALLCOURSE")],
            [InlineKeyboardButton("💥 Visit My Channel 💥", url="https://t.me/TARGETALLCOURSE")],
            [InlineKeyboardButton("🌟 Follow Me 🌟", url="https://t.me/FREE_COURSE2_BOT")],
            [InlineKeyboardButton("ℹ️ Help", callback_data="help")],
            [InlineKeyboardButton("⚙️ Set Channel", callback_data="setchannel")]
        ])
    )

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("⚠️ Bot Stopped ⚠️", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["upload"]))
async def upload_links(bot: Client, m: Message):
    editable = await m.reply_text('📩 Send me your .TXT file with the download links.')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"
    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = [i.split("://", 1) for i in content]
        os.remove(x)
    except:
        await m.reply_text("❌ Invalid file input. Please send a valid .TXT file.")
        os.remove(x)
        return
    
    await editable.edit(f"✅ Found {len(links)} links in the file. Send the starting index (default is 1).")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("🎯 Send the batch name (Example: 'Course Batch 1').")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit("🔧 Enter video resolution (options: 144, 240, 360, 480, 720, 1080).")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    res = {"144": "256x144", "240": "426x240", "360": "640x360", "480": "854x480", "720": "1280x720", "1080": "1920x1080"}.get(raw_text2, "UN")

    await editable.edit("💬 Enter a caption (or type 'Robin' for default caption).")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter = f"⭐" if raw_text3 == 'Robin' else raw_text3

    await editable.edit("🔑 Send thumbnail URL (or 'no' for none).")
    input6 = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):
            url = "https://" + links[i][1].replace("file/d/", "uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing", "")
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            cc = f"""╭━━━━━━━━━━━━━━━━━━━━━╮
💫 **VIDEO ID** : {str(count).zfill(3)}
╰━━━━━━━━━━━━━━━━━━━━━╮
📁 **TITLE** : {name1} ({res})

📚 **COURSE** : {raw_text0}  
📥 **DOWNLOADED BY** : {raw_text3}

🔗 [**JOIN THE CHANNEL**](https://t.me/TARGETALLCOURSE)
"""
            cc1 = f"""╭━━━━━━━━━━━━━━━━━━━━━╮
💫 **PDF ID** : {str(count).zfill(3)}
╰━━━━━━━━━━━━━━━━━━━━━╮
📁 **TITLE** : {name1}

📚 **COURSE** : {raw_text0}  
📥 **DOWNLOADED BY** : {raw_text3}

🔗 [**JOIN THE CHANNEL**](https://t.me/targetallcourse)
"""

            try:
                # Show download progress (you can replace this with actual download logic)
                Show = f"❊⟱ Downloading ⟱❊ »\n\n📝 Name: {name}\n⌨ Quality: {res}\n\n**🔗 URL: {url}**"
                prog = await m.reply_text(Show)

                # Simulate download (replace with actual download logic)
                filename = await helper.download_video(url, cmd, name)
                await prog.delete(True)
                await helper.send_vid(bot, m, cc, filename, thumb, name, prog)

                count += 1
                time.sleep(1)

            except Exception as e:
                await m.reply_text(f"❌ Download Interrupted: {str(e)}\nName: {name}\nURL: {url}")
                continue

    except Exception as e:
        await m.reply_text(f"❌ Error: {str(e)}")

    await m.reply_text("✅ Download completed successfully.")

@bot.on_message(filters.command(["help"]))
async def help_command(bot: Client, m: Message):
    await m.reply_text(
        "💡 **How to Use the Bot** 💡\n\n"
        "1. Use **/upload** to send a .TXT file with your download links.\n"
        "2. Follow the prompts to choose video resolution, batch name, caption, and thumbnail.\n"
        "3. The bot will download and send the file to your Telegram.\n\n"
        "✨ You can also use **/setchannel** to set a channel for updates."
    )

@bot.on_message(filters.command("setchannel"))
async def set_channel(bot: Client, m: Message):
    user_id = m.chat.id

    # Check if the user already has a channel set
    if user_id in user_channels:
        await m.reply_text(f"✅ You have already set your channel to: {user_channels[user_id]}")
        return

    # Ask the user to send their channel link or username
    await m.reply_text("🔑 Please send me your channel link or username (without @). Example: 'your_channel'.")

    # Wait for the user to input the channel
    user_input = await bot.listen(m.chat.id)

    # Get the input
    channel = user_input.text.strip()

    if not channel:
        await user_input.reply_text("❌ Please provide a valid channel link or username.")
        return

    # Save the user's channel
    user_channels[user_id] = channel
    await user_input.reply_text(f"✅ Your channel has been set to: {channel}")

@bot.on_message(filters.command("getchannel"))
async def get_channel(bot: Client, m: Message):
    user_id = m.chat.id
    if user_id in user_channels:
        await m.reply_text(f"✅ Your set channel is: {user_channels[user_id]}")
    else:
        await m.reply_text("❌ You have not set a channel yet. Use **/setchannel** to set one.")


print("""
███████████████████████████████████████████████
██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
███████████████████████████████████████████████
"""
)
print("✅ Bot is Ready and Running ✅")
bot.run()

if __name__ == "__main__":
    asyncio.run(main())
