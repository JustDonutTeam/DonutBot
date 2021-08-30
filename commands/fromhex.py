import discord
import json
from discord.ext import commands

class Fromhex(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["fromhex"]["aliases"])
    async def fromhex(self, ctx, *, input):
        await ctx.trigger_typing()

        output = input.replace("0x", "")
        output = output.replace(" ", "")

        output = bytes.fromhex(output)
        output = output.decode("ASCII")

        await ctx.reply(output, mention_author=False)
        

def setup(client):
    client.add_cog(Fromhex(client))