import discord
import json
import os
import requests
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = open("prefix.txt", "r").readline())
client.owner_ids = {585115156757872653,476335730470289429}
token = open("token.txt", "r")
status = open("status.txt","r").read()
client.remove_command('help')

#status = cycle(['status1, status2']) 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(':warning: Please pass in all required arguments.')
    #if isinstance(error, commands.errors.CommandNotFound):
        #await ctx.send(':warning: Please use a valid command.')
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(":warning: You don't have enough permissions to run this command.")
    if isinstance(error, commands.errors.BotMissingPermissions):
        await ctx.send(":warning: I don't have enough permissions to execute this command.")

@client.event
async def on_guild_join(guild):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(status.replace("gnum",str(len(client.guilds)))))

@client.event
async def on_guild_remove(guild):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(status.replace("gnum",str(len(client.guilds)))))

@client.event
async def on_ready():
    #change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(status.replace("gnum",str(len(client.guilds)))))
    print('Bot is ready')


'''
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
'''

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@commands.is_owner()
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Successfully loaded an extension.')

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Successfully unloaded an extension.')

@commands.is_owner()
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Successfully reloaded an extension.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@commands.is_owner()
@client.command(aliases=['echo', 'repeat'])
async def talk(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(message)

@client.command()
async def icon(ctx):
    icon_url = ctx.guild.icon_url
    await ctx.send(f"The icon url is: {icon_url}")

@commands.is_owner()
@client.command()
async def rules(ctx):
    await ctx.send(":wave: Welcome to the support server of Donut. Before taking any action please read the rules\n\n> - **The Rules**\n> These are the guidelines you have to follow in this server.\n> - **No Spam**\n> Any kind of spam will be punished\n> - **Absolutely no NSFW**\n> Every attempt at sending NSFW content will be punished with a kick or worse.\n> - **No Harrassement**\n> Everyone is equally good and you musn't harrass anyone.\n> - **Personal Information**\n> Without permission of the person, you are not allowed to reveal and share their personal information, such as name, adress, age, etc.\n> - **Argumentative Situations**\n> Anybody causing argumentative situations or drama can result in Administrative Action being taken against themselves.\n\n:link: **Links:**\n\nTop.gg: https://top.gg/bot/738788356506386462\nDiscord Bots: https://discord.bots.gg/bots/738788356506386462")

@client.command(aliases=['bs'])
async def botstats(ctx):

    embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), timestamp=ctx.message.created_at)

    embed.set_author(name=f'Bot Stats')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        
    embed.add_field(name='Servers:', value=len(client.guilds))
    embed.add_field(name='Library:', value='discord.py 1.5.0')
    embed.add_field(name='Ping:', value=f'{round(client.latency * 1000)}ms')
    embed.set_image(url='https://top.gg/api/widget/738788356506386462.svg')
    await ctx.send(embed=embed)
client.run(token.read())
