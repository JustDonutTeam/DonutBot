import discord
import json
import io
import aiohttp
from discord.ext import commands

class Tweet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["tweet"]["aliases"])
    async def tweet(self, ctx, comment, member : discord.Member = None,  displayname = None,):
        
        await ctx.trigger_typing()
        if not member: member = ctx.author
        if not displayname: displayname = member.display_name

        async with aiohttp.ClientSession() as session:

            async with session.get(
                f"https://some-random-api.ml/canvas/tweet?comment={comment}&displayname={displayname}&username={member.display_name}&avatar={member.avatar_url_as(format='png')}"
                #{member.avatar_url_as(format='png')}
            ) as af:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "tweet.png")
                embed = discord.Embed(
                    colour = discord.Colour.from_rgb(255, 158, 253),
                    timestamp = ctx.message.created_at
                )
                embed.set_image(url="attachment://tweet.png")
                embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(738788356506386462).avatar_url)
                await ctx.reply(embed=embed, file=file, mention_author=False)

        await session.close() 

def setup(client):
    client.add_cog(Tweet(client))