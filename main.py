from pyrogram import Client
from config import API_ID, API_HASH, SESSION_STRING

app = Client(
    session_name=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message()
async def hello(client, message):
    if message.text == "/ping":
        await message.reply("Bot aktivdir!")

app.run()
