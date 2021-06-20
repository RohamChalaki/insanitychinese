import discord
from discord.ext import commands

class logs(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Log system is ready...\n-----')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        content = message.content
        channel = message.channel
        print('Someone Sent a message\nChannel : {}\nAuthor : {}\nMessage : {}\n------------------'.format(channel, author, content))

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        author = message.author
        content = message.content
        channel = message.channel
        print('Someone Deleted a message\nChannel : {}\nAuthor : {}\nMessage : {}\n------------------'.format(channel, author, content))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        author = reaction.message.author
        content = reaction.message.content
        channel = reaction.message.channel
        print('Someone Added a reaction\nChannel : {}\nReactionAdder : {}\nMessage : {}\nReactionEmoji : {}\n------------------'.format(channel, user.name, reaction.message.content, reaction.emoji ))

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        author = reaction.message.author
        content = reaction.message.content
        channel = reaction.message.channel
        print('Someone Removed a reaction\nChannel : {}\nReactionRemover : {}\nMessage : {}\nReactionEmoji : {}\n------------------'.format(channel, user.name, reaction.message.content, reaction.emoji ))



    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} Has joined the server.\n------------------')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} Has left the server.\n------------------')



    #Commands

    @commands.command(aliases=['logs'])
    @commands.has_permissions(administrator = True)
    async def log(self, ctx):
        embed = discord.Embed(title="Log system is working.")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(logs(client))