import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import bot


class autorole(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Auto-role system is ready...\n-----')
    
    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     role = discord.utils.get(member.server.roles, name='member')
    #     await bot.add_roles(member, role)




    #Commands

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def autorole(self, ctx):
        embed = discord.Embed(title="Auto-role system is working.")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(autorole(client))