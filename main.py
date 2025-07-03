import discord
import os
import asyncio
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

SOURCE_CHANNEL_ID = 123456789012345678  # <-- replace this
TARGET_CHANNEL_ID = 876543210987654321  # <-- replace this

@client.event
async def on_ready():
    print(f"🤖 Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == SOURCE_CHANNEL_ID and not message.author.bot:
        target = client.get_channel(TARGET_CHANNEL_ID)
        if target:
            await target.send(f"{message.author.display_name}: {message.content}")

client.run(TOKEN)