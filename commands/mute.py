import discord
import json
from discord.ext import commands

class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["mute"]["aliases"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member : discord.Member):
        emoji = self.client.get_emoji(881874686173126666)
        for role in ctx.guild.roles:
            if role.name == 'Muted':
                await member.add_roles(role)
                embed = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 158, 253),
                    description=f'{emoji} **{member}** has been muted!',
                    timestamp=ctx.message.created_at
                )
                embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
                await ctx.reply(embed=embed, mention_author=False)
                return
        overwrite = discord.PermissionOverwrite(send_messages=False)
        newRole = await ctx.guild.create_role(name='Muted')

        for channel in ctx.guild.channels:
            await channel.set_permissions(newRole,overwrite=overwrite)

        await member.add_roles(newRole)
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            description=f'{emoji} **{member}** has been muted!',
            timestamp=ctx.message.created_at
            )
        embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Mute(client))