import discord
import json
from discord.ext import commands

class Tweet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["tweet"]["aliases"])
    async def tweet(self, ctx, comment, member : discord.Member = None):
        
        if member == None: member = ctx.author

        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at
        )

        embed.set_image(url=f"https://some-random-api.ml/canvas/tweet?comment={comment}&displayname={member.display_name}&username={member.name}avatar={str(member.avatar_url).replace('webp', 'png')}")
        embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)
    
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Tweet(client))