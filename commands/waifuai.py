import discord
import json
import random
from discord.ext import commands

class Waifuai(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["waifuai"]["aliases"])
    async def waifuai(self, ctx):

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=f"Here's your waifu!",
            description="Remember that these images are AI generated!",
            timestamp=ctx.message.created_at
        )
        embed.set_image(url="https://www.thiswaifudoesnotexist.net/example-"+str(random.randint(1,100000))+".jpg")
        embed.set_footer(text=f"Donut x ThisWaifuDoesNotExist.net", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Waifuai(client))