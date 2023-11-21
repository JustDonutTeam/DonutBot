import discord
import sqlite3
import random
from discord.ext import commands

class On_member_join(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join = self.client.get_emoji(881582462038323232)
        messages = ["Good to see you, **{user}**.", "Yay you made it, **{user}**!", "**{user}** just landed.", "Welcome, **{user}**. We hope you brought pizza.", "Glad you're here, **{user}**.", "Welcome **{user}**. Say hi!", "Everyone welcome **{user}**!", "**{user}** just slid into the server.", "**{user}** joined the party.", "**{user}** hopped into the server.", "**{user}** just showed up!", "Good to see you, **{user}**.", "A wild **{user}** appeared.", "**{user}** is here."]

        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        cursor.execute(f"SELECT enabled FROM welcome WHERE guild_id = {member.guild.id}")
        data = cursor.fetchone()

        cursor.execute(f"SELECT channel_id FROM welcome WHERE guild_id = {member.guild.id}")
        channel_id = cursor.fetchone()

        if not isinstance(channel_id[0], str):
            return
            
        channel = self.client.get_channel(int(channel_id[0]))
            

        cursor.execute(f"SELECT custom_welcome FROM welcome WHERE guild_id = {member.guild.id}")
        custom_welcome = cursor.fetchone()

        if str(data[0]) == "1":
            if str(custom_welcome[0]) == "0":
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(54, 57, 63),
                    description=str(join) + " " + random.choice(messages).replace("{user}", member.name)
                )
            else:
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(54, 57, 63),
                    description=str(join) + " " + str(custom_welcome[0]).replace("{user.name}", f" **{member.name}**").replace("{user.mention}", member.mention).replace("{guild.members}", f"**{len(member.guild.members)}**").replace("{guild.name}", f"**{member.guild.name}**")
                )
        
            await channel.send(embed=embed)

        database.commit()
        cursor.close()
        database.close()

async def setup(client):
    await client.add_cog(On_member_join(client))