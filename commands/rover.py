import discord
import requests
import json
import random
from discord.ext import commands

class Rover(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["rover"]["aliases"])
    async def rover(self, ctx, sol = "1000"):
        
        await ctx.trigger_typing()
        api = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key=S4hYTUEMT9xPsqB9fC3bhEr7q2g5gMwSHkG2YGHI")
        api = api.json()
        
        number = random.randint(0, len(api["photos"]))

        embed = discord.Embed(
            title = api["photos"][number]["camera"]["full_name"] + " | " + api["photos"][number]["rover"]["name"],
            colour = discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at
        )


        embed.set_image(url=api["photos"][number]["img_src"])
        embed.set_footer(text="Donut x NASA API", icon_url=self.client.get_user(738788356506386462).avatar_url)
        

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Rover(client))