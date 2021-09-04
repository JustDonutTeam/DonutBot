import discord
import json
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["help"]["aliases"])
    async def help(self, ctx, name = None):
        if name:
            with open("help.json", "r") as file:
                file = json.load(file)
            
            embed = discord.Embed(
                color = discord.Color.from_rgb(255, 158, 253),
                title = file[name]["name"],
                description = file[name]["desc"],
                timestamp = ctx.message.created_at
            )
            if file[name]["command"]: 
                embed.add_field(name=":mouse_three_button: Usage:", value=file[name]["usage"])
                embed.add_field(name=":clipboard: Aliases:", value=str(file[name]["aliases"]).replace("'", "`").replace("[", "").replace("]", ""))
            else: embed.add_field(name=":clipboard: Commands:", value=str(file[name]["commands"]).replace("'", "`").replace("[", "").replace("]", ""))
            embed.set_footer(text="Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)

            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed = discord.Embed(
                color = discord.Color.from_rgb(255, 158, 253),
                title = "Need some help?",
                description = "This is the list of all the command categories this bot has. You can use `.help <category>` to see all the commands.",
                timestamp = ctx.message.created_at
            )
            embed.add_field(name=":question: Other", value="A category with commands that don't belong in other categories.")
            embed.add_field(name=":camera: Image", value="Category with image related commands.")
            embed.add_field(name=":hammer: Moderation", value="A command category with commands for admins.")
            embed.set_footer(text="Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)

            await ctx.reply(embed=embed, mention_author=False)


        

def setup(client):
    client.add_cog(Help(client))