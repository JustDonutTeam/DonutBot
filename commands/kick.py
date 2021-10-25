import discord
import json
from discord.ext import commands

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["kick"]["aliases"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        leave = self.client.get_emoji(881870169918562345)
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            description=f'{leave} **{member}** has been kicked!',
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Kick(client))