# bot.py
import os
import re
import gspread

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

gc = gspread.service_account(filename="creds.json")

sh = gc.open("Mudae badge calcs").get_worksheet(1)
name = sh.acell("a2").value
print(name)

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
    global troll_msg
    re_say = re.search("^\\$say", message.content)
    if re_say is not None:
        troll_arr = re_say.string.split(" ", 1)
        troll_msg = troll_arr[1]
    if message.author.id == 432610292342587392:
        x = re.search("^:kakera", message.content)
        if x is not None and x.string != troll_msg:
            p_message = parse_message(x.string)
            print(p_message)

client.run(TOKEN)