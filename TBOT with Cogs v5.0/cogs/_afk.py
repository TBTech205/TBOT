# packages that are needed
import discord
import json

from discord.ext import commands

class AFK(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("json/afk.json", "r") as f:
            afk = json.load(f)

        await update_data(afk, member)

        with open("json/afk.json", "w") as f:
            json.dump(afk, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        with open("json/afk.json", "r") as f:
            afk = json.load(f)
        
        #mention a member
        for x in message.mentions:
            if afk[f"{x.id}"]["AFK"] == "True":

                reason1 = afk[f"{x.id}"]["Reason"]

                afk_mention= discord.Embed(color=0x5865f2, timestamp=message.created_at)

                afk_mention.set_thumbnail(url=x.avatar_url)
            
                afk_mention.add_field(name="AFK", value=f"{x.mention} is AFK \n**Reason:** {reason1}", inline=False)
            
                afk_mention.set_footer(icon_url=message.author.avatar_url, text=f" |   {message.author.name}")

                await message.channel.send(embed=afk_mention)
            
            if afk[f"{x.id}"]["AFK"] == "False":
                return
    
    @commands.command()
    @commands.cooldown(rate=1, per=120.0, type=commands.BucketType.user)
    async def afk(self, ctx, *, reason=None):
        with open("json/afk.json", "r") as f:
            afk = json.load(f)

        if afk[f"{ctx.author.id}"]["AFK"] == "True": #Gone afk
            reason1 = afk[f"{ctx.author.id}"]["Reason"] = f"{reason}"

            embed= discord.Embed(color=0x5865f2, timestamp=ctx.message.created_at)
            
            embed.add_field(name="AFK", value=f"{ctx.author.mention} is AFK \n**Reason:** {reason1}", inline=False)
            
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f" |   {ctx.author.name}")

            await ctx.channel.send(embed=embed)

            await ctx.author.edit(nick=f"[AFK] | {ctx.author.display_name}")

        else: # not afk
            embed= discord.Embed(color=0x5865f2, timestamp=ctx.message.created_at)
            
            embed.add_field(name="AFK", value=f"Welcome back {ctx.author.mention}", inline=False)
            
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f" |   {ctx.author.name}")

            await ctx.channel.send(embed=embed)
                
            afk[f"{ctx.author.id}"]["AFK"] = "False"
            afk[f"{ctx.author.id}"]["Reason"] = "None"

            await ctx.author.edit(nick=f"{ctx.author.display_name[8:]}")
        
        with open("json/afk.json", "w") as f:
            json.dump(afk, f)

async def update_data(afk, user):
    if not f"{user.id}" in afk:
        afk[f"{user.id}"] = {}
        afk[f"{user.id}"]["AFK"] = "False"
        afk[f"{user.id}"]["Reason"] = "None"

def setup(client):
    client.add_cog(AFK(client))