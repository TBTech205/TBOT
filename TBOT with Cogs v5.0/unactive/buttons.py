import discord

from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

client = commands.Bot(command_prefix = "!", help_command=None)
ddb=DiscordComponents(client)

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def button(self, ctx):
        content= discord.Embed(title="", color=0x4246C4)
        content.add_field(name="Button", value="Press the button", inline=False),
        await ctx.send(
            embed=content,
            components = [
                Button(style=ButtonStyle.red, label = "WOW Button")
            ]
        )

        interaction = await self.client.wait_for("button_click")
        await interaction.message.channel.send(
            type=InteractionType.ChannelMessageWithSource,
            content = "you clicked me"
        )

def setup(client):
    client.add_cog(misc(client))