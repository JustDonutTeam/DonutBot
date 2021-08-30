import discord
import json
from discord.ext import commands

class Serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["serverinfo"]["aliases"])
    async def serverinfo(self, ctx):
        owner = self.client.get_emoji(881889987539386378)
        channels = self.client.get_emoji(881890493095632936)
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp=ctx.message.created_at
        )
        embed.set_author(name="Info about " + str(ctx.guild.name), icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)


        embed.add_field(name=":date: Created At:", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=":id: ID:", value=ctx.guild.id)
        embed.add_field(name=":busts_in_silhouette: Members", value=len(ctx.guild.members))
        embed.add_field(name=f"{owner} Server Owner:", value=ctx.guild.owner)
        embed.add_field(name=f"{channels} Text Channels:", value=len(ctx.guild.text_channels))
        embed.add_field(name=":flag_white: Region:", value=ctx.guild.region)
        if ctx.guild.banner_url:
            embed.set_image(url=str(ctx.guild.banner_url))
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Serverinfo(client))