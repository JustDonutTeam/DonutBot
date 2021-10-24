import discord
import json
import requests
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

class Draw25(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["draw25"]["aliases"])
    async def draw25(self, ctx, user : discord.User, *, text):
        await ctx.trigger_typing()

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp1 = Image.open(data)

        asset = requests.get("https://i.imgur.com/1poVpuP.jpg")
        uno = Image.open(BytesIO(asset.content))

        pfp1 = pfp1.resize((100, 100))

        uno.paste(pfp1, (465, 85))
        draw = ImageDraw.Draw(uno)
        font = ImageFont.truetype("./fonts/BaksoSapi.ttf", 30)

        x = 130
        y = 220

        split_strings = []

        for index in range(0, len(text), 11):
            split_strings.append(text[index : index + 11])

        for line in split_strings:
            draw.text((x, y), line, (0, 0, 0), font=font)
            x -= 30
            y += 50

        fp = BytesIO()
        uno.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://draw25.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(self.client.user.id).avatar_url)

        await ctx.reply(embed=embed, file=discord.File(fp, "draw25.png"), mention_author=False)

def setup(client):
    client.add_cog(Draw25(client))