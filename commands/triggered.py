import discord
import json
import io
import aiohttp
from discord.ext import commands

class Triggered(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["triggered"]["aliases"])
    async def triggered(self, ctx, member : discord.Member = None):
        
        if member == None: member = ctx.author

        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png', size=1024)}"
            ) as af:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "triggered.png")
                embed = discord.Embed(
                    colour = discord.Colour.from_rgb(255, 158, 253),
                    timestamp = ctx.message.created_at
                )
                embed.set_image(url="attachment://triggered.png")
                embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(self.client.user.id).avatar_url)
                await ctx.reply(embed=embed, file=file, mention_author=False)
        await session.close()

def setup(client):
    client.add_cog(Triggered(client))