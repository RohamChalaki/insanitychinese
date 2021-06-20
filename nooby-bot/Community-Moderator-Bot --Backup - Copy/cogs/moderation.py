import discord
from discord import user
from discord import message
from discord.ext import commands
from discord.ext.commands import bot

reaction_channel = 855112024614240267

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation commands are ready...\n-----')


    
    #Commands
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        embed2 = discord.Embed(title='Command: !kick', description='**Description** : Kicks a member\n**Usage** : !kick [user] [reason]\n**Example** : !kick @user reason')
        if not member:
            await ctx.send(embed=embed2)
        await member.kick(reason=reason)
        embed3 = discord.Embed(title=f'{member} was kicked.', description=f'Reason : {reason}')
        await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=0):
        await ctx.channel.purge(limit= amount+1)
        embed = discord.Embed(title=f"{amount} Messages has been deleted.")
        await ctx.send(embed=embed)
        await ctx.channel.purge(limit= 1)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        embed2 = discord.Embed(title='Please specify a member.')
        if not member:
            await ctx.send(embed=embed2)
        await member.ban(reason=reason)
        embed3 = discord.Embed(title=f'{member} was banned.', description=f'Reason : {reason}')
        await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=f'{member} was unbanned')
                await ctx.send(embed=embed)
                return

    
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, *, member: discord.Member=None):
        embed2 = discord.Embed(title='Please specify a member.')
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not member:
            await ctx.send(embed=embed2)
        await member.add_roles(role)
        embed3 = discord.Embed(title=f'{member} was muted.')
        await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, *, member: discord.Member=None):
        embed2 = discord.Embed(title='Please specify a member.')
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not member:
            await ctx.send(embed=embed2)
        await member.remove_roles(role)
        embed3 = discord.Embed(title=f'{member} was unmuted.')
        await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay = seconds)
        embed = discord.Embed(title=f'Slowmode has been changed to {seconds} seconds.')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title=f"This channel has been locked so no one can't talk in it.")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title=f"This channel has been un-locked so everyone can talk in it.")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_nicknames = True)
    async def nick(self, ctx, member: discord.Member, nick):
        embed2 = discord.Embed(title='Please specify a member.')
        if not member:
            await ctx.send(embed=embed2)
        await member.edit(nick=nick)
        embed3 = discord.Embed(title=f"({member})'s Nickname was changed to ({nick})")
        await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unbanall(self, ctx):
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await ctx.guild.unban(user=users.user)
            except:
                pass
        embed = discord.Embed(title=f"Everyone banned person has been unbanned.")
        await ctx.send(embed=embed)

    @commands.command()
    async def help_moderation(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.blue()
        )
        embed.set_author(name='Help Moderation')
        embed.add_field(name='Clear', value='Deletes the amount of messages that you want.', inline=True)
        embed.add_field(name='Kick', value='Kicks a member of your choice.', inline=True)
        embed.add_field(name='Ban', value='Bans a member of your choice.', inline=True)
        embed.add_field(name='UnBan', value='UnBans a member of your choice.', inline=True)
        embed.add_field(name='Mute', value='Mutes a member of your choice.', inline=True)
        embed.add_field(name='UnMute', value='UnMutes a member of your choice.', inline=True)
        embed.add_field(name='SlowMode', value='Sets the slowmode of a channel.', inline=True)
        embed.add_field(name='Lock', value='Makes it so no one can talk in the channel', inline=True)
        embed.add_field(name='UnLock', value='Makes it so everyone can talk in the channel', inline=True)
        embed.add_field(name='Nick', value="Changes someone's nickname.", inline=True)
        embed.add_field(name='UnBanAll', value="Unbans every banned user from the server.", inline=True)
        embed.add_field(name='AddRole', value="Adds a role of your choice to a user.", inline=True)
        embed.add_field(name='TakeRole', value="Removes a role of your choice from a user.", inline=True)
        embed.add_field(name='Message', value="Sends a message from the bot to the mentioned user.", inline=True)
        embed.add_field(name='ReActRole', value="Makes a reaction role | Usage : !reactrole [emoji] [role.mention] [message]", inline=True)

    

        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.dark_green()
        )

        embed.set_author(name='Help')
        embed.add_field(name='Moderation', value="Do **!help_moderation** to recieve the moderation commands.", inline=True)
        embed.add_field(name='Utility', value="Do **!help_util** to recieve the utility commands.", inline=True)
        embed.add_field(name='Fun', value="Do **!help_fun** to recieve the FUNNY commands.", inline=True)
        embed.add_field(name='Music', value="Do **!help_music** to recieve the music commands.", inline=True)
        embed.add_field(name='Levelling', value="Do **!help_level** to recieve the levelling commands.", inline=True)
        embed.add_field(name='Economy', value="Do **!help_economy** to recieve the economy commands.", inline=True)



        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addrole(self, ctx, member: discord.Member = None, *, role:discord.Role = None):
        if not member:
            embed = discord.Embed(title='Please specify a member')
            await ctx.send(embed=embed)
        elif not role:
            embed2 = discord.Embed(title='Please specify a role.')
            await ctx.send(embed=embed2)
        else:
            await ctx.message.delete()
            await member.add_roles(role)
            embed3 = discord.Embed(title=f'Successfuly added the role : {role} | To the User : {member}')
            await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def takerole(self, ctx, member: discord.Member = None, *, role:discord.Role = None):
        if not member:
            embed = discord.Embed(title='Please specify a member')
            await ctx.send(embed=embed)
        elif not role:
            embed2 = discord.Embed(title='Please specify a role.')
            await ctx.send(embed=embed2)
        else:
            await ctx.message.delete()
            await member.remove_roles(role)
            embed3 = discord.Embed(title=f'Successfuly removed the role : {role} | From the User : {member}')
            await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def message(self, ctx, member: discord.Member, *, message):
        if not member:
            embed = discord.Embed(title='Please run the command like this: !message @user (message)')
            await ctx.send(embed=embed)
        embed2 = discord.Embed(title=f"{message}")
        await member.send(embed=embed2)
        embed3 = discord.Embed(title=f"Successfuly sent the message to {member}")
        await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def roleall(self, ctx, role:discord.Role = None):
        everyone = ctx.guild.members
        if not role:
            embed2 = discord.Embed(title='Please specify a role.')
            await ctx.send(embed=embed2)
        else:
            await ctx.message.delete()
            await everyone.add_roles(role)
            embed3 = discord.Embed(title=f'Successfuly added the role : {role} | To everyone')
            await ctx.send(embed=embed3)






        

def setup(client):
    client.add_cog(moderation(client))