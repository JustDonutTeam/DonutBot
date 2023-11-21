import discord
import sqlite3
from discord.ext import commands

class On_raw_reaction_add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.id == self.client.user.id:
            pass

        else:
            database = sqlite3.connect("database.sqlite")
            cursor = database.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS reactionroles (emoji TEXT, role_id TEXT, message_id TEXT, channel_id TEXT)")
            cursor.execute(f'SELECT * FROM reactionroles WHERE "emoji" = "{payload.emoji}" AND message_id = {payload.message_id}')
            data = cursor.fetchall()

            if data:
                role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id=int(data[0][1]))

                await payload.member.add_roles(role)


            database.commit()
            cursor.close()
            database.close()

async def setup(client):
    await client.add_cog(On_raw_reaction_add(client))