import discord
import json
from requests.utils import quote
from discord.ext import commands

class Triggered(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["triggered"]["aliases"])
    async def triggered(self, ctx, member : discord.Member = None):
        
        if member == None: member = ctx.author

        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at
        )

        embed.set_image(url=f"https://some-random-api.ml/canvas/triggered?avatar={quote(str(member.avatar_url).replace('webp', 'png'), safe='')}")
        await ctx.send(f"https://some-random-api.ml/canvas/triggered?avatar={quote(str(member.avatar_url).replace('webp', 'png'), safe='')}")
        embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)
    
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Triggered(client))