import discord
import sqlite3
from discord.ext import commands

class On_raw_reaction_remove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member = self.client.get_guild(payload.guild_id).get_member(payload.user_id)

        if payload.user_id == self.client.user.id:
            pass

        else:
            database = sqlite3.connect("database.sqlite")
            cursor = database.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS reactionroles (emoji TEXT, role_id TEXT, message_id TEXT, channel_id TEXT)")
            cursor.execute(f'SELECT * FROM reactionroles WHERE "emoji" = "{payload.emoji}" AND message_id = {payload.message_id}')
            data = cursor.fetchall()

            if data:
                role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id=int(data[0][1]))

                await member.remove_roles(role)


            database.commit()
            cursor.close()
            database.close()

def setup(client):
    client.add_cog(On_raw_reaction_remove(client))