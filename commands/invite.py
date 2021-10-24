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
            description=f"You can invite me [[here]](https://discord.com/api/oauth2/authorize?client_id=self.client.user.id&permissions=8&scope=bot). Remaining places: **{100-len(self.client.guilds)}**",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Invite(client))