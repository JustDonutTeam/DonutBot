import discord
import requests
import json
from discord.ext import commands

class Wink(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["wink"]["aliases"])
    async def wink(self, ctx, member : discord.Member = None):
        
        await ctx.trigger_typing()
        if member == None: member = ctx.author

        if ctx.author.id == member.id: desc = f"**{ctx.author.display_name}** winked at **themself**!?" 
        else: desc = f"**{ctx.author.display_name}** winked at **{member.display_name}**!"

        embed = discord.Embed(
            description = desc,
            colour = discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at
        )

        api = requests.get("https://some-random-api.ml/animu/wink").json()

        embed.set_image(url=api["link"])
        embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(self.client.user.id).avatar_url)
        

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Wink(client))