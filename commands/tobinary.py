import discord
import json
import requests
from discord.ext import commands

class Tobinary(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["tobinary"]["aliases"])
    async def tobinary(self, ctx, *, input):
        await ctx.trigger_typing()

        api = requests.get(f"https://some-random-api.ml/binary?encode={input}")
        api = api.json()
        output = ' '.join([api["binary"][i:i+8] for i in range(0, len(api["binary"]), 8)])
        await ctx.reply(output, mention_author=False)

def setup(client):
    client.add_cog(Tobinary(client))