import discord
import json
import os
import asyncio
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix) 

client.remove_command('help')

#status = cycle(['status1, status2'])

@client.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(':warning: Please pass in all required arguments.')
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(':warning: Please use a valid command.')
    

@client.event
async def on_guild_join(guild):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'.help | Being a bot in {len(client.guilds)} guilds.'))

@client.event
async def on_guild_remove(guild):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'.help | Being a bot in {len(client.guilds)} guilds.'))

@client.event
async def on_ready():
    #change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'.help | Being a bot in {len(client.guilds)} guilds.'))
    print('Bot is ready')


'''
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
'''

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

def is_it_me(ctx):
    return ctx.author.id == 585115156757872653

@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Successfully loaded an extension.')

@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Successfully unloaded an extension.')

@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Successfully reloaded an extension.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzM4Nzg4MzU2NTA2Mzg2NDYy.XyRARg.GaBbvmB3XhvzEDDhG8tWgfpJHFg')
