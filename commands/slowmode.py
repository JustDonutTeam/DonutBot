import discord
import json
from discord.ext import commands

class Slowmode(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["slowmode"]["aliases"])
    @commands.has_permissions(manage_channels = True)
    async def slowmode(self, ctx, seconds, channel : discord.TextChannel = None):
        if not channel: channel = ctx.channel
        emoji = self.client.get_emoji(883738406402818098)

        await channel.edit(slowmode_delay = int(seconds))

        await ctx.reply(f"{emoji} Successfully set the slowmode in {channel.mention} to {seconds}s!", mention_author=False)

def setup(client):
    client.add_cog(Slowmode(client))