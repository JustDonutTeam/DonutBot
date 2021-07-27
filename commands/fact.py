import discord
import json
import requests
from discord.ext import commands

class Fact(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["fact"]["aliases"])
    async def fact(self, ctx):

        await ctx.trigger_typing()
        api = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=':books: Did you know?', 
            description=api["text"],
            timestamp=ctx.message.created_at
            )
        embed.set_footer(text="Donut x Random Useless Facts API", icon_url=self.client.get_user(738788356506386462).avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fact(client))