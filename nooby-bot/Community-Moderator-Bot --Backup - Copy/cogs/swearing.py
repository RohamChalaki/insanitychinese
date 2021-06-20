import discord
from discord.ext import commands

with open('C:\\Users\\roham\\OneDrive\\Desktop\\Community-Moderator-Bot --Backup - Copy\\cogs\\badWords.txt', 'r') as f:
    global badwords  # You want to be able to access this throughout the code
    words = f.read()
    badwords = words.split()


class swearing(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Swearing system is ready...\n-----')


    @commands.Cog.listener()
    async def on_message(ctx, message):
        msg = message.content
        for word in badwords:
            if word in msg:
                await message.delete()
            


    
    

    #Commands

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def swearing(self, ctx):
        embed = discord.Embed(title="Swearing system is working.")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(swearing(client))