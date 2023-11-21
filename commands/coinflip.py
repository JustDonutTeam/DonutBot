import discord
import json
import random
from discord.ext import commands

class Coinflip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["coinflip"]["aliases"])
    async def coinflip(self, ctx):
        coin = random.randint(0, 1)
        result = "tails"

        if coin == 0: result = "heads"

        await ctx.reply(f":coin: Coin landed on **{result}**!", mention_author=False)

async def setup(client):
    await client.add_cog(Coinflip(client))