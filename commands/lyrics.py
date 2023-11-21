import discord
import json
import requests
from discord.ext import commands

class Lyrics(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["lyrics"]["aliases"])
    async def lyrics(self, ctx, *, song):
        await ctx.trigger_typing()

        api = api = requests.get(f"https://some-random-api.ml/lyrics?title={song}")
        api = api.json()

        author = api["author"]
        title = api["title"]
        lyrics = api["lyrics"]
        pic = api["thumbnail"]["genius"]

        embed = discord.Embed(
            title=f'Title: `{title}` By: `{author}`',
            description=lyrics, 
            color=discord.Colour.from_rgb(255, 158, 253)
        )
        embed.set_thumbnail(url=f"{pic}")
        embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed = embed, mention_author=False)

async def setup(client):
    await client.add_cog(Lyrics(client))