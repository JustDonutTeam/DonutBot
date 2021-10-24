import discord
import json
import sqlite3
from discord.ext import commands

class Notify(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["notify"]["aliases"])
    async def notify(self, ctx):
        success = self.client.get_emoji(883738376866516992)
        
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notify (user_id TEXT)")
        cursor.execute(f"SELECT user_id FROM notify WHERE user_id = {str(ctx.author.id)}")
        data = cursor.fetchone()

        if not data:
            cursor.execute("INSERT INTO notify(user_id) VALUES(?)", (str(ctx.author.id), ))
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"{success} Success!",
                    description=f"I will DM you when there's a server available!",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(self.client.user.id).avatar_url)
            await ctx.reply(embed = embed, mention_author = False)

        else:
            cursor.execute(f"DELETE from notify WHERE user_id = {str(ctx.author.id)}")
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"{success} Success!",
                    description=f"I will no longer DM you when there's a server available!",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(self.client.user.id).avatar_url)
            await ctx.reply(embed = embed, mention_author = False)
        
        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Notify(client))