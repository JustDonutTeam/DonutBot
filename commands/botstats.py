import discord
import json
from discord.ext import commands

class Botstats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["botstats"]["aliases"])
    async def botstats(self, ctx):

        discordpy = self.client.get_emoji(868868411806056558)
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            description=f'**Type .help to see the commands!**\n\nBecause of Discords limitaions for unverified bots I am unable to join more than 100 servers (remaining places: **{100-len(self.client.guilds)}**).',
            timestamp=ctx.message.created_at
        )
        embed.set_author(name=self.client.get_user(585115156757872653), icon_url=self.client.get_user(585115156757872653).avatar_url)
        embed.set_image(url='https://top.gg/api/widget/self.client.user.id.png')
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).avatar_url)

        embed.add_field(name=":globe_with_meridians: Servers:", value=f"{len(self.client.guilds)} servers!")
        embed.add_field(name=":ping_pong: Ping:", value=f"{round(self.client.latency * 1000)} ms!")
        embed.add_field(name=":busts_in_silhouette: Users:", value=f"{len(self.client.users)} users!")
        embed.add_field(name=f"{discordpy} Library:", value="Discord.py v1.7.3!")
        embed.add_field(name=":desktop: Commands:", value=f"{len(json.load(open('help.json', 'r'))) - 3} commands!")

        with open("config.json", "r") as config:
            config = json.load(config)
            embed.add_field(name=":clock1: Version:", value= f"v{config['version']}!")
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Botstats(client))