import discord
import json
from discord.ext import commands

class Mind(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["mind"]["aliases"])
    async def mind(self, ctx, *, text):

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at
        )
        embed.set_image(url=f'https://vacefron.nl/api/changemymind?text={text.replace(" ", "%20")}')
        embed.set_footer(text="Donut x Vacefron API", icon_url=self.client.get_user(738788356506386462).avatar_url)
        

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Mind(client))