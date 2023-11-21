import discord
import sqlite3
import random
from discord.ext import commands

class On_member_remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        leave = self.client.get_emoji(881878844871684096)
        message = ["**{user}** left the party.", "**{user}** has just left the server.", "**{user}** has just buggered off.", "Goodbye **{user}**! Next time, bring more cookies.", "Goodbye **{user}**! Next time, bring more cookies.", "Smell ya later, **{user}**!", "Don’t forget to send a letter, **{user}**.", "Come back soon, **{user}**.", "See ya, **{user}**!", "See you in another life, **{user}**.", "Goodbye **{user}**! Next time, bring more donuts."]

        database = sqlite3.connect("database.sqlite")
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
                    description=str(leave) + " " + random.choice(message).replace('{user}', member.name)
                )
            else:
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(54, 57, 63),
                    description=str(leave) + " " + str(custom_bye[0]).replace("{user.name}", f"**{member.name}**").replace("{user.mention}", member.mention).replace("{guild.members}", f"**{len(member.guild.members)}**").replace("{guild.name}", f"**{member.guild.name}**")
                )
        
            await channel.send(embed=embed)

        database.commit()
        cursor.close()
        database.close()

async def setup(client):
    await client.add_cog(On_member_remove(client))