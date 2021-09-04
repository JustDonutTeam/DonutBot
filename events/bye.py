import discord
import sqlite3
import random
from discord.ext import commands

class Member_remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        leave = self.client.get_emoji(881878844871684096)

        database = sqlite3.connect("welcome.sqlite")
        cursor = database.cursor()
        cursor.execute(f"SELECT enabled FROM welcome WHERE guild_id = {member.guild.id}")
        data = cursor.fetchone()

        cursor.execute(f"SELECT channel_id FROM welcome WHERE guild_id = {member.guild.id}")
        channel_id = cursor.fetchone()
        channel = self.client.get_channel(int(channel_id[0]))

        cursor.execute(f"SELECT custom_bye FROM welcome WHERE guild_id = {member.guild.id}")
        custom_bye = cursor.fetchone()

        if str(data[0]) == "1":
            if str(custom_bye[0]) == "0":
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(54, 57, 63),
                    description=str(leave) + " **{user}** has just left the server.".replace("{user}", member.name)
                )
            else:
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(54, 57, 63),
                    description=str(leave) + str(custom_bye[0]).replace("{user}", f" **{member.name}**").replace("{mention}", member.mention).replace("{members}", f"**{len(member.guild.members)}**")
                )
        
            await channel.send(embed=embed)

        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Member_remove(client))