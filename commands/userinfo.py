import discord
import json
from discord.ext import commands

class Userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["userinfo"]["aliases"])
    async def userinfo(self, ctx, member : discord.Member = None):

        if not member: member = ctx.author

        online = self.client.get_emoji(869949554739523625)
        dnd = self.client.get_emoji(869949528185389056)
        idle = self.client.get_emoji(869949583285968897)
        offline = self.client.get_emoji(869949610838351882)
        rpc = self.client.get_emoji(869949664517034024)

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp=ctx.message.created_at
        )
        embed.set_author(name="Info about " + str(member), icon_url=member.avatar_url)
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)

        if member.status == discord.Status.dnd:
            status = dnd
        elif member.status == discord.Status.idle:
            status = idle
        elif member.status == discord.Status.online:
            status = online
        elif member.status == discord.Status.offline:
            status = offline

        embed.add_field(name=":date: Account Created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=":id: ID:", value=member.id)
        embed.add_field(name=":busts_in_silhouette: Highest Role", value=member.top_role.mention)
        embed.add_field(name=":bust_in_silhouette: Nickname", value=member.display_name)
        embed.add_field(name=f"{status} Status:", value=str(member.status))
        if member.activities:
            embed.add_field(name=f"{rpc} Activity:", value=member.activities[0].name)
        else:
            embed.add_field(name=f"{rpc} Activity:", value="None")
        
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Userinfo(client))