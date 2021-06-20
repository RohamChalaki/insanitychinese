import discord
import random
from discord import colour
import praw
import aiohttp
from discord.ext import commands
from discord.ext.commands import bot




class fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun commands are ready...\n-----')
    
    #Commands
    @commands.command(aliases=['8ball', 'question'])
    async def _8ball(self, ctx, *, question):
        responses = ['Mhm, I think so',
                    'lol not at all',
                    'maybe? who knows?',
                    'yes ofcourse idiot :/',
                    'definently',
                    'is that even a question? ofcourse my guy',
                    'most likely...',
                    'no',
                    'yes',
                    'ask again later',
                    'ahh im tired, ask another time',
                    'without a doubt',
                    'ofcourse not idiot :/']
        embed2 = discord.Embed(title=f'Question: {question}', description=f'Answer: {random.choice(responses)}')
        await ctx.send(embed=embed2)

    @commands.command()
    async def howgay(self, ctx, *, member: discord.Member=None):
        embed2 = discord.Embed(title='Please specify a member.')
        if not member:
            await ctx.send(embed=embed2)
        if member == "529263654915276821":
            embed4 = discord.Embed(title="Ehhh, That guy is way more than 100 percent gay.")
            await ctx.send(embed=embed4)
        else:
            number = random.sample(range(1,100), 1)
            embed3 = discord.Embed(title=f'{member} is {number} percent gay.')
            await ctx.send(embed=embed3)

    @commands.command()
    async def help_fun(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name='Help Fun')
        embed.add_field(name='8ball', value='Will answer you with a yes or no.', inline=True)    
        embed.add_field(name='HowGay', value='Tells how gay is the mentioned user.', inline=True)
        embed.add_field(name='Meme', value='Shows a random meme from reddit.', inline=True)
        embed.add_field(name='Cat', value='Shows a random picture of a cat from reddit', inline=True)
        embed.add_field(name='Dog', value='Shows a random picture of a dog from reddit', inline=True)
        embed.add_field(name='HowSimp', value='Tells how simp is the mentioned user.', inline=True)
        embed.add_field(name='Echo', value='Repeats what ever you want.', inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        reddit = praw.Reddit(client_id='-Kd0A59wIthySA',
        client_secret='tdG6eR7d09G34jc2z3l6L2POE6lbLQ',
        user_agent='Community-Moderator')

        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        
        embed = discord.Embed(title='MEMEEEEEEEEEE', colour = discord.Colour.green())
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        reddit = praw.Reddit(client_id='-Kd0A59wIthySA',
        client_secret='tdG6eR7d09G34jc2z3l6L2POE6lbLQ',
        user_agent='Community-Moderator')

        cats_submissions = reddit.subreddit('cat').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in cats_submissions if not x.stickied)

        embed = discord.Embed(title='CATTTTTTTT', colour = discord.Colour.purple())
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def dog(self, ctx):
        reddit = praw.Reddit(client_id='-Kd0A59wIthySA',
        client_secret='tdG6eR7d09G34jc2z3l6L2POE6lbLQ',
        user_agent='Community-Moderator')

        dogs_submissions = reddit.subreddit('dog').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in dogs_submissions if not x.stickied)

        
        embed = discord.Embed(title='DOGGGGGGG', colour = discord.Colour.blue())
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def howsimp(self, ctx, *, member: discord.Member=None):
        embed2 = discord.Embed(title='Please specify a member.')
        if not member:
            await ctx.send(embed=embed2)
        else:
            number = random.sample(range(1,100), 1)
            embed3 = discord.Embed(title=f'{member} is {number} percent simp.')
            await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def echo(self, ctx, message):
        await ctx.channel.purge(limit= 1)
        embed = discord.Embed(description=message)
        await ctx.send(embed=embed)




    

def setup(client):
    client.add_cog(fun(client))