import discord
import json
import sqlite3
from discord.ext import commands

class Enable(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["enable"]["aliases"])
    @commands.has_permissions(administrator=True)
    async def enable(self, ctx, channel : discord.TextChannel = None, custom_welcome = "0", custom_bye = "0"):
        if not channel: channel = ctx.channel
        success = self.client.get_emoji(883738376866516992)
        
        database = sqlite3.connect("database.sqlite")
        cursor = database.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS welcome (enabled	TEXT, guild_id TEXT, channel_id TEXT, custom_welcome TEXT, custom_bye TEXT)")
        cursor.execute(f"SELECT channel_id FROM welcome WHERE guild_id = {ctx.guild.id}")
        data = cursor.fetchone()

        if not data:
            cursor.execute("INSERT INTO welcome(enabled, guild_id, channel_id, custom_welcome, custom_bye) VALUES(?, ?, ?, ?, ?)", (1, ctx.guild.id, channel.id, custom_welcome, custom_bye))
            if custom_welcome == "0": custom_welcome = "No custom message"
            if custom_bye == "0": custom_bye = "No custom message"
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"{success} Success!",
                    description=f"Successfully enabled welcome-bye messages!\nChannel: {channel.mention}\nWelcome message: `{custom_welcome}`\nBye message: `{custom_bye}`",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(738788356506386462).avatar_url)
            await ctx.reply(embed = embed, mention_author = False)

        else:
            cursor.execute("UPDATE welcome SET enabled = ? WHERE guild_id = ?", (1, ctx.guild.id))
            cursor.execute("UPDATE welcome SET channel_id = ? WHERE guild_id = ?", (channel.id, ctx.guild.id))
            cursor.execute("UPDATE welcome SET custom_welcome = ? WHERE guild_id = ?", (custom_welcome, ctx.guild.id))
            cursor.execute("UPDATE welcome SET custom_bye = ? WHERE guild_id = ?", (custom_bye, ctx.guild.id))
            if custom_welcome == "0": custom_welcome = "Default"
            if custom_bye == "0": custom_bye = "Default"
            embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    title=f"{success} Success!",
                    description=f"Successfully enabled welcome-bye messages!\n\n```Channel: #{channel}\nWelcome message: {custom_welcome}\nBye message: {custom_bye}```",
                    timestamp = ctx.message.created_at
                )
            embed.set_footer(text=f"Donut x SQLite3", icon_url=self.client.get_user(738788356506386462).avatar_url)
            await ctx.reply(embed = embed, mention_author = False)
        
        database.commit()
        cursor.close()
        database.close()

def setup(client):
    client.add_cog(Enable(client))