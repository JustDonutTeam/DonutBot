import discord
import json
import requests
from discord.ext import commands

class Frombinary(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["frombinary"]["aliases"])
    async def frombinary(self, ctx, *, input):
        await ctx.trigger_typing()

        api = requests.get(f"https://some-random-api.ml/binary?decode={input.replace(' ', '')}")
        api = api.json()
        await ctx.reply(api["text"], mention_author=False)

def setup(client):
    client.add_cog(Frombinary(client))