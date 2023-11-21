import discord
import json
from discord.ext import commands

class Tohex(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["tohex"]["aliases"])
    async def tohex(self, ctx, *, input):
        await ctx.trigger_typing()

        output = input.encode('utf-8').hex()
        output = ' '.join([output[i:i+2] for i in range(0, len(output), 2)])
        await ctx.reply(output, mention_author=False)

async def setup(client):
    await client.add_cog(Tohex(client))