# bot.py
import os
import re

import discord
from dotenv import load_dotenv

def parse_message(message):
    msg_split = message.split(":", 2)
    kakera_type = msg_split[1]
    temp = msg_split[2].split("**")
    temp2 = temp[1].split("+")
    username = temp2[0]
    username = username.strip()
    kakera_value = temp2[1]

    return [kakera_type, kakera_value, username]




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('CHANNEL_ID')
ID = os.getenv('USER_ID')

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_message(message):
    # global str2
    if message.author.id == 432610292342587392:
        x = re.search("^:kakera", message.content)
        if x is not None:
            p_message = parse_message(x.string)
            print(p_message)

client.run(TOKEN)