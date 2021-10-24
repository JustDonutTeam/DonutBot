import discord
import json
import requests
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

class Location(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["location"]["aliases"])
    async def location(self, ctx, member : discord.Member):
        await ctx.trigger_typing()
        text = member.display_name + " wants to:"

        asset = requests.get("https://i.imgur.com/kghLu6w.png")
        uno = Image.open(BytesIO(asset.content))

        draw = ImageDraw.Draw(uno)
        font = ImageFont.truetype("./fonts/Arial.ttf", 25)

        x = 36
        y = 25

        draw.text((x, y), text, (50, 50, 50), font=font)

        fp = BytesIO()
        uno.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://location.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(self.client.user.id).avatar_url)

        await ctx.reply(embed=embed, file=discord.File(fp, "location.png"), mention_author=False)

def setup(client):
    client.add_cog(Location(client))