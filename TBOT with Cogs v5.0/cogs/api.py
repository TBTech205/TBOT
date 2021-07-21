# packages that are needed for the bot
import discord
import random
import requests
import json
import giphy_client
import praw
import aiohttp
import urllib.request
import wikipedia

from discord.ext import commands
from giphy_client.rest import ApiException
from aiohttp import request
from googleapiclient.discovery import build

api_key = "AIzaSyDq6WnUWGOUZ9FWhrnADjqkzjOklLCPdf4"

class api(commands.Cog):
    def __init__(self, client):
        self.client = client

    #hug command
    #@commands.command()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def hug(self, ctx):
        api_key = "E37VOBn75rgJsyVkRJI43esG28ILDawy"
        api_instance = giphy_client.DefaultApi()
        keyword = "anime hug"

        try:
            api_responce = api_instance.gifs_search_get(api_key, keyword , limit=5, rating="g")
            lst = list(api_responce.data)
            giff = random.choice(lst)

            await ctx.send(giff.embed_url)

        except ApiException:
            return

    #kiss command
    @commands.command()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def kiss(self, ctx):
        api_key = "E37VOBn75rgJsyVkRJI43esG28ILDawy"
        api_instance = giphy_client.DefaultApi()
        keyword = "anime kiss"
        try:
            api_responce = api_instance.gifs_search_get(api_key, keyword , limit=5, rating="g")
            lst = list(api_responce.data)
            giff = random.choice(lst)

            await ctx.send(giff.embed_url)

        except ApiException:
            return

    #meme command
    @commands.command()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def meme(self, ctx):
        reddit = praw.Reddit(
            client_id='0ob0TDuZLKtccA',
            client_secret='TLggaeGi_pHwR93SWegfihtmkkncKw',
            user_agent='TBot Bot'
        )

        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submissions = next(x for x in memes_submissions if not x.stickied)

        meme_embed = discord.Embed(color=0x5865F2)

        meme_embed.set_image(url=submissions.url)
  
        await ctx.send(embed=meme_embed)

    #cat image command
    @commands.command()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://aws.random.cat/meow") as r:                   
        
                data = await r.json()

                embed = discord.Embed(color=0x808080)

                embed.set_image(url=data["file"])

                await ctx.send(embed=embed)

    #dog image command
    @commands.command()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def dog(self, ctx):   
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random.dog/woof.json") as r:                       
                data = await r.json()

                embed = discord.Embed(color=0x00ff00)

                embed.set_image(url=data["url"])

                await ctx.send(embed=embed)

    #joke command 
    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def friends(self, ctx):
        url = "https://friends-quotes-api.herokuapp.com/quotes/random"

        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(color=0x5865F2)

                embed.add_field(name=data["character"], value=data["quote"])

                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def quote(self, ctx):
        url = "http://quotes.stormconsultancy.co.uk/random.json"

        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(color=0x5865F2)

                embed.add_field(name=data["quote"], value=data["author"])

                await ctx.send(embed=embed)

    @commands.command(aliases=["show","search"])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def showpic(self, ctx, *, search):
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=api_key).cse()

        result = resource.list(q=f"{search}", cx="a0aee262f890651c4", searchType="image").execute()

        url = result["items"][ran]["link"]

        embed1 = discord.Embed(title=f"Here is Your Image for `{search.title()}`")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        """ Find the 'best' definition to your words 📚"""
        async with ctx.channel.typing():
            try:
                with urllib.request.urlopen(f"https://api.urbandictionary.com/v0/define?term={search}") as url:
                    url = json.loads(url.read().decode())
            except:
                return await ctx.send("Urban API returned invalid data... might be down atm.")

            if not url:
                return await ctx.send("I think the API broke...")

            if not len(url["list"]):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url["list"], reverse=True,
                            key=lambda g: int(g["thumbs_up"]))[0]

            definition = result["definition"]
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(" ", 1)[0]
                definition += "..."
            definition = definition.replace('[', "").replace("]", "")
            em = discord.Embed(
                title=f"📚 Definitions for **{result['word']}**", description=f"\n{definition}",
                color=discord.Colour.red())
            await ctx.send(embed=em)

    @commands.command(aliases=['wikipedia'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def wiki(self, ctx, *, querry_: str):
        async with ctx.channel.typing():
            try:
                results = wikipedia.search(querry_, results=5)
                result_summary = wikipedia.summary(results[0])
                result_title = results[0]
                em = discord.Embed(title=result_title,
                                   color=discord.Color(0xf58742))
                em.set_footer(text=result_summary)
                em2 = discord.Embed(color=discord.Color(0xf58742))

                em2.set_footer(text=f'Recommended searches : ' +
                                    f'{results[1:-1]}'[1:-1])
                await ctx.send(embed=em)
                await ctx.send(embed=em2)
            except:
                await ctx.send("Sorry, I can't find " + querry_ + " in Wikipedia")

    @commands.command()
    async def covid(self, ctx, *, countryName = None):
        try:
            if countryName is None:
                url="https://covid19.mathdro.id/api"
                stats = requests.get(url)
                data = stats.json()

                covid=discord.Embed(title="Worldwide COVID-19 Stats 🌎", color=0x5865F2)

                covid.add_field(name="Confirmed Cases", value=data["confirmed"], inline=False)
                covid.add_field(name="Recovered", value=data["recovered"], inline=False)
                covid.add_field(name="Deaths", value=data["deaths"], inline=False)

                await ctx.send(embed=covid)

            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description="This Information Isn't Live Always, Hence It May Not Be Accurate!", colour=0x0000ff, timestamp=ctx.message.created_at)
                embed2.add_field(name="**Total Cases**", value=totalCases, inline=False)
                embed2.add_field(name="**Today Cases**", value=todayCases, inline=False)
                embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=False)
                embed2.add_field(name="**Today Deaths**", value=todayDeaths, inline=False)
                embed2.add_field(name="**Recovered**", value=recovered, inline=False)
                embed2.add_field(name="**Active**", value=active, inline=False)
                embed2.add_field(name="**Critical**", value=critical, inline=False)
                embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=False)
                embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=False)
                embed2.add_field(name="**Total Tests**", value=totalTests, inline=False)
                embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=False)

                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                await ctx.send(embed=embed2)

        except:
            embed3 = discord.Embed(title="Invalid Country Name Try Again..!", colour=0xff0000, timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def binary(self, ctx, *, args):
        url=f"http://some-random-api.ml/binary?text=${args}"

        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(color=0x5865F2)

                embed.set_thumbnail(url="https://png.pngtree.com/png-clipart/20200225/original/pngtree-binary-code-and-magnifying-glass-isometric-icon-png-image_5252004.jpg")

                embed.add_field(name=f"Text To Binary", value=data["binary"])

                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def clyde(self, ctx, *, text):
        url=f"https://nekobot.xyz/api/imagegen?type=clyde&text=${text}"

        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(color=0x5865F2)

                embed.set_image(url=data["message"])

                await ctx.send(embed=embed)

    #broken
    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def country(self, ctx, country):
        url=f"https://restcountries.eu/rest/v2/name/" + country

        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(color=0x5865F2)

                embed.add_field(name=f"Name", value=(data["name"]))
                embed.add_field(name=f"Capital", value=(data["capital"]))
                embed.add_field(name=f"Location", value=(data["region"]))
                embed.add_field(name=f"Currenc", value=(data["currencies"]))
                embed.add_field(name=f"Population", value=(data["population"]))
                embed.add_field(name=f"Area", value=(data["area"]+"km"))
                embed.add_field(name=f"Languages", value=(data["languages"]))

                await ctx.send(embed=embed)
    
    @commands.command()
    async def youtube(self, ctx, search):
        yt=discord.Embed(title="YT search", color=0x5865F2)
        
        yt.add_field(name="You Searched for", value=f"{search}", inline=True)
        yt.add_field(name="Results", value=f"[Here's What I found](https://youtube.com/results?search_query=${search})`", inline=True)

        await ctx.send(embed=yt)
    
    #broken
    @commands.command()
    async def minecraft(self, ctx, *, sentence):
        embed = discord.Embed(color=0x00ff00)

        embed.set_image(url=f'https://api.cool-img-api.ml/achievement?text={sentence}')

        await ctx.send(embed=embed)
    
    @commands.command()
    async def pat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://nekos.life/api/v2/img/pat") as r:                       
                data = await r.json()

                embed = discord.Embed(color=0x00ff00)

                embed.set_image(url=data["url"])

                await ctx.send(embed=embed)

    @commands.command()
    async def qr(self, ctx, link):
        embed = discord.Embed(color=0x00ff00)

        embed.set_image(url=f"http://api.qrserver.com/v1/create-qr-code/?data={link}&size=200x200")

        await ctx.send(embed=embed)
    
    #wink.js

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def duck(self, ctx):
        url=f"https://random-d.uk/api/v1/random?type=png"

        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(color=0x5865F2)

                embed.set_image(url=data["url"])

                embed.set_footer(text=f" |   {ctx.author.name}  |   {data['message']}", icon_url=ctx.author.avatar_url)

                await ctx.send(embed=embed)

def setup(client):
        client.add_cog(api(client))