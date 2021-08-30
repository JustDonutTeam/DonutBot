import discord
import json
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["ping"]["aliases"])
    async def ping(self, ctx):
        await ctx.reply(f'Pong! {round(self.client.latency * 1000)}ms', mention_author=False)

def setup(client):
    client.add_cog(Ping(client))