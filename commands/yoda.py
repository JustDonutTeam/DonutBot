import discord
import json
import requests
from discord.ext import commands

class Yoda(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["yoda"]["aliases"])
    async def yoda(self, ctx, *, phrase):
        api = requests.get(f"http://yoda-api.appspot.com/api/v1/yodish?text={phrase}")
        api = api.json()
        await ctx.reply(api["yodish"])

def setup(client):
    client.add_cog(Yoda(client))