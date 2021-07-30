import discord
import json
from discord.ext import commands

class Comrade(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["comrade"]["aliases"])
    async def comrade(self, ctx, member : discord.Member = None):

        await ctx.trigger_typing()
        if not member: member = ctx.author

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp=ctx.message.created_at
        )
        embed.set_image(url=f'https://some-random-api.ml/canvas/comrade?avatar={member.avatar_url_as(format="png")}')
        embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Comrade(client))