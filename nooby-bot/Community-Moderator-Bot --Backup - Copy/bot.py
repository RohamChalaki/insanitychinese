from asyncio.tasks import wait, wait_for
import discord
import os
import random
import aiofiles
import asyncpraw
import asyncio
import json
from discord import user
from discord import client
from discord import message
from discord import emoji
from discord.activity import CustomActivity
from discord.ext import commands
from discord.role import RoleTags

os.chdir("C:\\Users\\roham\\OneDrive\\Desktop\\Community-Moderator-Bot --Backup - Copy")

mainshop = [{"name":"Watch","price":"100","description":"Used for checking Time"},
            {"name":"Laptop","price":"1000","description":"Used for Working"},
            {"name":"PC","price":"10000","description":"Used for Gaming"}]

reactions = [":white_check_mark:", ":stop_sign:", ":no_entry_sign:"]

intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix = '!', intents=intents)
bot.remove_command('help')

random_color = [0xf50303,
                0x2c91b3, 
                0x0bcf00]



invites = {}

def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!help'))
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: ( ! )\n-----")
    for guild in bot.guilds:
        invites[guild.id] = await guild.invites()

def find_invite_by_code(invite_list, code):
    for inv in invite_list:                
        if inv.code == code:
            return inv



@bot.event
async def on_message(msg):
    if not msg.author.bot:
        if not msg.guild:
            channel = bot.get_channel(853175901087858769)
            embed = discord.Embed(title=f"MOD-MAIL---{msg.author}", description=f"User **{msg.author}** sent a mod-mail saying\n`{msg.content}`")
            await channel.send(embed=embed)
        await bot.process_commands(msg)


@bot.event
async def on_member_join(member):
    invites_before_join = invites[member.guild.id]
    invites_after_join = await member.guild.invites()
    role = discord.utils.get(member.guild.roles, name='member')
    role2 = discord.utils.get(member.guild.roles, name='auto')
    await member.add_roles(role)
    await member.add_roles(role2)
    channel = bot.get_channel(853155073168637962)
    avatar = member.avatar_url
    embed = discord.Embed(title='FROSTBYTE DEVELOPEMENT', description=f'Welcome to the server.\n{member}', colour=discord.Colour.blue())
    embed.set_thumbnail(url=avatar)
    await channel.send(embed=embed)
    for invite in invites_before_join:
        if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
            print(f"Member {member.name} Joined")
            print(f"Invite Code: {invite.code}")
            print(f"Inviter: {invite.inviter}")
            invites[member.guild.id] = invites_after_join
            return




