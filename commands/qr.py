from io import BytesIO
import discord
import qrcode
import json
from discord.ext import commands

class Qr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["qr"]["aliases"])
    async def qr(self, ctx, input):
        await ctx.trigger_typing()
    
        embed = discord.Embed(
            title = "Here's your QR code!",
            colour = discord.Colour.from_rgb(255, 158, 253),
            timestamp = ctx.message.created_at,
        )

        image = qrcode.make(input)

        fp = BytesIO()
        image.save(fp, "png")
        fp.seek(0)

        embed.set_image(url="attachment://qr.png")
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

        await ctx.reply(embed=embed, file=discord.File(fp, "qr.png"), mention_author=False)

def setup(client):
    client.add_cog(Qr(client))