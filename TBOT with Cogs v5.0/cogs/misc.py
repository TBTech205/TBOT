import discord
import random
import platform
import json

from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    #short help list
    @commands.command()
    async def help(self, ctx):
        help_Embed = discord.Embed(title=f"**__{ctx.author.name} this are the help commands:__**", color=0x5865f2)
  
        help_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        help_Embed.add_field(name="TBOT'S Commandlist",value="A list of all Commands | [click here](https://www.tbotdashboard.xyz/)", inline=False)

        help_Embed.add_field(name="TBOT'S Community Server",value="Come join the community | [click here](https://discord.gg/FEPbjPGKJv)", inline=False)  
  
        await ctx.send(embed=help_Embed)

    #hello command
    @commands.command()
    async def hello2(self, ctx):
        hello_Embed = discord.Embed(title="", color=0x5865f2)
  
        hello_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        hello_Embed.add_field(name="Hello", value="Hello, how are you", inline=False)
  
        hello_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.send(embed=hello_Embed)

    #goodbye command
    @commands.command()
    async def bye(self, ctx):
        bye_Embed = discord.Embed(title="", color=0x5865f2)
      
        bye_Embed.set_thumbnail(url=ctx.guild.icon_url)

        bye_Embed.add_field(name="Goodbye", value="Why are you leaveing me", inline=False)
      
        bye_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
      
        await ctx.send(embed=bye_Embed)

    #happy command
    @commands.command()
    async def happy(self, ctx):
        happy_Embed = discord.Embed(title="", color=0x5865f2)
  
        happy_Embed.set_thumbnail(url=ctx.guild.icon_url)

        happy_Embed.add_field(name="Happy", value="Why are you happy")
  
        happy_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.send(embed=happy_Embed)

    #sad commands
    @commands.command()
    async def sad(self, ctx):
        sad_Embed = discord.Embed(title="", color=0x5865f2)
    
        sad_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        sad_Embed.add_field(name="sad", value="Why are you sad", inline=False)
  
        sad_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.send(embed=sad_Embed)

    #love command
    @commands.command()
    async def love(self, ctx):
        love_Embed = discord.Embed(title="", color=0x5865f2)
  
        love_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        love_Embed.add_field(name="Love", value="Love you :love_letter:", inline=False)
  
        love_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.send(embed=love_Embed)

    #hate command
    @commands.command()
    async def hate(self, ctx):
        hate_Embed = discord.Embed(title="", color=0x5865f2)
  
        hate_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        hate_Embed.add_field(name="Hate", value="Why do you hate me :sob:", inline=False)
  
        hate_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.send(embed=hate_Embed)

    #TB command
    @commands.command()
    async def tbot(self, ctx):
        tb_Embed = discord.Embed(title="", color=0x5865f2)
  
        tb_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        tb_Embed.add_field(name="TB", value="You might say who am i? i am @TBOT next you might ask what do i do? so i play !help and that is what i do and my owner is @TB Tech", inline=False)
  
        tb_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.send(embed=tb_Embed)

    #ping command
    @commands.command(aliases=["pong"])
    async def ping(self, ctx):
        ping_Embed = discord.Embed(title="", color=0x5865f2)

        ping_Embed.set_thumbnail(url=ctx.guild.icon_url)
  
        ping_Embed.add_field(name="Bot's latency", value=f":arrow_right: ping: {round(self.client.latency*1000)}ms", inline=False)
  
        ping_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=ping_Embed)

    @commands.command(aliases=['death'])
    async def dead(self, ctx):      
        dead_Embed = discord.Embed(title="", color=0x5865F2)
        
        dead_Embed.add_field(name="Dead Chat", value=f"The chat was declared dead by {ctx.author.display_name}", inline=False)
  
        dead_Embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
        await ctx.message.delete()
        await ctx.send(embed=dead_Embed)

    #goodmornig command
    @commands.command(aliases=["gm"])
    async def morning(self, ctx):
        await ctx.send ("https://tenor.com/view/bear-blow-akiss-love-hearts-kissing-gif-14744176")

    #goodevening command
    @commands.command(aliases=["ge"])
    async def evening(self, ctx):
        await ctx.send ("https://tenor.com/view/good-evening-gif-8471216")

    #goodnight command
    @commands.command(aliases=["gn"])
    async def night(self, ctx):
        await ctx.send ("https://tenor.com/view/bear-blow-akiss-love-hearts-kissing-gif-15229339")

    #cry command
    @commands.command()
    async def cry(self, ctx):
        await ctx.send ("https://tenor.com/view/milkandmocha-cry-sad-tears-upset-gif-11667710")
    
    #loveu command
    @commands.command()
    async def loveu(self, ctx):
        await ctx.send ("https://tenor.com/view/bear-blow-akiss-love-hearts-kissing-gif-15898752")

    #stfu command
    @commands.command()
    async def stfu(self, ctx):
        await ctx.send (":regional_indicator_s: :regional_indicator_t: :regional_indicator_f: :regional_indicator_u:")

    #shut command
    @commands.command()
    async def shut(self, ctx):
        unshut_Embed = discord.Embed(title="", color=0x5865f2)
  
        unshut_Embed.set_image(url="https://cdn.discordapp.com/emojis/814239623378501702.png?v=1") 

        await ctx.send(embed=unshut_Embed)

    #unshut command
    @commands.command()
    async def unshut(self, ctx):
        unshut_Embed = discord.Embed(title="", color=0x5865f2)
  
        unshut_Embed.set_image(url="https://media.discordapp.net/attachments/853044775422656522/853054215341211678/t_unshut.png") 

        await ctx.send(embed=unshut_Embed)

    #8ball command
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        ballresponses = ['definatly','hahaha no','sure','mmm idk','i guess?','emm.. what? i wasnt listening','ask again','dont ask me']
                
        ball_embed = discord.Embed(title="", color=0x5865f2)
        
        ball_embed.add_field(name=f"question: {question}", value=f"\n**Answer:** {random.choice(ballresponses)}", inline=False)
                
        await ctx.send(embed=ball_embed)

    #head to api_cmds.py

    #copy command
    @commands.command()
    async def copy(self, ctx,*, mssg):
        await ctx.send(f"{mssg}")

    #respect commamd
    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

    #suggestion command
    @commands.command()
    async def suggestform(self, ctx):
        suggest_embed = discord.Embed(title="**__command suggestion:__**", description="Suggest a command for TBOT [**Here**](https://forms.gle/FumcPexsQ9NuvMTHA)", color=0x5865f2)

        suggest_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=suggest_embed)

    @commands.command(aliases=["suggestion"])
    async def suggest(self, ctx, trigger, *, suggestion: str):
        em = discord.Embed(title="Your suggestion has been recorded!", color=discord.Color.green())
        mes= await ctx.reply(embed=em, delete_after=5.0)
        await mes.add_reaction('✅')

        sugg_em = discord.Embed(title=f"New Suggestion")

        sugg_em.set_thumbnail(url=ctx.author.avatar_url)

        sugg_em.add_field(name=f"**Trigger:**", value=f"{trigger}", inline=False)
        sugg_em.add_field(name=f"**Response:**", value=f"{suggestion}", inline=False)
        sugg_em.add_field(name=f"**Suggested by:**", value=f"{ctx.author.display_name}", inline=False)

        mes= await self.client.get_channel(852208566672031754).send(embed=sugg_em)
        await mes.add_reaction('✅')
    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            error=discord.Embed(title="", color=0xed5757)
            
            error.add_field(name="Missing Required Argument please do \n!suggest {trigger} {suggestion}", value="Error - 403")

            await ctx.send(embed=error)
        else:
            raise error

    #pp command
    @commands.command(aliases=["pepe"])
    async def pp(self, ctx, member: discord.Member):
        size = ['', '==', '', '=', '', '====', '', '=', '======', '==========================', '===',
                "===============","========", "===", "===================", "===", '========', '=====',  "======================================", "===", "============"]
        
        em = discord.Embed(color=discord.Color.blue(), title="PeePee size calculator")

        em.add_field(name=f"{member.display_name}s pp", value=f"8{random.choice(size)}D")
        await ctx.send(embed=em)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        await ctx.send(f"Your hug has been set off to {member}")

        if member == ctx.message.author:
            hug = discord.Embed(color=0xed5757)
        
            hug.set_author(name=f"{ctx.author.display_name} has given you a hug")
                
            await member.send(embed=hug)

            return

        else:
            hug = discord.Embed(color=0xed5757)
        
            hug.set_author(name=f"{ctx.author.display_name} has given you a hug")
                
            await member.send(embed=hug)

    #num command
    @commands.command(aliases=["num", "number"])
    async def givenum(self, ctx):
        responses = ["1","2","3","4","5","6","7","8","9","10"]
        
        num=discord.Embed(title="", color=0x5865f2)

        num.add_field(name="your number is:", value=f"{(random.choice(responses))}")
        
        await ctx.send(embed=num)

    #yes command
    @commands.command()
    async def yes(self, ctx):
        yes_Embed = discord.Embed(title="", color=0x5865f2)
  
        yes_Embed.set_image(url="https://images-ext-1.discordapp.net/external/OaJgoRrcThqPP5pjRE2IDsv9kPtsVDADW2f4EzAbJ1U/%3Fv%3D1/https/cdn.discordapp.com/emojis/597590985802907658.png")

        await ctx.send(embed=yes_Embed)

    #no command
    @commands.command()
    async def no(self, ctx):
        no_Embed = discord.Embed(title="", color=0x5865f2)
  
        no_Embed.set_image(url="https://images-ext-2.discordapp.net/external/95PlD1VzmGy2hgTntTjOfi4lXvmccM5kFXK0hQ_kv7E/%3Fv%3D1/https/cdn.discordapp.com/emojis/597591030807920660.png")

        await ctx.send(embed=no_Embed)

    @commands.command()
    async def servers(self, ctx):
        await ctx.send(f"I'm in `" + str(len(self.client.guilds)) + "` servers")

    @commands.command()
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver
        
        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0
            player1 = p1
            player2 = p2
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        else:
            await ctx.send("A game is already in progress! Finish it before starting a new one.")

    #place command
    @commands.command()
    async def place(self, ctx, pos: int): 
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver
        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
                    checkWinner(winningConditions, mark)
                    if gameOver == True:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie!")

                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.send("It is not your turn.")
        else:
            await ctx.send("Please start a new game using the !tictactoe command.")

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):     
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

    @place.error
    async def place_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")

    #server-info commands
    @commands.command(aliases=["server-info", "serverinformation"])
    async def serverinfo(self, ctx):
        name= str(ctx.guild.name)
        members = str(ctx.guild.member_count)
        owner = str(ctx.guild.owner.mention)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)

        embed = discord.Embed(title= name + " server Information", color=0x5865f2)

        embed.add_field(name="Server name", value= name ,inline=False)

        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="server ID", value=id, inline=False)
        embed.add_field(name="region", value=region, inline=False)
        embed.add_field(name="Member Count", value=members, inline=False)
        embed.add_field(name="creation date", value="`coming soon`", inline=False)
        embed.add_field(name="server icon", value= f"{ctx.guild.icon_url}", inline=False)

        await ctx.send(embed=embed)

    #userinfo command
    @commands.command(aliases=["user-info", "u-info","uinfo"])
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        
        memberid=(member.id)
        name=(member.display_name)
        created=(member.created_at.strftime("%a, %#d %B %Y UTC"))
        join=(member.joined_at.strftime("%a, %#d %B %Y UTC"))
        roles=" ".join([role.mention for role in roles])
        toprole=(member.top_role.mention)
        bot=(member.bot)
        boost=(str(bool(member.premium_since)))
  
        userinfo_embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
  
        userinfo_embed.set_author(name=f"user info - {member}")
  
        userinfo_embed.set_thumbnail(url=ctx.author.avatar_url)
  
        userinfo_embed.add_field(name="ID: ", value=memberid, inline=False)
        userinfo_embed.add_field(name="Name: ", value=name, inline=False)
        userinfo_embed.add_field(name="Created at: ", value=created, inline=False)
        userinfo_embed.add_field(name="Joined at: ", value=join, inline=False)
        userinfo_embed.add_field(name=f"roles ({len(roles)})", value=roles, inline=False)
        userinfo_embed.add_field(name="Top role: ", value=toprole, inline=False)
        userinfo_embed.add_field(name="Bot: ", value=bot, inline=False)
        userinfo_embed.add_field(name="Boosted: ", value=boost, inline=False)
  
        userinfo_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=userinfo_embed)

    #botinfo command
    @commands.command()
    async def botinfo(self, ctx):
        Responsetime = round(self.client.latency*1000)
        Library_Version = platform.python_version()
        total_servers = str(len(self.client.guilds))
        dpyVersion = discord.__version__

        info_embed = discord.Embed(title="", color=0x5865f2)

        info_embed.set_author(name="Bot info", icon_url= "https://media.discordapp.net/attachments/837459215807021057/847576017509154816/unknown.png")

        info_embed.set_thumbnail(url="https://media.discordapp.net/attachments/837459215807021057/847574989565198336/4ExBd_dP_400x400.jpg")

        info_embed.add_field(name=f"Response time", value=f"`{Responsetime}ms`", inline=False)
        info_embed.add_field(name=f"Total Servers", value=f"`{total_servers}`", inline=False)
        info_embed.add_field(name=f"Library Version", value=f"`{Library_Version}`", inline=False)
        info_embed.add_field(name=f"Discord Version", value=f"`{dpyVersion}`", inline=False)

        await ctx.send(embed=info_embed)

    #HRU command
    @commands.command()
    async def hru(self, ctx):
        await ctx.reply("I am fine... how are you?")

    #bongo command
    @commands.command()
    async def bongo(self, ctx):
        Embed = discord.Embed(title="", color=0x5865f2)

        Embed.set_image(url="https://c.tenor.com/ixg0iUMoBZAAAAAj/cat-bongo.gif")

        await ctx.send(embed=Embed)

    #avatar command
    @commands.command()
    async def avatar(self, ctx, *,  member : discord.Member=None):
        embed = discord.Embed(title=f"{member}'s Avatar!", colour=0x5865f2, timestamp=ctx.message.created_at)
        
        embed.add_field(name="Animated?", value=member.is_avatar_animated())
        
        embed.set_image(url=member.avatar_url)
        
        await ctx.send(embed=embed)
  
    #dice roll command
    @commands.command()
    async def diceroll(self, ctx):
        responses = ["1","2","3","4","5","6"]
    
        embed = discord.Embed(title="", color=0x5865f2)
    
        embed.add_field(name=f"you rolled the number: ", value=f"{random.choice(responses)}", inline=False)
    
        await ctx.send(embed=embed)

    #test command
    @commands.command()
    async def test(self, ctx):
        await ctx.send("░█████╗░██╗░░░░░██╗██╗░░░██╗███████╗ \n██╔══██╗██║░░░░░██║██║░░░██║██╔════╝ \n███████║██║░░░░░██║╚██╗░██╔╝█████╗░░ \n██╔══██║██║░░░░░██║░╚████╔╝░██╔══╝░░ \n██║░░██║███████╗██║░░╚██╔╝░░███████╗ \n╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝")

    #member command
    @commands.command()
    async def members(self, ctx):
        embed = discord.Embed(title=f"There are {str(ctx.guild.member_count)} members in {ctx.guild.name}!", colour=0x5865f2, timestamp=ctx.message.created_at) 
        
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)

        await ctx.send(embed=embed)

    #rip command
    @commands.command()
    async def rip(self, ctx):
        await ctx.send("https://tenor.com/view/rip-coffin-black-ghana-celebrating-gif-16743302")

    #noice command 
    @commands.command()
    async def noice(self, ctx):
        Embed = discord.Embed(title="", color=0x5865F2)
    
        Embed.set_image(url="https://cdn.discordapp.com/attachments/831537820036235284/847514964474462298/Z.png")
    
        await ctx.send(embed=Embed)

    #sheesh command
    @commands.command()
    async def sheesh(self, ctx):
        await ctx.send("<:sheesh:849041102337867846>")

    @commands.command()
    async def coinflip(self, ctx):
        coin = ["heads", "tales"]
    
        coin_embed = discord.Embed(title="", color=0x5865F2)
    
        coin_embed.add_field(name=f"you fliped the number: ", value=f"{random.choice(coin)}", inline=False)
    
        await ctx.send(embed=coin_embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="", color=0x5865F2)
    
        embed.add_field(name="TBOT invite link:", value="Add TBOT [here](https://discord.com/api/oauth2/authorize?client_id=818585855861063690&permissions=4294967287&scope=bot%20applications.commands)", inline=False)
  
        embed.add_field(name="Things to consider", value="please put my roles as high as you can \nPlease give my administrator role \nPlease make my `Muted` role", inline=False)
    
        await ctx.send(embed=embed)

    @commands.command(aliases=["calc"])
    async def calculate(self, ctx, *nums):
        sys = ["+", "-", "*", "/", "÷", "×"]

        var = f' {sys} '.join(nums)
        await ctx.send(f"{var} = {eval(var)}")

    @commands.command()
    async def bread(self, ctx):
        embed = discord.Embed(color=0x5865f2)
        
        embed.set_image(url="https://cdn.discordapp.com/emojis/814238780705472522.png?v=1")

        await ctx.send(embed=embed)

    @commands.command()
    async def iloveu(self, ctx):
        await ctx.send("```██╗  ██╗░░░░░░█████╗░██╗░░░██╗███████╗  ██╗░░░██╗░█████╗░██╗░░░██╗    \n██║  ██║░░░░░██╔══██╗██║░░░██║██╔════╝  ╚██╗░██╔╝██╔══██╗██║░░░██║ \n██║  ██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░  ░╚████╔╝░██║░░██║██║░░░██║ \n██║  ██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░  ░░╚██╔╝░░██║░░██║██║░░░██║ \n██║  ███████╗╚█████╔╝░░╚██╔╝░░███████╗  ░░░██║░░░╚█████╔╝╚██████╔╝ \n╚═╝  ╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░```")

    #head to _level.py

    @commands.command()
    async def goodjob(self, ctx):
        await ctx.send("https://tenor.com/view/fireworks-well-done-good-job-colorful-celebrate-gif-17240767")
    
    @commands.command()
    async def dev(self, ctx):
        dev = discord.Embed(title="", description= "", color=0x5865f2)

        dev.add_field(name="<:owner:852143471480668170> Owner", value="TB Tech#0873", inline=False)
        dev.add_field(name="<:DiscordBotDev:843938651074199593> Developer", value="Mr. Snowman༄#0001", inline=False)

        await ctx.send(embed=dev)

    @commands.command(aliases=["contact"])
    async def support(self, ctx):
        support = discord.Embed(title="", description= "", color=0x5865f2)

        support.add_field(name="<:discord_logo:857918374574555167> Discord Server", value="https://discord.gg/FEPbjPGKJv", inline=False)

        await ctx.send(embed=support)

    @commands.command(aliases=["sicon", "guildicon"])
    async def servericon(self, ctx):
        sicon_Embed = discord.Embed(title="", color=0x5865f2)
  
        sicon_Embed.set_image(url=ctx.guild.icon_url)

        await ctx.send(embed=sicon_Embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send ("██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░ \n██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗ \n███████║█████╗░░██║░░░░░██║░░░░░██║░░██║ \n██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║ \n██║░░██║███████╗███████╗███████╗╚█████╔╝ \n╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░")
    
    @commands.command()
    async def error(self, ctx):
        error = discord.Embed(title="TBOT error codes", color=0x5865f2)

        error.add_field(name="`401` - Forgot to mention a Member", value="\uFEFF", inline=False)
        error.add_field(name="`402` - Missing Permissions", value="\uFEFF", inline=False)
        error.add_field(name="`403` - Missing value", value="\uFEFF", inline=False)

        await ctx.send(embed=error)

    @commands.command()
    async def updates(self, ctx):
        error = discord.Embed(title="", color=0x5865f2)

        error.add_field(name="Latest Changes", value="```> Cosmetic Changes < \n# Error messaged have been re-designed \n\n> Bug Fixes < \n# Fixed !suggest \n\n> New Commands< \n# Added !error```", inline=False)

        await ctx.send(embed=error)
    
    @commands.command()
    async def bages(self, ctx):
        bages=discord.Embed(title="Discord Profile Badges", color=0x5865f2)

        bages.add_field(name="<:DiscordNitroClassic:843938623564939295> Discord Nitro", value="When someone with this badge subscribes to Discord Nitro! Both Nitro and Nitro Classic members will get the same badge. However over their badge and you’ll see how long they’ve been a Nitro member! (find more [here](https://support.discord.com/hc/en-us/articles/115000435108-Discord-Nitro-Classic-Nitro))", inline=False)

        bages.add_field(name="<:serverbost:860053567371870208> Server Booster", value="This user directly supports one of their favorite servers! In the server they’ve boosted, they also get a Boosting icon next to their name. Hover over the badge and you’ll see how long they’ve boosted servers. (find more [here](https://support.discord.com/hc/en-us/articles/360028038352))", inline=False)

        bages.add_field(name="<:houseofbravery:860053135279128606> House Of Bravery", value="The universe needs people to lead the charge with confident optimism and tenacity. Without the brave, the HypeSquad would descend into chaos.(find more [here](https://support.discord.com/hc/en-us/articles/360007553672))", inline=False)

        bages.add_field(name="<:houseofbrilliance:860053134960230411> House Of Brilliance", value="It takes patience and discipline to become a vital member of the universe. Without brilliance, the HypeSquad would descend into chaos. (find more [here](https://support.discord.com/hc/en-us/articles/360007553672))", inline=False)
    
        bages.add_field(name="<:houseofbalance:860053135207432202> House Of Balance", value="Harmony and poise are necessary to create equilibrium in the universe. Without balance, the HypeSquad would descend into chaos. (find more [here](https://support.discord.com/hc/en-us/articles/360007553672))", inline=False)
    
        bages.add_field(name="<:DiscordHypeSquad:843938641755897937> HypeSquad events", value="The HypeSquad Events badge is for HypeSquad Event Attendees &  who attend local conventions in the name of HypeSquad. Event Coordinators run the events themselves, such as a university club or LAN event.", inline=False)

        bages.add_field(name="<:DiscordBugHunter:843938659995484170> Bug Hunter", value="The Bug Hunter badge is awarded to the most hard-working of those in the Bug Hunter community. Someone with this badge probably spends their time perfecting their next Redstone-powered monolith that also acts as a calculator. (Wanna join the Bug Hunting community? [here](https://discord.gg/discord-testers))", inline=False)

        bages.add_field(name="<:DiscordPartner:843938669064880188> Discord Partner", value="Designed for active and engaged communities, the Partner Program distinguishes the best servers out there. This badge is given to owners of thriving communities and creators that show an authentic enthusiasm for Discord.(find more [here](https://discord.com/partners))", inline=False)

        bages.add_field(name="<:DiscordStaff:843938614370238535> Discord Staff", value="this person spends most of their week at Discord HQ, thinking of the next best thing to add improve your Discord experience and dreaming of when the office is going to get a soft-serve machine. (find more [here]())", inline=False)

        await ctx.send(embed=bages)
    
    @commands.command()
    async def serverinvite(self, ctx):
        invite= await ctx.channel.create_invite()
        await ctx.send(invite)
    
    @commands.command()
    async def logs(self, ctx):
        logs=discord.Embed(title="", color=0x5865f2)

        logs.add_field(name="Available Command logging", value="```clear \nkick \nban \nunban \nmute \nunmute \ntempmute \nslowmode \nwarn```")
        
        logs.add_field(name="Available Automatic logging", value="```create invites \ndelete invites \nban members \nunban members \nwelcome  \nleave \nmessage deleted \nchannel created \nchannel deleted \nchannel updated \nchannel pins \nuser update \nrole create \nrole update \nemoji  update```")

        await ctx.send(embed=logs)

#tictactoe
player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6] ]

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


def setup(client):
    client.add_cog(misc(client))