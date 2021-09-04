import discord
import random
import sqlite3
from discord.ext import commands

class On_guild_join(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM notify")
        data = cursor.fetchall()

        hello = ["Yo {user}, what's up? ", "Hey {user}, ", "Hello {user}. ", "Hi!"]

        #if len(self.client.guilds) == 100:
        for user_id in data:
            await self.client.get_user(int(user_id[0])).send(random.choice(hello).replace("{user}", self.client.get_user(int(user_id[0])).name) + "I have joined 100 servers and can't join any more now.")

        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(On_guild_join(client))