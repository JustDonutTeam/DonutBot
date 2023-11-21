import discord
import json
import requests
from discord.ext import commands
from PIL import Image
from io import BytesIO

class Pooh(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["pooh"]["aliases"])
    async def pooh(self, ctx, user1 : discord.User, user2 : discord.User):
        await ctx.trigger_typing()

        asset = user1.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp1 = Image.open(data)

        asset = user2.avatar_url_as(size=128, format="png")
        data = BytesIO(await asset.read())
        pfp2 = Image.open(data)

        asset = requests.get("https://i.imgur.com/50Zc61G.png")
        pooh = Image.open(BytesIO(asset.content))

        pfp1 = pfp1.resize((230, 230))
        pfp2 = pfp2.resize((230, 230))

        pooh.paste(pfp1, (456, 33))
        pooh.paste(pfp2, (456, 320))

        fp = BytesIO()
        pooh.save(fp, "png")
        fp.seek(0)

        embed = discord.Embed(
                colour = discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
        embed.set_image(url="attachment://pooh.png")
        embed.set_footer(text="Donut x PIL", icon_url=self.client.get_user(738788356506386462).avatar_url)

        await ctx.reply(embed=embed, file=discord.File(fp, "pooh.png"), mention_author=False)

async def setup(client):
    await client.add_cog(Pooh(client))