@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(854308238353498122)
    avatar = member.avatar_url
    embed = discord.Embed(title='FROSTBYTE DEVELOPEMENT.', description=f'Goodbye.\n{member}', colour=discord.Colour.blue())
    embed.set_thumbnail(url=avatar)
    await channel.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    
    if payload.member.bot:
        pass
    
    else:

        with open('reactrole.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):

        with open('reactrole.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

@bot.command()
async def bug(ctx, desc=None, rep=None):
    user = ctx.author
    await ctx.author.send('```Please explain the bug```')
    responseDesc = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    description = responseDesc.content
    await ctx.author.send('````Please provide pictures/videos of this bug```')
    responseRep = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    replicate = responseRep.content
    embed = discord.Embed(title='Bug Report', color=0x00ff00)
    embed.add_field(name='Description', value=description, inline=False)
    embed.add_field(name='Replicate', value=replicate, inline=True)
    embed.add_field(name='Reported By', value=user, inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    adminBug = bot.get_channel(854054486461251604)
    await adminBug.send(embed=embed)


@bot.command()
async def mail(ctx, desc=None, rep=None):
    user = ctx.author
    embed3 = discord.Embed(title="Check your dms", colour = random.choice(random_color))
    await ctx.send(embed=embed3)
    embed5 = discord.Embed(title="Please tell your modmail.", description="Respond within 300 seconds.", colour = random.choice(random_color))
    await ctx.author.send(embed=embed5)
    responseDesc = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    description = responseDesc.content
    embed2 = discord.Embed(title="If you wanna provide any images you can provide their link, suggested to use : imgur", description="Respond within 300 seconds.", colour = random.choice(random_color))
    await ctx.author.send(embed=embed2)
    responseRep = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    replicate = responseRep.content
    embed4 = discord.Embed(title="Your modmail has been succesfuly sent.", colour = random.choice(random_color))
    msg = await ctx.author.send(embed=embed4)
    await msg.add_reaction("✅")
    embed = discord.Embed(title='MOD-MAIL', colour = random.choice(random_color))
    embed.add_field(name=f'Mail', value=description, inline=False)
    embed.add_field(name='Images', value=replicate, inline=True)
    embed.add_field(name='Reported By', value=user, inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    adminBug = bot.get_channel(854054486461251604)
    await adminBug.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Succesfuly Loaded the Cog {extension}.')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Succesfuly Unloaded the Cog {extension}.')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Succesfuly Reloaded the Cog {extension}.')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("Giveaways")
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?",
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]
    
    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("You didn't answer in the time, please be quicker next time!")
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time!")
        return
    
    prize = answers[2]

    await ctx.send(f"The giveaway will be in {channel.mention} and will last {answers[1]}")
    
    embed = discord.Embed(title=f"{prize}", description=f"React with 🎉 To enter!", color=discord.Colour.red())

    embed.add_field(name="Hosted By:", value=ctx.author.mention)

    embed.set_footer(text=f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)
    
    embed3 = discord.Embed(title=f"{prize}", description=f"React with 🎉 To enter!", color=discord.Colour.red())

    embed3.add_field(name="Hosted By:", value=ctx.author.mention)

    embed3.set_footer(text=f"{winner} has won, The giveaway has ended.")
    await my_msg.edit(embed=embed3)
    embed2 = discord.Embed(title=f"Congratulations! {winner} won {prize}!", colour = discord.Colour.green())
    await channel.send(embed=embed2)





@bot.command()
async def post(ctx, forr = None, desc = None, rep = None, amount2 = None, images2 = None):
    user = ctx.author
    embed8 = discord.Embed(title='Check your dm.', colour = 0xf50303)
    await ctx.send(embed=embed8)
    embed7 = discord.Embed(title='Please respond to this question within 300 seconds.', description='Which you are you looking for? (selling, hiring)', colour=discord.Colour.green())
    await ctx.author.send(embed=embed7)
    responseFor = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    For1 = responseFor.content
    embed = discord.Embed(title='Please respond to this question within 300 seconds.', description='Which you are? (builder, scripter, animator, modeler, sfx designer, gfx designer)', colour=discord.Colour.green())
    await ctx.author.send(embed=embed)
    responseDesc = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    description = responseDesc.content
    embed2 = discord.Embed(title='Please respond to this question within 300 seconds.', description='Please provide the information about your work.', colour=discord.Colour.green())
    await ctx.author.send(embed=embed2)
    responseRep = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    replicate = responseRep.content
    embed3 = discord.Embed(title='Please respond to this question within 300 seconds.', description='Please tell how much robux/paypal you are accepting | eg: 1000 robux', colour=discord.Colour.green())
    await ctx.author.send(embed=embed3)
    responseAmount = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    amount = responseAmount.content
    embed4 = discord.Embed(title='Please respond to this question within 300 seconds.', description='Please provide all the images of your work. send them in one message please.', colour=discord.Colour.green())
    await ctx.author.send(embed=embed4)
    imagesProof = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    images = imagesProof.content
    embed6 = discord.Embed(title='Your post was sent.', colour = discord.Colour.green())
    await ctx.author.send(embed=embed6)
    embed5 = discord.Embed(title=str.upper(For1), color=discord.Colour.blue())
    embed5.add_field(name='Developer', value=user, inline=False)
    embed5.add_field(name='Worker', value=description, inline=False)
    embed5.add_field(name='Information', value=replicate, inline=False)
    embed5.add_field(name='Money', value=f"{amount}🤑", inline=False)
    embed5.set_image(url=images)


    

    embed5.set_thumbnail(url=ctx.author.avatar_url)
    adminBug = bot.get_channel(853160200189771786)
    my_msg = await adminBug.send(embed=embed5)
    await my_msg.add_reaction("✅")

@bot.command(aliases=["rules"])
async def rule(ctx):
    embed = discord.Embed(title="Server Rules!", colour = random.choice(random_color))
    embed.add_field(name="Rule Number - 1", value="Do not swear, Swearing may just get you kicked or banned at the worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 2", value="Do not be stupid, Asking questions about stupid stuff, or dming the owner/admins for nothing may also get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 3", value="Keep conversations in English, Please do not talk in any other languages or you may get kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 4", value="No publishing of personal information, Leaking any other's person information may get you kicked or banned at worst case", inline=False)
    embed.add_field(name="Rule Number - 5", value="No harassment, Harrasing anyone may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 6", value="No nsfw content, Any nsfw content may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 7", value="No racism, Any racism to anyone may get you kicked or banned at worst case senario", inline=False)
    embed.add_field(name="Rule Number - 8", value="No hacking/exploiting, Hacking or exploiting in any of our games may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 9", value="No inapropriate Roblox usernames, Any inapropriate usernames may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 10", value="No trolling and No spamming, Doing any of those may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 11", value="No scamming, Scamming anyone may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 12", value="Reselling Products is against the Licence agreement, Reselling anything may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 13", value="No breaking discord TOS, Doing it may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 14", value="Must be subscribed to pewdiepie to be in this server, Not being subscribed may get you kicked or banned at worst case senario.", inline=False)
    embed.add_field(name="Rule Number - 15", value="No pinging without reasonable cause, Doing that may get you kicked or banned at worst case senario.", inline=False)



    await ctx.author.send(embed=embed)

    




@bot.command()
@commands.has_permissions(manage_roles = True)
async def reactrole(ctx, emoji, role: discord.Role = None, *, message):
    embed = discord.Embed(description=message)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name':role.name,
            'role_id':role.id,
            'emoji':emoji,
            'message_id':msg.id
        }

        data.append(new_react_role)


    with open('reactrole.json','w') as j:
        json.dump(data,j,indent=4)

@bot.command()
async def help_music(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name='Help Music')
    embed.add_field(name='Play', value='Plays the music you want.', inline=True)
    embed.add_field(name='Queue', value='Returns the musics in queue.', inline=True)
    embed.add_field(name='Skip', value='Plays the next music.', inline=True)
    embed.add_field(name='Leave', value='Disconnects from the vc.', inline=True)
    embed.add_field(name='Loop', value='Loops the queue.', inline=True)
    embed.add_field(name='Remove', value='Removes a song from the queue.', inline=True)
    embed.add_field(name='Shuffle', value='Shuffles the queue.', inline=True)
    embed.add_field(name='Stop', value='Stops playing songs.', inline=True)
    embed.add_field(name='Pause', value='Pauses the playing song.', inline=True)
    embed.add_field(name='Resume', value='Resumes the playing song.', inline=True)
    embed.add_field(name='Volume', value='Changes the volume of the playing song.', inline=True)
    embed.add_field(name='Join', value='Joins your channel.', inline=True)
    embed.add_field(name='Summon', value='Summon in your channel. (Admin only)', inline=True)



    await ctx.send(embed=embed)

@bot.command()
async def help_economy(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name='Help Economy')
    embed.add_field(name='Balance', value='Shows your balance.', inline=True)
    embed.add_field(name='Beg', value='Beg someone for money.', inline=True)
    embed.add_field(name='WithDraw', value='Take some money from your bank and put in your wallet.', inline=True)
    embed.add_field(name='Deposit', value='Put some money from your wallet to your bank.', inline=True)
    embed.add_field(name='Send', value='Send someone else some money from your bank.', inline=True)
    embed.add_field(name='Rob', value='Take money from someone from their wallet.', inline=True)
    embed.add_field(name='Shop', value='Returns the current shop.', inline=True)
    embed.add_field(name='Buy', value='You can buy an item from the shop with this command. Usage : !buy [item] [amount]', inline=True)
    embed.add_field(name='Sell', value='You can sell an item from your bag with this command. Usage : !sell [item] [amount]', inline=True)
    embed.add_field(name='Bag', value='Returns your inventory.', inline=True)
    embed.add_field(name='Leaderboard', value='Returns the most rich users on the server.', inline=True)





    await ctx.send(embed=embed)

@bot.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]


    embed = discord.Embed(title=f"{ctx.author.name}'s Balance", color = discord.Colour.red())
    embed.add_field(name=f'Wallet Balance',value=wallet_amt)
    embed.add_field(name=f'Bank Balance',value=bank_amt)

    await ctx.send(embed=embed)

