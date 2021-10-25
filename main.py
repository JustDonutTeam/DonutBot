import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__.replace("main.py", "token.env"))

load_dotenv(dotenv_path = dotenv_path)
TOKEN = os.getenv('TOKEN')

with open("config.json", "r") as config:
    config = json.load(config)
    prefix = config["prefix"]
    status = prefix + "help | Donut " + config["version"] + " (Pycord Rewrite)"

intents = discord.Intents.all()
discord.member = True
discord.guild = True
discord.reaction = True

client = commands.Bot(command_prefix = prefix, intents = intents, allowed_mentions=discord.AllowedMentions(everyone=False))

client.remove_command("help")
client.owner_ids = {585115156757872653, 476335730470289429}

@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.idle, activity=discord.Game(status))
    print(f'Bot is ready. Logged in as {client.user}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')

for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')

@commands.is_owner()
@client.command()
async def load(ctx, command):
    client.load_extension(f'commands.{command}')
    await ctx.reply('Successfully loaded a command.', mention_author = False)

@commands.is_owner()
@client.command()
async def unload(ctx, command):
    client.unload_extension(f'commands.{command}')
    await ctx.reply('Successfully unloaded a command.', mention_author = False)

@commands.is_owner()
@client.command()
async def reload(ctx, command):
    client.unload_extension(f'commands.{command}')
    client.load_extension(f'commands.{command}')
    await ctx.reply('Successfully reloaded a command.', mention_author = False)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('❓')
    else:
        embed = discord.Embed(
            color = discord.Color.from_rgb(255, 13, 0),
            title = ":x: Command raised an exception!",
            timestamp = ctx.message.created_at,
            description = f"```{error}```"
        )
        embed.add_field(name="Please contact the developer!", value="DM Feeeeddmmmeee#7784 or join the [support server](https://discord.gg/GAPYQa9).")
        embed.set_footer(text="Donut encountered an error!", icon_url=client.get_user(client.user.id).display_avatar.url)

        await ctx.reply(embed=embed, mention_author=False)

client.run(TOKEN)