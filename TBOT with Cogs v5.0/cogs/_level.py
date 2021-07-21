import discord
import sqlite3
import json

from discord.ext import commands

con = sqlite3.connect('databases/level.db')
cur = con.cursor()

class level(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("databases/levelconfig.json", "r") as f:
            channels = json.load(f)

            channels[str(guild.id)] = {}
            channels[str(guild.id)]["level_channel"] = "None"
            channels[str(guild.id)]["level_logs"] = "off"

        with open("databases/levelconfig.json", "w") as f:
            json.dump(channels, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot != True:
            try:
                with open("databases/levelconfig.json", "r") as f:
                    logs = json.load(f)

                on_off = logs[str(message.guild.id)]["level_logs"]
            
                if on_off == "off":
                    return

                if on_off == "on":
                    cur.execute(f"SELECT * FROM GUILD_{message.guild.id} WHERE user_id={message.author.id}")
                    result = cur.fetchone()

                    if result[1]==20:
                        channel_database = logs[str(message.guild.id)]["level_channel"]

                        levelup=discord.Embed(title="", color=0x4246C4)

                        levelup.add_field(name="levelup", value=f"{message.author.mention} advanced to lvl {result[2]+1}")

                        channel = self.client.get_channel(id=int(channel_database))
                        await channel.send(embed=levelup)

                        cur.execute(f"UPDATE GUILD_{message.guild.id} SET exp=0, lvl={result[2]+1} WHERE user_id={message.author.id}")
                        con.commit()

                    else:
                        cur.execute(f"UPDATE GUILD_{message.guild.id} SET exp={result[1]+1} WHERE user_id=  {message.author.id}")
                        con.commit()

            except sqlite3.OperationalError:
                pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setlevelchannel(self, ctx, channel: discord.TextChannel=None):
        with open("databases/levelconfig.json", "r") as f:
            channels = json.load(f)

            channels[str(ctx.guild.id)] = {}
            channels[str(ctx.guild.id)]["level_channel"] = f"{channel.id}"
            channels[str(ctx.guild.id)]["level_logs"] = "on"

        with open("databases/levelconfig.json", "w") as f:
            json.dump(channels, f)

        #this send it to the command usage channel
        embed = discord.Embed(color=0x00ff00)
        embed.set_author(name=f"Succesfully set the leveling channel to #{channel.name}")
        await ctx.send(embed=embed)

        # this sends it to the mentioned channel
        embed = discord.Embed(color=0x00ff00)
        embed.set_author(name=f"This channel has been set as the leveling channel")
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def levelconfig(self, ctx, *, args):
        with open("databases/levelconfig.json", "r") as f:
                logs = json.load(f)

        if args == "off":
            logs[str(ctx.guild.id)]["level_logs"] = "off"
                
            with open("databases/levelconfig.json", "w") as f:
                    json.dump(logs, f)

            cur.execute(f'DELETE FROM GUILD_{ctx.guild.id}')
            con.commit()

            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name="Succesfully set leveling off")

            await ctx.send(embed=embed)
            return     

        if args == "on":
            logs[str(ctx.guild.id)]["level_logs"] = "on"
            
            with open("databases/levelconfig.json", "w") as f:
                    json.dump(logs, f)

            cur.execute(f'''CREATE TABLE IF NOT EXISTS GUILD_{ctx.guild.id} (user_id int NOT NULL, exp int DEFAULT 0, lvl int DEFAULT 0) ''')

            for x in ctx.guild.members:
                if x.bot != True:
                    cur.execute(f"INSERT INTO GUILD_{ctx.guild.id} (user_id) VALUES ({x.id})")

            con.commit()

            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name="Succesfully set leveling on")

            await ctx.send(embed=embed)
            return    

    @commands.command(aliases=['xp','rank','lvl', 'level', 'points'])
    async def _rank(self, ctx, user: discord.User = None):
        with open("databases/levelconfig.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(ctx.guild.id)]["level_logs"]
    
        if on_off == "off":
            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name="Database off")

            await ctx.send(embed=embed)
            return

        if on_off == "on":
            if user == None :
                cur.execute(f"SELECT * FROM GUILD_{ctx.guild.id} WHERE user_id={ctx.author.id}")
                result = cur.fetchone()

                xp=discord.Embed(title=f"{ctx.author.display_name}'s Level", color=0x5865F2)

                xp.add_field(name=f"Level: {result[2]}", value=f"\n**XP:** {result[1]}", inline=False)
                    
                await ctx.channel.send(embed=xp)

            else:
                cur.execute(f"SELECT * FROM GUILD_{ctx.guild.id} WHERE user_id={user.id}")
                result = cur.fetchone()

                if result!=None:
                    xp=discord.Embed(title=f"{user.display_name}'s Level", color=0x5865F2)

                    xp.add_field(name=f"Level: {result[2]}", value=f"\n**XP:** {result[1]}", inline=False)

                    await ctx.channel.send(embed=xp)

                else:
                    await ctx.channel.send("Hmm no such user in the db")
                    
def setup(client):
    client.add_cog(level(client))