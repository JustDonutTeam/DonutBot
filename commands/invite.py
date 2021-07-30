import discord
import json
from discord.ext import commands

class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["invite"]["aliases"])
    async def invite(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Invite Donut to your server!",
            description="You can invite me [[here]](https://discord.com/api/oauth2/authorize?client_id=738788356506386462&permissions=8&scope=bot).",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Invite(client))