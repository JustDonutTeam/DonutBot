import discord
import json
import requests
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

class Worthless(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["worthless"]["aliases"])
    async def worthless(self, ctx, *, text):
        await ctx.trigger_typing()

        asset = requests.get("https://i.imgur.com/JdujF4G.jpg")
        uno = Image.open(BytesIO(asset.content))

        draw = ImageDraw.Draw(uno)
        font = ImageFont.truetype("./fonts/Arial.ttf", 30)

        x = 98
        y = 80

        split_strings = []

        for index in range(0, len(text), 25):
            split_strings.append(text[index : index + 25])

        for line in split_strings:
            draw.text((x, y), line, (0, 0, 0), font=font)
            y += 30

        fp = BytesIO()
        uno.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://worthless.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed=embed, file=discord.File(fp, "worthless.png"), mention_author=False)

def setup(client):
    client.add_cog(Worthless(client))