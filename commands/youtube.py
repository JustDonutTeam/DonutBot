import discord
import json
import io
import aiohttp
from discord.ext import commands

class Youtube(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["youtube"]["aliases"])
    async def youtube(self, ctx, member : discord.Member = None, *, comment):
        
        await ctx.trigger_typing()
        if not member: member = ctx.author

        async with aiohttp.ClientSession() as session:

            async with session.get(
                f"https://some-random-api.ml/canvas/youtube-comment?comment={comment}&username={member.display_name}&avatar={member.avatar_url_as(format='png')}"
                #{member.avatar_url_as(format='png')}
            ) as af:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "youtube.png")
                embed = discord.Embed(
                    colour = discord.Colour.from_rgb(255, 158, 253),
                    timestamp = ctx.message.created_at
                )
                embed.set_image(url="attachment://youtube.png")
                embed.set_footer(text="Donut x Some Random API", icon_url=self.client.get_user(self.client.user.id).avatar_url)
                await ctx.reply(embed=embed, file=file, mention_author=False)

        await session.close() 

def setup(client):
    client.add_cog(Youtube(client))