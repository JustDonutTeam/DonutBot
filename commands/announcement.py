import discord
import json
from discord.ext import commands

class Announcement(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["announcement"]["aliases"])
    @commands.has_permissions(manage_channels=True)
    async def announcement(self, ctx, channel : discord.TextChannel, *, text):

        announcement = self.client.get_emoji(869949639997136976)

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=f"{announcement} Announcement",
            description=f"{text}",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await channel.send(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Announcement(client))