# packages that are needed
import discord
import sqlite3
import datetime
import json

from datetime import timedelta, datetime
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("databases/eventlog.json", "r") as f:
            channels = json.load(f)

            channels[str(guild.id)] = {}
            channels[str(guild.id)]["log_channel"] = "None"
            channels[str(guild.id)]["log_logs"] = "off"

        with open("databases/eventlog.json", "w") as f:
            json.dump(channels, f)

#bellow are on_invite events
    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(invite.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={invite.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            invite_embed = discord.Embed(title="Invite Created", color=0xfee75c)

            invite_embed.add_field(name="Creator:", value=f"{invite.inviter.mention}", inline=False)
            invite_embed.add_field(name="Creatorid:", value=f"{invite.inviter.id}", inline=False)
            invite_embed.add_field(name="URL:", value=f"{invite}", inline=False)
            invite_embed.add_field(name="Channel:", value=f"{invite.channel.mention}", inline=False)
            invite_embed.add_field(name="Channel ID:", value=f"{invite.channel.id}", inline=False)

            invite_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=invite_embed)
    
    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(invite.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={invite.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            invite_embed = discord.Embed(title="Invite Deleted", color=0xfee75c)

            invite_embed.add_field(name="Creator:", value=f"N/A", inline=False)
            invite_embed.add_field(name="Creatorid:", value=f"N/A", inline=False)
            invite_embed.add_field(name="URL:", value=f"{invite}", inline=False)
            invite_embed.add_field(name="Channel:", value=f"{invite.channel.mention}", inline=False)
            invite_embed.add_field(name="Channel ID:", value=f"{invite.channel.id}", inline=False)
            
            invite_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=invite_embed)

#bellow are on_member events
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            ban_embed = discord.Embed(title="", color=0xfee75c)

            ban_embed.set_thumbnail(url=user.avatar_url)

            ban_embed.add_field(name="Member banned", value=f"{user.mention} was banned")

            ban_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=ban_embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            unban_embed = discord.Embed(title="", color=0xfee75c)

            unban_embed.set_thumbnail(url=user.avatar_url)

            unban_embed.add_field(name="Member unbanned", value=f"{user.mention} was unbanned")

            unban_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=unban_embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(member.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={member.guild.id}")
            result=cursor.fetchone()
            
            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            member_join_embed = discord.Embed(title="User has joined the server.", color=0xfee75c)

            member_join_embed.add_field(name="Member that has joined the server:", value=f"{member.mention} joined the server", inline=False)
            member_join_embed.add_field(name="Member ID", value=f"{member.id}", inline=False)

            member_join_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=member_join_embed)

            print(f"{member} joined {member.guild}")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(member.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={member.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            member_embed = discord.Embed(title="User has left the server.", color=0xfee75c)

            member_embed.add_field(name="Goodbye:", value=f"{member.mention} left the server", inline=False)
            
            member_embed.set_footer(text=f"Today At {time}")

            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=member_embed)

#bellow are on_message events
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(message.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={message.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            embed = discord.Embed(title="Message deleted", color=0xfee75c)

            embed.add_field(name=f"Message deleted in: ", value=message.channel.mention, inline=False)
            embed.add_field(name=f"Message:", value=message.content, inline=False)

            embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=embed)

#below is none private channels events
    #@commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(channel.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={channel.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            channel_embed = discord.Embed(title="Channel created", color=0xfee75c)

            channel_embed.add_field(name=f"Channel name", value=channel.mention, inline=False)
            channel_embed.add_field(name=f"Channel ID", value=channel.id, inline=False)

            channel_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=channel_embed)
    
    #@commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(channel.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={channel.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            channel_embed = discord.Embed(title="Text channel Deleted", color=0xfee75c)

            channel_embed.add_field(name=f"Channel name", value=channel, inline=False)
            channel_embed.add_field(name=f"Channel ID", value=channel.id, inline=False)

            channel_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=channel_embed)

    #@commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(before.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={before.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            channel_embed = discord.Embed(title="Text channel updated", color=0xfee75c)

            channel_embed.add_field(name=f"Channel name before:", value=before, inline=False)
            channel_embed.add_field(name=f"Channel name after:", value=after, inline=False)

            channel_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=channel_embed)


#bellow are on_channel_pins events
    @commands.Cog.listener()
    async def on_guild_channel_pins_update(self, channel, last_pin):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(channel.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={channel.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            channel_embed = discord.Embed(title="Pinned message", color=0xfee75c)

            channel_embed.add_field(name=f"message pinned in channel:", value=channel.mention, inline=False)
            channel_embed.add_field(name=f"Pined Time", value=last_pin, inline=False)

            channel_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=channel_embed)

#bellow are on_member_update events
    #@commands.Cog.listener()
    async def on_member_update(self, before, after):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(before.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={after.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            member_embed = discord.Embed(title="Member updated", color=0xfee75c)

            member_embed.add_field(name=f"Before:", value=before, inline=False)
            member_embed.add_field(name=f"After:", value=after, inline=False)

            member_embed.set_footer(text=f"Today At {time}")

            channel= self.client.get_channel(id=int(result[0]))
            await channel.send(embed=member_embed)

    #@commands.Cog.listener()
    async def on_user_update(self, before, after):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(after.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={after.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            user_embed = discord.Embed(title="Member updated", color=0xfee75c)
            
            user_embed.add_field(name=f"Before:", value=before, inline=False)
            user_embed.add_field(name=f"After:", value=after, inline=False)

            user_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=user_embed)


#on_guild_update(self, before, after)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(role.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={role.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            role_embed = discord.Embed(title="Role created", color=0xfee75c)

            role_embed.add_field(name=f"Role name:", value=role.mention, inline=False)
            role_embed.add_field(name=f"Role ID:", value=role.id, inline=False)

            role_embed.set_footer(text=f"Today At {time}")

        channel=self.client.get_channel(id=int(result[0]))
        await channel.send(embed=role_embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(role.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={role.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            role_embed = discord.Embed(title="Role deleted", color=0xfee75c)

            role_embed.add_field(name=f"Role name:", value=role, inline=False)
            role_embed.add_field(name=f"Role ID:", value=role.id, inline=False)

            role_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=role_embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(before.guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={before.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            role_embed = discord.Embed(title="Role Updated", color=0xfee75c)

            role_embed.add_field(name=f"Role name before:", value=before, inline=False)
            role_embed.add_field(name=f"Role name after:", value=after.mention, inline=False)

            role_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=role_embed)

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        with open("databases/eventlog.json", "r") as f:
            logs = json.load(f)

        on_off = logs[str(guild.id)]["log_logs"]
    
        if on_off == "off":
            return

        if on_off == "on":
            db= sqlite3.connect("databases/modlogs.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM main WHERE guild_id={before.guild.id}")
            result=cursor.fetchone()

            timestamp = datetime.now()
            time = timestamp.strftime(r"%I:%M %p")

            role_embed = discord.Embed(title="Role Updated", color=0xfee75c)

            role_embed.add_field(name=f"Emoji before:", value=before, inline=False)
            role_embed.add_field(name=f"Emoji after:", value=after, inline=False)

            role_embed.set_footer(text=f"Today At {time}")

            channel=self.client.get_channel(id=int(result[0]))
            await channel.send(embed=role_embed)

#below is private channel events

#on_private_channel_delete(channel)
#on_private_channel_create(channel)
#on_private_channel_update(before, after)
#on_private_channel_pins_update(channel, last_pin)

def setup(client):
   client.add_cog(events(client))