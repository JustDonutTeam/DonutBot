import discord
import json
from discord.ext import commands

class Unmute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["unmute"]["aliases"])
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member : discord.Member):
        emoji = self.client.get_emoji(881873652977639444)
        for role in ctx.guild.roles:
            if role.name == 'Muted':
                if role in member.roles:
                    await member.remove_roles(role)
                    embed = discord.Embed(
                        colour=discord.Colour.from_rgb(255, 158, 253),
                        description=f'{emoji} **{member}** has been unmuted!',
                        timestamp=ctx.message.created_at
                    )
                    embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                else:
                    raise TypeError("This user is not muted.")
        
async def setup(client):
    await client.add_cog(Unmute(client))