@bot.command()
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    embed = discord.Embed(title='Bruh, Imagine begging', description=f'Someone gave you {earnings} Coins, Cringe.')
    await ctx.send(embed=embed)



    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    
@bot.command()
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title='Please enter the amount.')
        await ctx.send(embed=embed)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        embed2 = discord.Embed(title="You don't have that much money!", colour = discord.Colour.green())
        await ctx.send(embed=embed2)
        return
    if amount<0:
        embed3 = discord.Embed(title="Amount must be positive!", colour = discord.Colour.green())
        await ctx.send(embed=embed3)
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount, "bank")

    embed4 = discord.Embed(title=f"You withdrew {amount} Coins!", colour = discord.Colour.blue())
    await ctx.send(embed=embed4)
    

@bot.command()
async def deposit(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title='Please enter the amount.')
        await ctx.send(embed=embed)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        embed2 = discord.Embed(title="You don't have that much money!", colour = discord.Colour.green())
        await ctx.send(embed=embed2)
        return
    if amount<0:
        embed3 = discord.Embed(title="Amount must be positive!", colour = discord.Colour.green())
        await ctx.send(embed=embed3)
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    embed4 = discord.Embed(title=f"You deposited {amount} Coins!", colour = discord.Colour.blue())
    await ctx.send(embed=embed4)

