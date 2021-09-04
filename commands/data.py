from sqlite3.dbapi2 import OperationalError
import discord
import json
import sqlite3
from discord.ext import commands

class Data(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["data"]["aliases"])
    @commands.has_permissions(administrator=True)
    async def data(self, ctx):
        database = sqlite3.connect("welcome.sqlite")
        cursor = database.cursor()
        try:
            cursor.execute(f"SELECT * FROM welcome WHERE guild_id = {ctx.guild.id}")
            data = cursor.fetchone()
        except OperationalError:
            raise KeyError("I have no data about your server!")

        data = dict(zip(["enabled", "guild_id", "channel_id", "custom_welcome", "custom_bye"], data))

        if data:
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"Here's your data!",
                    description=f"```json\n{json.dumps(data, indent=1)}```",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(738788356506386462).avatar_url)

            await ctx.reply(embed=embed, mention_author=False)

            
        
        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Data(client))