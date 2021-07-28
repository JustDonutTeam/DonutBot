import discord
import json
from discord.ext import commands

class Iamspeed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["iamspeed"]["aliases"])
    async def iamspeed(self, ctx, member : discord.Member = None):

        if not member: member = ctx.author

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at
        )
        embed.set_image(url=f'https://vacefron.nl/api/iamspeed?user={member.avatar_url_as(format="png")}')
        embed.set_footer(text="Donut x Vacefron API", icon_url=self.client.get_user(738788356506386462).avatar_url)
        

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Iamspeed(client))