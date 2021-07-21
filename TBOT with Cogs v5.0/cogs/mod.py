# packages that are needed
import discord
import json
import asyncio
import datetime, time
import aiohttp
import random
import sqlite3

from io import BytesIO
from discord.ext import commands

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global StartTime 
        StartTime = time.time()

    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if amount == 0:
            embed = discord.Embed(color=0xed5757)
            embed.set_author(name="The amount cant be 0!")
            await ctx.send(embed=embed)

            return
        
        if amount < 0:
            embed = discord.Embed(color=0xed5757)
            embed.set_author(name="The amount must be positive!")
                
            await ctx.send(embed=embed)
            return

        if amount > 150:
            embed = discord.Embed(color=0xed5757)
            embed.set_author(name="You cannot delete more then 150 messages!")

            await ctx.send(embed=embed)
            return

        else:
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
            result=cursor.fetchone()

            await ctx.channel.purge(limit=amount + 1)

            clear_embed_channel = discord.Embed(title="**__Clear command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

            clear_embed_channel.set_thumbnail(url=ctx.author.avatar_url)

            clear_embed_channel.add_field(name="**__Amount of messages that i deleted:__**", value=amount, inline=False)
            clear_embed_channel.add_field(name="**__The user that used the command:__**", value=ctx.author.mention, inline=False)

            clear_embed_channel.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=clear_embed_channel, delete_after=5.0)

            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=clear_embed_channel)
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_messages` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #kick commands
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if result is None:
            return

        else:
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
            result=cursor.fetchone()

        if member == ctx.guild.owner:
            kick_embed = discord.Embed(title=f"", color=0xed5757)

            kick_embed.add_field(name="<:no:858652512869810196> You can't kick the owner of this server", value="Error - Undefined")

            await ctx.send(embed=kick_embed)

            return

        if member == ctx.message.author:
            kick_embed = discord.Embed(title="", description="", color=0xed5757)

            kick_embed.add_field(name="<:no:858652512869810196> You can't kick yourself", value="Error - 401", inline=False)

            await ctx.send(embed=kick_embed)
            return

        if member == None:
            kick_embed = discord.Embed(title="", description="", color=0xed5757)

            kick_embed.add_field(name="<:no:858652512869810196> Mention a member that you want to kick", value="Error - 401", inline=False)

            await ctx.send(embed=kick_embed)
            return

        else:
            embed = discord.Embed(title="**__Kick command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

            embed.add_field(name="Member kicked: ", value=member.mention, inline=False)
            embed.add_field(name="Reason: ", value=reason, inline=False)

            await member.kick(reason=reason)
            await ctx.send(embed=embed, delete_after=5.0)

            #mod logs
            embed = discord.Embed(title="**__Kick command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

            embed.add_field(name="Member kicked: ", value=member.mention, inline=False)
            embed.add_field(name="Reason: ", value=reason, inline=False)
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)

            await member.kick(reason=reason)
            await ctx.send(embed=embed, delete_after=5.0)

            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_members` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if result is None:
            return

        else:
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
            result=cursor.fetchone()

        if member == ctx.guild.owner:
            ban_embed = discord.Embed(title=f"", color=0xed5757)

            ban_embed.add_field(name="<:no:858652512869810196> You can't ban the owner of this server", value="Error - Undefined")

            await ctx.send(embed=ban_embed)

            return

        if member == ctx.message.author:
            ban_embed = discord.Embed(title="", description="", color=0xed5757)

            ban_embed.add_field(name="<:no:858652512869810196> You can't ban yourself", value="Error - 401", inline=False)

            await ctx.send(embed=ban_embed)

            return

        if member == None:
            ban_embed = discord.Embed(title="", description="", color=0xed5757)

            ban_embed.add_field(name="<:no:858652512869810196> Mention a member that you want to ban", value="Error - 401", inline=False)

            await ctx.send(embed=ban_embed)
                
            return

        else:
            ban_embed = discord.Embed(title="**__I succesfully banned someone!__**", description="<:yes:858799280998449152>", color=0x57f287)

            ban_embed.set_thumbnail(url=ctx.author.avatar_url)

            ban_embed.add_field(name="**__The person that i banned:__**", value=member.mention, inline=False)
            ban_embed.add_field(name=f"**__The reason why {member.name} got banned:__**", value=reason, inline=False)
            ban_embed.add_field(name=f"**__The user that banned__** {member.name}", value=ctx.author.mention, inline=False)
    
            await member.ban(reason=reason)
            await ctx.send(embed=ban_embed, delete_after=5.0)

            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=ban_embed)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `ban_memers` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if result is None:
            return

        else:
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
            result=cursor.fetchone()

        embed = discord.Embed(title="**__I unbanned someone succesfully__**", description=":Animated_Checkmark:", color=0x57f287)

        embed.add_field(name="**__The user that i unbanned:__**", value=user.mention, inline=False)

        embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.guild.unban(user=user)
        await ctx.send(embed=embed, delete_after=5.0)
    
        channel= self.client.get_channel(id=int(result[0]))
        await channel.send(embed=embed)
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `ban_memers` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #mute command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, *, reason=None):
        db=sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if result is None:
            return

        else:
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
            result=cursor.fetchone()

        if member == ctx.guild.owner:
            mute_embed = discord.Embed(title=f"", color=0xed5757)

            mute_embed.add_field(name="<:no:858652512869810196> You can't mute the owner of this server", value="Error - Undefined")

            await ctx.send(embed=mute_embed)

            return

        if member == ctx.message.author:
            mute_embed = discord.Embed(title="", color=0xed5757)
          
            mute_embed.add_field(name="<:no:858652512869810196> You can't mute yourself", value="Error - 401")
          
            await ctx.send(embed=mute_embed)

            return

        if member == None:
            mute_embed = discord.Embed(title="", color=0xed5757)
          
            mute_embed.add_field(name="<:no:858652512869810196> Mention a member that you want to mute", value="Error - 401")
          
            await ctx.send(embed=mute_embed)
            return
  
        else:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

            if not mutedRole:
                mutedRole = await ctx.guild.create_role(name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
        
        await member.add_roles(mutedRole, reason=reason)

        mute_embed = discord.Embed(title="**__I have muted someone succesfully!__**", description="<:yes:858799280998449152>", color=0x57f287)

        mute_embed.set_thumbnail(url=member.avatar_url)

        mute_embed.add_field(name="**__The person that i muted:__**", value=member.mention, inline=False)
        mute_embed.add_field(name=f"**__The reason why {member.name} got muted:__**", value=reason, inline=False)
        mute_embed.add_field(name=f"**__The user that muted {member.name}:__**", value=ctx.author.mention, inline=False)

        mute_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=mute_embed, delete_after=5.0)

        channel= self.client.get_channel(id=int(result[0]))
        await channel.send(embed=mute_embed)
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_members` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #unmute command
    @commands.command()
    @commands.has_permissions(kick_members=True)   
    async def unmute(self, ctx, member: discord.Member=None):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if result is None:
            return

        else:
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
            result=cursor.fetchone()

        if member == None:
            unmute_embed = discord.Embed(title="", color=0xed5757)
          
            unmute_embed.add_field(name="<:no:858652512869810196> Mention a member that you want to unmute", value="Error - 401")
          
            await ctx.send(embed=unmute_embed)
            return

        else:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

            await member.remove_roles(mutedRole)

            unmute_embed = discord.Embed(title="**__I unmuted someone succesfully:__**", description="<:yes:858799280998449152>", color=0x57f287)

            unmute_embed.set_thumbnail(url=member.avatar_url)

            unmute_embed.add_field(name="**__The user that i unmuted__**", value=member.mention, inline=False)
            unmute_embed.add_field(name=f"**__the person that unmuted {member.name}:__**", value=ctx.author.mention, inline=False)

            unmute_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=unmute_embed, delete_after=5.0)
            
            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=unmute_embed)
            
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_members` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #tempmute command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member: discord.Member,time):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        muted_role=discord.utils.get(ctx.guild.roles, name="Muted")

        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute= int(time[0]) * time_convert[time[-1]]

        if member == None:
            mute_embed = discord.Embed(title="", color=0xed5757)
          
            mute_embed.add_field(name="<:no:858652512869810196> Mention a member that you want to tempmute", value="Error - 401")
          
            await ctx.send(embed=mute_embed)
            return

        await member.add_roles(muted_role)

        embed = discord.Embed(title="**__I temporary muted someone succesfully:__**", description="<:yes:858799280998449152>", color=discord.Color.green())

        embed.add_field(name="**__The user that i temporary muted__**", value=f"{member.display_name} muted successfuly for: `{time}`", inline=False)
    
        embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
    
        await ctx.send(embed=embed, delete_after=10.0)
        
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)
        
        channel= self.client.get_channel(id=int(result[0]))
        await channel.send(embed=embed)

    @tempmute.error
    async def tempmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_members` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #slowmode command
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds=None):
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        if seconds == None:
            slowmode_embed = discord.Embed(title="**__There is an error!__**", description=":negative_squared_cross_mark:", color=0xed5757)

            slowmode_embed.add_field(name="<:no:858652512869810196> You forgat to put an amount of seconds!", value="Error - 401", inline=False)

            await ctx.send(embed=slowmode_embed)

            return
        else:
            await ctx.channel.edit(slowmode_delay=seconds)

            slowmode_embed = discord.Embed(title="**__Slowmode command succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

            slowmode_embed.set_thumbnail(url=ctx.author.avatar_url)

            slowmode_embed.add_field(name="**__Amount of seconds slowmode:__**", value=seconds, inline=False)
            slowmode_embed.add_field(name="**__The user the used the command:__**", value=ctx.author.mention, inline=False)

            slowmode_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=slowmode_embed, delete_after=5.0)
            
            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=slowmode_embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #warn command
    @commands.command()
    @commands.has_permissions(kick_members=True)    
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        await open_account(member)
        user = member
        users = await get_warnings_data()

        warn = 1
        
        users[str(user.id)]["warnings"] += warn
        users[str(user.id)]["reasons"] += f" {reason} \n"

        with open("json/warnings.json","w") as f:
            json.dump(users,f)

        if member == ctx.guild.owner:
            mute_embed = discord.Embed(title=f"", color=0xed5757)

            mute_embed.add_field(name="<:no:858652512869810196> You can't warn the owner of this server", value="Error - Undefined")

            await ctx.send(embed=mute_embed)

            return

        if member == ctx.message.author:
            mute_embed = discord.Embed(title="", color=0xed5757)
          
            mute_embed.add_field(name="<:no:858652512869810196> You can't warn yourself", value="Error - 401")
          
            await ctx.send(embed=mute_embed)

            return

        if member == None:
            mute_embed = discord.Embed(title="", color=0xed5757)
          
            mute_embed.add_field(name="<:no:858652512869810196> Mention a member that you want to warn", value="Error - 401")
          
            await ctx.send(embed=mute_embed)
            return

        #send this channel that the command was in
        warn_embed = discord.Embed(title=f"{member} has been warned", description=f"Reason: {reason}", color=0xadd8e6)

        warn_embed.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=warn_embed)
        await member.send(embed=warn_embed)

        #send in a log channel
        db= sqlite3.connect("databases/modlogs.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={ctx.guild.id}")
        result=cursor.fetchone()

        warn_embed = discord.Embed(title=f"[WARN] {member}", color=0x57f287)

        warn_embed.add_field(name=f"Reason", value=f"{reason}", inline=False)
        warn_embed.add_field(name=f"User", value=f"{member.mention}", inline=False)
        warn_embed.add_field(name=f"Moderator", value=f"{ctx.author.mention}", inline=False)
        
        

        channel= self.client.get_channel(id=int(result[0]))
        await channel.send(embed=warn_embed)
    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0x57f287)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_memers` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #warnings command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warnings(self, ctx, member: discord.Member):
        await open_account(member)
        user = member
        users = await get_warnings_data()

        warnings_amount = users[str(user.id)]["warnings"]
        reasons = users[str(user.id)]["reasons"]

        if warnings_amount == 0:
            warn=discord.Embed(color=0x7289da)
            
            warn.add_field(name="This user has no warnings", value="Error - Undefined")

            await ctx.send(embed=warn)

        else: 
            warning_embed = discord.Embed(title=f"{member}'s warnings:", color=0x57f287)

            warning_embed.set_thumbnail(url=member.avatar_url)

            warning_embed.add_field(name="**__Warnings:__**", value=warnings_amount, inline=True)
            warning_embed.add_field(name="**__Reasons:__**", value=reasons, inline=True)

            await ctx.send(embed=warning_embed)
            
    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_memers` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #warn command
    @commands.command()
    @commands.has_permissions(kick_members=True)    
    async def clearwarn(self, ctx, member: discord.Member):
        await open_account(member)
        user = member
        users = await get_warnings_data()

        warn = 1
        users[str(user.id)]["warnings"] -= warn

        with open("json/warnings.json","w") as f:
            json.dump(users,f)

        warn_embed = discord.Embed(title=f"{member}'s warnings:", color=0x57f287)

        warn_embed.set_thumbnail(url=member.avatar_url)

        warn_embed.add_field(name=f"Succesfully removed warn from {member}", value=f"\uFEFF")

        await ctx.send(embed=warn_embed)
    @clearwarn.error
    async def clearwarn_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `kick_memers` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    #poll command 
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, *, message):
        embed = discord.Embed(title="POLL", description=f"{message}")
        msg=await ctx.channel.send(embed=embed)

        await msg.add_reaction('✅')
        await msg.add_reaction('❎')
    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_messages` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def giveaway(self, ctx, mins : int, * , prize: str):
        embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

        end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

        embed.add_field(name = "Ends At:", value = f"{end} UTC")

        embed.set_footer(text = f"Ends {mins} mintues from now!")

        my_msg = await ctx.send(embed = embed)

        await my_msg.add_reaction("🎉")
        await asyncio.sleep(mins*60)
        new_msg = await ctx.channel.fetch_message(my_msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        await ctx.send(f"Congratulations! {winner.mention} won `{prize}`!")
    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def changenick(self, ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)
        
        nick_embed = discord.Embed(title="**__I have change someone kickname succesfully!__**", description="<:yes:858799280998449152>", color=0xed5757)

        nick_embed.set_thumbnail(url=member.avatar_url)

        nick_embed.add_field(name="**__The person that i changed nickname for:__**", value=member.mention, inline=False)

        nick_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=nick_embed)
    @changenick.error
    async def changenick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_nickname` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error
    
    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def clearnick(self, ctx):
        await ctx.author.edit(nick=ctx.author.name)
        
        nick_embed = discord.Embed(title="**__I have change someone kickname succesfully!__**", description="<:yes:858799280998449152>", color=0x57f287)

        nick_embed.set_thumbnail(url=ctx.author.avatar_url)

        nick_embed.add_field(name="**__The person that i changed nickname for:__**", value=ctx.author.mention)
        nick_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=nick_embed)
    @clearnick.error
    async def clearnick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack `manage_nicknames` permission.")
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, *, name):
        guild = ctx.guild
        await guild.create_role(name=name)
            
        role_embed = discord.Embed(title="**__I have created a role succesfully!__**", description="<:yes:858799280998449152>", color=0x57f287)

        role_embed.add_field(name="**__The role i have created:__**", value=name, inline=False)

        role_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=role_embed)
    @createrole.error
    async def createrole_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_nickname` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def deleterole(self, ctx, *, role: discord.Role):
        guild = ctx.guild
        await guild.create_role(name=role)
            
        role_embed = discord.Embed(title="**__I have deleted a role succesfully!__**", description="<:yes:858799280998449152>", color=0x57f287)

        role_embed.add_field(name="**__The role i have deleted:__**", value=role, inline=False)

        role_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=role_embed)
    @deleterole.error
    async def deleterole_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_roles` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command(aliases=["giverole"])
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user : discord.Member, *, role : discord.Role):
        if role.position > ctx.author.top_role.position:
            await ctx.send('**:x: | That role is above your top role!**')
            return 

        if role in user.roles:
            await ctx.send("you have this role")

        else:
            await user.add_roles(role)
            await ctx.send(f"Added `{role}` to {user.mention}")
            print(f"Role added to {user}")

        role_embed = discord.Embed(title="**__I have added a role to a member succesfully!__**", description="<:yes:858799280998449152>", color=0x57f287)

        role_embed.add_field(name="**__The person that i added the role to:__**", value=user.mention, inline=False)
        role_embed.add_field(name="**__The role i added to the member:__**", value=role, inline=False)

        role_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_roles` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command(aliases=["takerole"])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user : discord.Member, *, role : discord.Role):
        if role.position > ctx.author.top_role.position:
            return
        await ctx.send('**:x: | That role is above your top role!**')

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"Removed `{role}` from {user.mention}")
            print(f"Role removed from {user}")
            
            return

        role_embed = discord.Embed(title="**__I have removed a role from a member succesfully!__**", description="<:yes:858799280998449152>", color=0x57f287)

        role_embed.add_field(name="**__The person that i removed the role from:__**", value=user.mention, inline=False)
        role_embed.add_field(name="**__The role i removed from the member:__**", value=role, inline=False)

        role_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_roles` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def createchannel(self, ctx, *, channel):
        guild = ctx.guild

        embed = discord.Embed(title="**__create channel command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x5865F2)

        embed.add_field(name="The channel i have made", value=f"`#{channel}`")

        await guild.create_text_channel(name=f"{channel}")
        await ctx.send(embed=embed)
    @createchannel.error
    async def createchannel_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def deletechannel(self, ctx, channel: discord.TextChannel):
        embed = discord.Embed(title="**__Delete channel command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

        embed.add_field(name="The channel i have deleted", value=f"Channel: `#{channel}`")

        embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await channel.delete()
        await ctx.send(embed=embed)
    @deletechannel.error
    async def deletechannel_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def createcategory(self, ctx, *, name):
        embed = discord.Embed(title="**__create category command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

        embed.add_field(name="The category i have made", value=f"`{name}`")

        await ctx.guild.create_category(name=f"{name}")
        await ctx.send(embed=embed)
    @createcategory.error
    async def createcategory_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def deletecategory(self, ctx, *, category: discord.CategoryChannel):
        embed = discord.Embed(title="**__create category command is succesfully used!__**", description="<:yes:858799280998449152>", color=0x57f287)

        embed.add_field(name="The category i have deleted", value=f"`{category}`")

        await category.delete()
        await ctx.send(embed=embed)
    @deletecategory.error
    async def deletecategory_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        await ctx.send(ctx.channel.mention + " Is now in lockdown!")
    @lockdown.error
    async def lockdown_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=True)
        await ctx.send(ctx.channel.mention + " Has been unlocked!")
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions()
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-StartTime))))
        
        embed = discord.Embed(colour=0x5865f2)
        embed.add_field(name="Uptime", value=uptime)
        await ctx.send(embed=embed)

    @uptime.error
    async def uptime_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `administrator` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, *, args):
        with open("databases/prefixes.json", "r") as f:
            system = json.load(f)

        system[str(ctx.guild.id)] = args

        with open("databases/prefixes.json", "w") as f:
            json.dump(system,f)

        embed = discord.Embed(color=0x00ff00)
        embed.set_author(name=f"Succesfully set the prefix to {args}")
        await ctx.send(embed=embed)

    @changeprefix.error
    async def changeprefix_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `administrator` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error
  
    @commands.command(aliases=["addemoji", "ae", "ce", "steal"])
    @commands.has_permissions(manage_emojis=True)
    async def createemoji(self, ctx, url: str, *, name):
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        await ctx.message.delete()
                        await ctx.send(f"Successfully created emoji: <:{name}:{emoji.id}>")
                        await ses.close()

                    else:
                        await ctx.send(f'Error when making request | {r.status} response.')
                        await ses.close()
                                    
                except discord.HTTPException:
                    await ctx.send('File size is too big!')
    @createemoji.error
    async def createemoji_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_emojis` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def deleteemoji(self, ctx, emoji: discord.Emoji):
        if ctx.author.guild_permissions.manage_emojis:
            await ctx.send(f'Successfully deleted: {emoji}')
            await emoji.delete()
    @deleteemoji.error
    async def deleteemoji_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_emojis` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def embed(self, ctx, name, *, message):
        embed = discord.Embed(title="", color=0x5865F2)

        embed.set_thumbnail(url=ctx.guild.icon_url)

        embed.add_field(name=f"{str(name)}", value=f"{str(message)}")

        embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.guild.icon_url)
        
        await ctx.send(embed=embed)
    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def apoll(self, ctx, option1: str, option2: str):
        embed = discord.Embed(title="", color=0x5865F2)

        embed.add_field(name=f"poll time", value=f"A) {option1} \nB) {option2}", inline=False)

        embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.guild.icon_url)

        msg=await ctx.channel.send(embed=embed)

        await msg.add_reaction('🅰️')
        await msg.add_reaction('🅱️')
    @apoll.error
    async def apoll_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="<:no:858652512869810196> Missing `manage_channels` permission.", value="Error - 402")

            await ctx.send(embed=error)
        else:
            raise error

    @commands.command(aliases=['cs'])
    @commands.has_permissions(manage_channels=True)
    async def channelstats(self, ctx, channel: discord.TextChannel):
        embed = discord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=0x5865F2)

        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Channel Id", value=channel.id, inline=False)
        embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Channel Position", value=channel.position, inline=False)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="Channel is news?", value=channel.is_news(), inline=False)
        embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=False)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def roleinfo(self, ctx, role : discord.Role):
        embed = discord.Embed(title="", color=0x5865f2)

        embed.set_thumbnail(url=ctx.guild.icon_url)

        embed.add_field(name=f"Role Name:", value=f"`{role}`", inline=False)
        embed.add_field(name=f"Role ID:", value=f"`{role.id}`", inline=True)
        embed.add_field(name=f"Role Mention:", value=f"{role.mention}", inline=False)
        embed.add_field(name=f"Role Permissions:", value=f"`Available Soon`", inline=False)
        embed.add_field(name=f"Role Creation Date:", value=f"`Available Soon`", inline=False)


        embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.guild.icon_url)

        await ctx.send(embed=embed)


async def open_account(user):
    users = await get_warnings_data()
    with open("json/warnings.json","r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["warnings"] = 0
        users[str(user.id)]["reasons"] = ""

    with open("json/warnings.json","w") as f:
        json.dump(users,f)
    return True

async def get_warnings_data():
    with open("json/warnings.json","r") as f:
        users = json.load(f)
    
    return users

async def update_warnings(user, change= 0, mode = "warnings"):
    users = await get_warnings_data()
    users[str(user.id)][mode] += change

    with open("warnings.json","w") as f:
        json.dump(users,f)
    reasons = [users[str(user.id)]["warnings"], users[str(user.id)]["reasons"]]
    return reasons


def setup(client):
  client.add_cog(mod(client))