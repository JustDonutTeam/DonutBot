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
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        errors = 0
        wb_data = ""
        rr_data = ""
        data = []

        try:
            cursor.execute(f"SELECT * FROM welcome WHERE guild_id = {ctx.guild.id}")
            wb_data = cursor.fetchone()
            data.append(dict(zip(["enabled", "guild_id", "channel_id", "custom_welcome", "custom_bye"], wb_data)))
        except OperationalError:
            errors += 1
            pass

        try:
            cursor.execute(f"SELECT * FROM reactionroles WHERE guild_id = {ctx.guild.id}")
            rr_data = cursor.fetchall()

            for item in rr_data:
                data.append(dict(zip(["emoji", "role_id", "message_id", "channel_id", "guild_id"], item)))

        except OperationalError:
            errors += 1
            pass

        if errors >= 2:
            raise ValueError

        if data:
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"Here's your data!",
                    description=f"```json\n{json.dumps(data, indent=1)}```",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(self.client.user.id).avatar_url)

            await ctx.reply(embed=embed, mention_author=False)

            
        
        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Data(client))