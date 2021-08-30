import discord
import json
from discord.ext import commands

class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["unban"]["aliases"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        emoji = self.client.get_emoji(881878530969976874)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    description=f'{emoji} **{member}** has been unbanned!',
                    timestamp=ctx.message.created_at
                )
                embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)
        
                await ctx.reply(embed=embed, mention_author=False)
                return

def setup(client):
    client.add_cog(Unban(client))