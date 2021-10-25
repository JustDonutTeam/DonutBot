import discord
import json
import requests
from discord.ext import commands
from PIL import Image
from io import BytesIO

class Drake(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["drake"]["aliases"])
    async def drake(self, ctx, user1 : discord.User, user2 : discord.User):
        await ctx.trigger_typing()

        asset = user1.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp1 = Image.open(data)

        asset = user2.avatar_url_as(size=128, format="png")
        data = BytesIO(await asset.read())
        pfp2 = Image.open(data)

        asset = requests.get("https://i.imgur.com/garOUxb.jpg")
        drake = Image.open(BytesIO(asset.content))

        pfp1 = pfp1.resize((95, 95))
        pfp2 = pfp2.resize((95, 95))

        drake.paste(pfp1, (141, 11))
        drake.paste(pfp2, (141, 143))

        fp = BytesIO()
        drake.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://drake.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

        await ctx.reply(embed=embed, file=discord.File(fp, "drake.png"), mention_author=False)

def setup(client):
    client.add_cog(Drake(client))