from logging import disable
import discord
import json
import sqlite3
from discord.ext import commands

class Disable(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases = json.load(open("help.json", "r"))["disable"]["aliases"], invoke_without_command = True)
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx):
        await ctx.reply("This is a command group which requires additional arguments! Type `.help disable` for more info.", mention_author=False)
        

    @disable.command()
    @commands.has_permissions(manage_roles=True)
    async def reactionroles(self, ctx, message_id = None):
        success = self.client.get_emoji(883738376866516992)
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        message = ""
        desc = "your guild"

        if message_id:
            message = f" AND message_id = {message_id}"
            desc = f"the message with an ID of `{message_id}`"

        cursor.execute(f"DELETE from reactionroles WHERE guild_id = {ctx.guild.id}" + message)
        embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"{success} Success!",
                    description=f"Successfully cleared all reaction roles from {desc}!\n\nRun `.enable reactionroles` to add new ones!",
                    timestamp = ctx.message.created_at
                )
        embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
        await ctx.reply(embed = embed, mention_author = False)

        database.commit()
        cursor.close()
        database.close()

    @disable.command()
    @commands.has_permissions(administrator=True)
    async def welcomebye(self, ctx):
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
                    description=f"Successfully disabled welcome-bye messages!\n\nRemember that using `.enable welcomebye` will overwrite your previous settings!",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
            await ctx.reply(embed = embed, mention_author = False)
        else:
            raise TypeError("welcome-bye messages are already disabled.")

        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Disable(client))