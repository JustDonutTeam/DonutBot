import discord
import json
from discord.ext import commands

class Nuke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["nuke"]["aliases"])
    @commands.has_permissions(kick_members=True)
    async def nuke(self, ctx, *, destination):

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=f'Nuke has been sent!',
            description=f'**{ctx.author.display_name}** has nuked **{destination}**!',
            timestamp=ctx.message.created_at
        )
        embed.set_image(url='https://i.pinimg.com/originals/6c/48/5e/6c485efad8b910e5289fc7968ea1d22f.gif')
        embed.set_footer(text=f"Donut x North Korea", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Nuke(client))