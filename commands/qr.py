import discord
import requests
import json
from discord.ext import commands

class Qr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["qr"]["aliases"])
    async def qr(self, ctx, url):
        await ctx.trigger_typing()
    

        embed = discord.Embed(
            title = "Here's your QR code!",
            colour = discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at,
            url = url
        )

        embed.set_image(url=f"https://qrtag.net/api/qr.png?url={url}")
        embed.set_footer(text="Donut x QRTag.net", icon_url=self.client.get_user(738788356506386462).avatar_url)
        

        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Qr(client))