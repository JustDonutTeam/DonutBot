import discord
import json
import requests
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO

class Yeet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["yeet"]["aliases"])
    async def yeet(self, ctx, *, text):
        await ctx.trigger_typing()

        asset = requests.get("https://i.imgur.com/pFbPHlp.png")
        meme = Image.open(BytesIO(asset.content)).convert("RGBA")

        txt = Image.new('RGBA', (300, 300), (255, 255, 255, 255))

        draw = ImageDraw.Draw(txt)
        font = ImageFont.truetype("./fonts/Arial.ttf", 30)

        x = 1
        y = 1

        split_strings = []

        for index in range(0, len(text), 20):
            split_strings.append(text[index : index + 20])

        for line in split_strings:
            draw.text((x, y), line, (0, 0, 0, 255), font=font)
            y += 30

        rotated = txt.rotate(angle=20, expand=True, fillcolor=(0, 0, 0, 0))

        meme.paste(rotated, (1015, 300), rotated)

        fp = BytesIO()
        meme.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://yeet.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(self.client.user.id).avatar_url)

        await ctx.reply(embed=embed, file=discord.File(fp, "yeet.png"), mention_author=False)

def setup(client):
    client.add_cog(Yeet(client))