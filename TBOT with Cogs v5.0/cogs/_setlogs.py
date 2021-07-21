import discord
import sqlite3
import json

from discord.ext import commands

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
    #mod log
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS main(
                guild_id TEXT,
                channel_id TEXT
            )
            ''')

    @commands.command(aliases=['setm', 'smc', 'setmodlog'])
    @commands.has_permissions(administrator=True)
    async def setmodlogchannel(self, ctx, channel: discord.TextChannel):
        db=sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()
        
        if result is None:
            sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)

            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name=f"Succesfully set the log channel to <#{channel.name}>")
            await ctx.send(embed=embed)
        
        elif result is not None:
            sql = ("UPDATE main SET channel_id = ? WHERE channel_id = ?")
            val = (channel.id, ctx.guild.id)
            
            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name=f"Succesfully updated log channel to #{channel.name}")
            await ctx.send(embed=embed)
        
        cursor.execute(sql, val)
        db.commit()

        cursor.close()
        db.close()

        await channel.send("Mod channel set here")
    @setmodlogchannel.error
    async def setmodlogchannel_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `administrator` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def aduitlog(self, ctx, *, args):
        with open("databases/eventlog.json", "r") as f:
                logs = json.load(f)

        if args == "off":
            logs[str(ctx.guild.id)]["log_logs"] = "off"
                
            with open("databases/eventlog.json", "w") as f:
                    json.dump(logs, f)

            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name="Succesfully set leveling off")

            await ctx.send(embed=embed)
            return     

        if args == "on":
            logs[str(ctx.guild.id)]["log_logs"] = "on"

            with open("databases/eventlog.json", "w") as f:
                json.dump(logs, f)

            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name="Succesfully set logs on")
            await ctx.send(embed=embed)

            return

def setup(client):
    client.add_cog(mod(client))