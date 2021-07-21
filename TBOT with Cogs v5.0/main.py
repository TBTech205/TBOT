# packages that are needed for the bot
import discord
import json
import asyncio
import os
import re

from discord.ext import commands
from keep_alive import keep_alive

def get_prefix(client, message):
    with open("databases/prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

intents = discord.Intents().all()
intents.members = True

# saying that client = an bot
client = commands.Bot(command_prefix = get_prefix, intents = intents, case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_guild_join(guild):
    with open("databases/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "!"
    
    with open("databases/prefixes.json", "w") as f:
        json.dump(prefixes,f)




@client.event
async def status_task():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"my prefix"))
    
    await asyncio.sleep(10)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="help"))
    
    await asyncio.sleep(10)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Discord.py"))
    
    await asyncio.sleep(10)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your commands"))
    
    await asyncio.sleep(10)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {str(len(client.guilds))} servers"))

    await asyncio.sleep(10)

    await status_task()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run("ODE4NTg1ODU1ODYxMDYzNjkw.YEaNfA.aYFFgNkxnA3XQGVBkUuYkNlhbOE")