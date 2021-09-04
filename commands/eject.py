import discord
import json
from discord.ext import commands

class Eject(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["eject"]["aliases"])
    async def eject(self, ctx, color, impostor, member : discord.Member = None):
        member = ctx.author if not member else member
        username = member.display_name.replace(' ', '%20')

        colors = ['black','blue','brown','cyan','darkgreen','lime','orange','pink','purple','red','white','yellow']

        if impostor.lower() == "yes" or impostor == "1" or impostor.lower() == "true": impostor = True
        if impostor.lower() == "no" or impostor == "0" or impostor.lower() == "false": impostor = False

        if color.lower() in colors:
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                timestamp = ctx.message.created_at
            )
            embed.set_image(url=f'https://vacefron.nl/api/ejected?name={username}&impostor={impostor}&crewmate={color}')
            embed.set_footer(text="Donut x Vacefron API", icon_url=self.client.get_user(738788356506386462).avatar_url)
        

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Eject(client))