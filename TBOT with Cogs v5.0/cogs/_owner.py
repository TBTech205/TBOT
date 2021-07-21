# packages that are needed
import discord
import asyncio
import os
import traceback

from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    #owner commands
    @commands.command()
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
        await self.client.logout()
    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack permission to use this command as you do not own TBOT")
        else:
            raise error

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f"cogs.{extension}")

        await ctx.send(f"cogs.{extension} has been loaded")
    @load.error
    async def load_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack permission to use this command as you do not own TBOT")
        else:
            raise error

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f"cogs.{extension}")

        await ctx.send(f"cogs.{extension} has been unloaded")
    @unload.error
    async def unload_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack permission to use this command as you do not own TBOT")
        else:
            raise error

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.client.unload_extension(f"cogs.{ext[:-3]}")
                            self.client.load_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )

                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)

        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.client.unload_extension(f"cogs.{ext[:-3]}")
                        self.client.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )

                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)

    @reload.error
    async def reload_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack permission to use this command as you do not own TBOT")
        else:
            raise error

def setup(client):
    client.add_cog(owner(client))