import discord
import json
from discord.ext import commands

class Support(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["support"]["aliases"])
    async def support(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Join Donut's support server!",
            description="Click [[this]](https://discord.gg/GAPYQa9) link to join!",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Support(client))