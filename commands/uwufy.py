import discord
import json
from discord.ext import commands

class Uwufy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["uwufy"]["aliases"])
    async def uwufy(self, ctx, *, phrase):
        uwufied = phrase.replace('rl', 'w').replace('RL', 'W').replace('ove', 'uv').replace('the', 'dee').replace('r', 'w')
        await ctx.reply(uwufied)

def setup(client):
    client.add_cog(Uwufy(client))