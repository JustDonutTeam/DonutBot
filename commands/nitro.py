import discord
import json
from discord.ext import commands

class Nitro(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["nitro"]["aliases"])
    async def nitro(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Claim your free Nitro today!",
            description="Click [**[this]**](https://bit.ly/3zCSQqL) link to get a month of Nitro Classic for free!",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut x Discord Nitro", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Nitro(client))