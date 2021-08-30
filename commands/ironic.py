import discord
import json
import random
from discord.ext import commands

class Ironic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["ironic"]["aliases"])
    async def ironic(self, ctx, *, sentence):
        result = ''
        for letter in sentence:
            uporlow = random.randint(0, 1)
            if uporlow == 0:
                result = result + letter.upper()
            else:
                result = result + letter.lower()
        await ctx.reply(result, mention_author=False)

def setup(client):
    client.add_cog(Ironic(client))