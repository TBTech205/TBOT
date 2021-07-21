# packages that are needed for the bot
import discord
import json
import os
import re

from discord.ext import commands

if os.path.exists(os.getcwd() + "/databases/badwords.json"):
    with open("databases/badwords.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"bannedWords": []}
    with open(os.getcwd() + "databases/badwords.json", "w+") as f:
        json.dump(configTemplate, f) 

bannedWords = configData["bannedWords"]

class bannedWord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        #prefix
        try:
            if message.mentions[0] == self.client.user:
                with open("databases/prefixes.json", "r") as f:
                    prefixes = json.load(f)
                pre = prefixes[str(message.guild.id)]
                
                embed = discord.Embed(title="", color=0x5865F2)
        
                embed.add_field(name=f"Hey :wave:", value=f"I'm TBOT\n The prefix on this server is: {pre} \nUse `{pre}help` for a list of commands", inline=False)
        
                await message.channel.send(embed=embed)
        except:
            pass

    #banned words
        if bannedWords != None and (isinstance(message.channel, discord.channel.DMChannel) == False):
            for bannedWord in bannedWords:
                if msg_contains_word(message.content.lower(), bannedWord):
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} your message was removed as it contained a banned word.")

        await self.client.process_commands(message)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addbannedword(self, ctx, word):
        if word.lower() in bannedWords:
            await ctx.send("Already banned")
        else:
            bannedWords.append(word.lower())

            with open("databases/badwords.json", "r+") as f:
                data = json.load(f)
                data["bannedWords"] = bannedWords
                f.seek(0)
                f.write(json.dumps(data))
                f.truncate()

            await ctx.message.delete()
            await ctx.send("Word added to banned words.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removebannedword(self, ctx, word):
        if word.lower() in bannedWords:
            bannedWords.remove(word.lower())

            with open("databases/badwords.json", "r+") as f:
                data = json.load(f)
                data["bannedWords"] = bannedWords
                f.seek(0)
                f.write(json.dumps(data))
                f.truncate()

            await ctx.message.delete()
            await ctx.send("Word remove from banned words.")
        else:
            await ctx.send("Word isn't banned.")

def msg_contains_word(msg, word):
    return re.search(fr'\b({word})\b', msg) is not None

def setup(client):
    client.add_cog(bannedWord(client))