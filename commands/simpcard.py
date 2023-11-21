import discord
import json
import io
import aiohttp
from discord.ext import commands

class Simpcard(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["simpcard"]["aliases"])
    async def simpcard(self, ctx, member : discord.Member = None):
        await ctx.trigger_typing()
        if not member: member = ctx.author

        async with aiohttp.ClientSession() as session:

            async with session.get(
                f"https://some-random-api.ml/canvas/simpcard?avatar={member.avatar_url_as(format='png')}"
            ) as af:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "simpcard.png")
                embed = discord.Embed(
                    colour = discord.Colour.from_rgb(255, 158, 253),
                    timestamp = ctx.message.created_at
                )
                embed.set_image(url="attachment://simpcard.png")
                embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)
                await ctx.reply(embed=embed, file=file, mention_author=False)

        await session.close() 

async def setup(client):
    await client.add_cog(Simpcard(client))