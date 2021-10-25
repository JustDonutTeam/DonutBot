import discord
import json
from discord.ext import commands

class Serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["serverinfo"]["aliases"])
    async def serverinfo(self, ctx):
        owner = self.client.get_emoji(881889987539386378)
        channels = self.client.get_emoji(881890493095632936)
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            timestamp=ctx.message.created_at
        )
        embed.set_author(name="Info about " + str(ctx.guild.name), icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
        embed.add_field(name=":date: Created At:", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=":id: ID:", value=ctx.guild.id)
        embed.add_field(name=":busts_in_silhouette: Members", value=len(ctx.guild.members))
        embed.add_field(name=f"{owner} Server Owner:", value=ctx.guild.owner)
        embed.add_field(name=f"{channels} Text Channels:", value=len(ctx.guild.text_channels))
        embed.add_field(name=":earth_africa: Region:", value=ctx.guild.region)

        if ctx.guild.premium_subscription_count > 0:
            boostrole = self.client.get_emoji(881901503097499659)
            boostbadge = self.client.get_emoji(881901464610570332)

            t0 = self.client.get_emoji(881906890253172808)
            t1 = self.client.get_emoji(881901549339680819)
            t2 = self.client.get_emoji(881901599075758102)
            t3 = self.client.get_emoji(881901629081796658)

            if ctx.guild.premium_tier == 0: tier = t0
            elif ctx.guild.premium_tier == 1: tier = t1
            elif ctx.guild.premium_tier == 2: tier = t2
            elif ctx.guild.premium_tier == 3: tier = t3
            
            embed.add_field(name=f"{boostrole} Booster Role:", value=ctx.guild.premium_subscriber_role)
            embed.add_field(name=f"{boostbadge} Boosters:", value=ctx.guild.premium_subscription_count)
            embed.add_field(name=f"{tier} Boosting Tier", value=ctx.guild.premium_tier)

        if ctx.guild.banner_url:
            embed.set_image(url=str(ctx.guild.banner_url))
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Serverinfo(client))