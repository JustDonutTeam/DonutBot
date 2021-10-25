import discord
import json
import random
from discord.ext import commands

class _8ball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["8ball"]["aliases"])
    async def _8ball(self, ctx, *, question):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again',
            "Don't count on it.",
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.',
            'No.' ]

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=':8ball: And the answer is...',
            description=f'{random.choice(responses)}',
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(_8ball(client))