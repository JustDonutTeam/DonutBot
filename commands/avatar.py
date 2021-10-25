import discord
import json
from discord.ext import commands

class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["avatar"]["aliases"])
    async def avatar(self, ctx, *, member : discord.Member = None):

        await ctx.trigger_typing()
        if not member: member = ctx.author

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp=ctx.message.created_at
        )
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Avatar(client))