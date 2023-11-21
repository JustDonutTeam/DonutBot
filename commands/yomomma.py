import discord
import json
import requests
from discord.ext import commands

class Yomomma(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["yomomma"]["aliases"])
    async def yomomma(self, ctx):
        api = requests.get("https://api.yomomma.info/")
        api = api.json()
        await ctx.reply(api["joke"], mention_author=False)

async def setup(client):
    await client.add_cog(Yomomma(client))