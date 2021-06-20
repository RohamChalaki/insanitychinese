from re import IGNORECASE
import discord
from discord import client
from discord import message
from discord import channel
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands import bot



class utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility commands are ready...\n-----')
    
    #Commands
    @commands.command()
    async def ping(self, ctx):
            embed2 = discord.Embed(title=f'Pong! {round(commands.Bot.latency * 1000)}ms')
            await ctx.send(embed=embed2)

    @commands.command()
    async def help_util(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.green()
        )
        embed.set_author(name='Help Utility')
        embed.add_field(name='Ping', value="Returns the bot's latency.", inline=True)
        embed.add_field(name='Poll', value='Makes a message which people can react yes/no to it.', inline=True)
        embed.add_field(name='Invite', value="Returns the bot's invite link.", inline=True)
        embed.add_field(name='Vote', value="Returns the bot's Vote link.", inline=True)
        embed.add_field(name='WebSite', value="Returns the bot's Website link.", inline=True)
        embed.add_field(name='Credit', value="Returns the bot's Developer.", inline=True)
        embed.add_field(name='UserInfo', value="Returns information about the mentioned user.", inline=True)
        embed.add_field(name='Avatar', value="Returns someone's avatar link.", inline=True)
        embed.add_field(name='ServerInfo', value="Returns all the information about the server.", inline=True)
        embed.add_field(name='Giveaway', value="Hosts a giveaway in the channel you want.", inline=True)
        embed.add_field(name='Post', value="Dms you making a post for hiring/selling.", inline=True)
        embed.add_field(name='Rules', value="The bot sends you all the server rules.", inline=True)




        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def poll(self, ctx, *, message):
        await ctx.channel.purge(limit= 1)
        embed = discord.Embed(title=" POLL ", description=f"{message}", inline=True)
        msg=await ctx.channel.send(embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title='SOOOOON')
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title='COMING SOON', description='STAY TUNE')
        await ctx.send(embed=embed)

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(title='COMING SOON', description='STAY TUNE')
        await ctx.send(embed=embed)

    @commands.command()
    async def credit(self, ctx):
        embed = discord.Embed(title='Made By NotNooby#1234')
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):

        roles = [role for role in member.roles]


        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"Information - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID :", value=member.id, inline=True)
        embed.add_field(name="UserName :", value=member.display_name, inline=True)

        embed.add_field(name="Created At :", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined At :", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)

        embed.add_field(name=f"Roles :({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name=f"Top Role :", value=member.top_role.mention, inline=True)

        embed.add_field(name=f"Bot?", value=member.bot, inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        if not member:
            embed = discord.Embed(title="Please specify a member.")
            await ctx.send(embed=embed)
        else:
            await ctx.send(member.avatar_url)

    @commands.command()
    async def serverinfo(self, ctx):
        channels_amount = len(ctx.guild.channels)
        emoji_limit = (ctx.guild.emoji_limit)
        emoji_count = len(ctx.guild.emojis)
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        embed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
        embed.add_field(name='Server Owner :', value="NotNooby#1234", inline=True)
        embed.add_field(name='Server Name :', value=ctx.guild.name, inline=True)
        embed.add_field(name='Member Count :', value=ctx.guild.member_count, inline=True)
        embed.add_field(name='Verification Level :', value=str(ctx.guild.verification_level), inline=True)
        embed.add_field(name='Top Role :', value=ctx.guild.roles[-2], inline=True)
        embed.add_field(name='Amount of Roles :', value=str(role_count), inline=True)
        embed.add_field(name='Bots :', value=', '.join(list_of_bots), inline=True)
        embed.add_field(name='Emojis :', value=f'({emoji_count}/{emoji_limit})', inline=True)
        embed.add_field(name='Amount of Channels :', value=(channels_amount), inline=True)

        await ctx.send(embed=embed)







    

        
    

def setup(client):
    client.add_cog(utilities(client))