import discord
import json
import random
import requests
from discord.ext import commands

class Meme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["meme"]["aliases"])
    async def meme(self, ctx):
        api = requests.get("https://www.reddit.com/r/memes/hot.json").json()
        if not api["message"]:
            meme = api["data"]["children"][random.randint(0, len(api["data"]["children"]) - 1)]

            embed = discord.Embed(
                title = meme["data"]["title"],
                description = f"Posted by **u/{meme['data']['name']}**",
                colour = discord.Colour.from_rgb(255, 158, 253),
                url = "https://reddit.com" + meme["data"]["permalink"]
            )
            embed.set_image(url=meme['data']['url'])
            embed.set_footer(text=f"Upvotes: {meme['data']['score']} • {meme['data']['upvote_ratio']}% Downvoted\nDonut x Reddit • Posted on {meme['data']['subreddit_name_prefixed']}", icon_url=self.client.get_user(738788356506386462).avatar_url)

            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed = discord.Embed(
                color = discord.Color.from_rgb(255, 13, 0),
                title = ":x: Slow down! You're making too many requests!",
                timestamp = ctx.message.created_at,
                description = f"```{api}```"
            )
            embed.add_field(name="If you keep seeing this contact the developer!", value="DM Feeeeddmmmeee#7784 or join the [support server](https://discord.gg/GAPYQa9).")
            embed.set_footer(text="Donut encountered an error!", icon_url=self.client.get_user(738788356506386462).avatar_url)
            await ctx.reply(embed=embed, mention_author = False)

def setup(client):
    client.add_cog(Meme(client))