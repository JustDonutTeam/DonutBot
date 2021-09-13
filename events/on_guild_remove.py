import discord
import random
import sqlite3
from discord.ext import commands

class On_guild_remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notify (user_id TEXT)")
        cursor.execute(f"SELECT * FROM notify")
        data = cursor.fetchall()

        hello = ["Yo {user}, what's up? ", "Hey {user}, ", "Hello {user}. ", "Hi! "]

        if len(self.client.guilds) == 99:
            for user_id in data:
                await self.client.get_user(int(user_id[0])).send(random.choice(hello).replace("{user}", self.client.get_user(int(user_id[0])).name) + "I have just a left a server and you're now able to invite me!")

        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(On_guild_remove(client))