@bot.command()
async def send(ctx, member: discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        embed = discord.Embed(title='Please enter the amount.')
        await ctx.send(embed=embed)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        embed2 = discord.Embed(title="You don't have that much money!", colour = discord.Colour.green())
        await ctx.send(embed=embed2)
        return
    if amount<0:
        embed3 = discord.Embed(title="Amount must be positive!", colour = discord.Colour.green())
        await ctx.send(embed=embed3)
        return

    await update_bank(ctx.author,-1*amount, "bank")
    await update_bank(member,amount,"bank")

    embed4 = discord.Embed(title=f"You Gave {amount} Coins to {member}!", colour = discord.Colour.blue())
    await ctx.send(embed=embed4)


@bot.command()
async def slots(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title='Please enter the amount.')
        await ctx.send(embed=embed)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        embed2 = discord.Embed(title="You don't have that much money!", colour = discord.Colour.green())
        await ctx.send(embed=embed2)
        return
    if amount<0:
        embed3 = discord.Embed(title="Amount must be positive!", colour = discord.Colour.green())
        await ctx.send(embed=embed3)
        return

    final = []
    for i in range(3):

        a = random.choice(["X", "O", "Q"])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author, 2*amount)
        embed = discord.Embed(title='You won', colour=discord.Colour.gold())
        await ctx.send(embed=embed)
    else:
        await update_bank(ctx.author, -1*amount)
        embed2 = discord.Embed(title='You lost', colour=discord.Colour.dark_grey())
        await ctx.send(embed=embed2)

    
@bot.command()
async def rob(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)


    bal = await update_bank(member)

    if bal[0]<100:
        embed2 = discord.Embed(title="Not worth it man.", colour = discord.Colour.green())
        await ctx.send(embed=embed2)
        return

    earnings = random.randrange(0, bal[0])

    await update_bank(ctx.author,earnings)
    await update_bank(member,-1*earnings)

    embed4 = discord.Embed(title=f"You Robbed {earnings} Coins from {member}", colour = discord.Colour.blue())
    await ctx.send(embed=embed4)

@bot.command()
async def shop(ctx):
    embed = discord.Embed(title="Shop!", colour = discord.Colour.dark_blue())
    for item in mainshop:
        name = item['name']
        price = item['price']
        desc = item['description']
        embed.add_field(name = name, value= f"Price: {price} \n Description: {desc}", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            embed = discord.Embed(title="That Object isn't there!", colour = discord.Colour.purple())
            await ctx.send(embed=embed)
            return
        if res[1]==2:
            embed2 = discord.Embed(title=f"You don't have enough money in your wallet to buy {amount} {item}", colour = discord.Colour.purple())
            await ctx.send(embed=embed2)
            return

    embed3 = discord.Embed(title=f"You just bought {amount} {item}", colour = discord.Colour.green())
    await ctx.send(embed=embed3)

@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag", colour = discord.Colour.green())
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)

@bot.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            embed = discord.Embed(title="That Object isn't there!", colour = discord.Colour.purple())
            await ctx.send(embed=embed)
            return
        if res[1]==2:
            embed2 = discord.Embed(title=f"You don't have {amount} {item} in your bag.", colour = discord.Colour.purple())
            await ctx.send(embed=embed2)
            return
        if res[1]==3:
            embed3 = discord.Embed(title=f"You don't have {item} in your bag.", colour = discord.Colour.purple())
            await ctx.send(embed=embed3)
            return

    embed4 = discord.Embed(title=f"You just sold {amount} {item}.", colour = discord.Colour.green())
    await ctx.send(embed=embed4)

@bot.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]



async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)
    
    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]



async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True
    
async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users



async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal


@bot.command()
async def invites(ctx, member: discord.Member=None):
    if member is None: member = ctx.author
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == member:
            totalInvites += i.uses
    embed = discord.Embed(title=f"{member}'s Invites", description=f"Joins: {totalInvites}")
    await ctx.send(embed=embed)



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')




bot.run('ODQ3MDMzNzIyODg0MDYzMjMy.YK4LoA.ChIppct94tMtLJrfvM8rA00nrE8')

