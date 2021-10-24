import discord
import json
import requests
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

class Bernie(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["bernie"]["aliases"])
    async def bernie(self, ctx, *, text):
        await ctx.trigger_typing()

        asset = requests.get("https://i.imgur.com/GfwqVtL.jpg")
        uno = Image.open(BytesIO(asset.content))

        draw = ImageDraw.Draw(uno)
        font = ImageFont.truetype("./fonts/ArialBold.ttf", 42)

        x = 33
        y = 650

        split_strings = []

        for index in range(0, len(text), 33):
            split_strings.append(text[index : index + 33])

        for line in split_strings:
            draw.text((x, y), line, (255, 255, 255), font=font)
            y += 40

        fp = BytesIO()
        uno.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://bernie.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(self.client.user.id).avatar_url)

        await ctx.reply(embed=embed, file=discord.File(fp, "bernie.png"), mention_author=False)

def setup(client):
    client.add_cog(Bernie(client))