import discord
import json
import requests
from discord.ext import commands

class Cat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["cat"]["aliases"])
    async def cat(self, ctx):
        await ctx.trigger_typing()
        
        api = requests.get('https://some-random-api.ml/img/cat').json()
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Here's your cat picture!", 
            timestamp=ctx.message.created_at
            )
        embed.set_image(url=api["link"])
        embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Cat(client))