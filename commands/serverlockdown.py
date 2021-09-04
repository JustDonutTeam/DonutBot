import discord
import json
from discord.ext import commands

class Serverlockdown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["serverlockdown"]["aliases"])
    @commands.has_permissions(administrator=True)
    async def serverlockdown(self, ctx):

        if ctx.guild.default_role not in ctx.channel.overwrites:
            for channel in ctx.guild.text_channels:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
                }
                await channel.edit(overwrites=overwrites)
            await ctx.send(f'🔒 I have put `{ctx.guild.name}` on lockdown.')

        elif ctx.channel.overwrites[ctx.guild.default_role].send_messages == True or ctx.channel.overwrites[ctx.guild.default_role].send_messages == None:
            for channel in ctx.guild.text_channels:
                overwrites = channel.overwrites[ctx.guild.default_role]
                overwrites.send_messages = False
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.reply(f'🔒 I have put `{ctx.guild.name}` on lockdown.', mention_author=False)
            
        else:
            for channel in ctx.guild.text_channels:
                overwrites = channel.overwrites[ctx.guild.default_role]
                overwrites.send_messages = True
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.reply(f'🔓 I have removed `{ctx.guild.name}` from lockdown.', mention_author=False)

def setup(client):
    client.add_cog(Serverlockdown(client))