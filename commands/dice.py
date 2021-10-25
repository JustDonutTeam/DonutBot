import discord
import json
import random
from discord.ext import commands

class Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["dice"]["aliases"])
    async def dice(self, ctx):

        result = random.randint(1, 6)

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=':game_die: Dice rolled...',
            description=f"The dice has rolled to the number {result}!",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Dice(client))