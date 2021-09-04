import discord
import json
import sqlite3
from discord.ext import commands

class Disable(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["disable"]["aliases"])
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx):
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        cursor.execute(f"SELECT enabled FROM welcome WHERE guild_id = {ctx.guild.id}")
        data = cursor.fetchone()

        if str(data[0]) == "1":
            success = self.client.get_emoji(883738376866516992)
            cursor.execute("UPDATE welcome SET enabled = ? WHERE guild_id = ?", (0, ctx.guild.id))
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"{success} Success!",
                    description=f"Successfully disabled welcome-bye messages!\n\nRemember that using `.enable` will overwrite previous settings!",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(738788356506386462).avatar_url)
            await ctx.reply(embed = embed, mention_author = False)
        else:
            raise TypeError("welcome-bye messages are already disabled.")

        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Disable(client))