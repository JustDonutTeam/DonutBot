from datetime import datetime
import discord
import json
from discord.commands.commands import OptionChoice
from discord.commands.context import ApplicationContext
from discord.ext import commands
from discord.commands import slash_command, Option

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command()
    async def help(self, ctx: ApplicationContext, category = Option(str, "category", required=False)):
        # Category is a string object if argument was provided and an Option object if not.
        if type(category) is str:
            with open("help.json", "r") as file:
                file = json.load(file)
            
            embed = discord.Embed(
                color = discord.Color.from_rgb(255, 158, 253),
                title = file[category]["name"],
                description = file[category]["desc"],
                timestamp = datetime.now(),
            )
            if file[category]["command"]: 
                embed.add_field(name=":mouse_three_button: Usage:", value=file[category]["usage"])
                embed.add_field(name=":clipboard: Aliases:", value=str(file[category]["aliases"]).replace("'", "`").replace("[", "").replace("]", ""))
            else: embed.add_field(name=":clipboard: Commands:", value=str(file[category]["commands"]).replace("'", "`").replace("[", "").replace("]", ""))
            embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                color = discord.Color.from_rgb(255, 158, 253),
                title = "Need some help?",
                description = "This is the list of all the command categories this bot has. You can use `.help <category>` to see all the commands.",
                timestamp = datetime.now(),
            )
            embed.add_field(name=":question: Other", value="A category with commands that don't belong in other categories.")
            embed.add_field(name=":camera: Image", value="Category with image related commands.")
            embed.add_field(name=":hammer: Moderation", value="A command category with commands for admins.")
            embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)

            await ctx.respond(embed=embed)


        

def setup(client):
    client.add_cog(Help(client))