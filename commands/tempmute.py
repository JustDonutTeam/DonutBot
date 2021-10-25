import asyncio
import discord
import json
import datetime
from discord.ext import commands

def convert(time_string):
    smhd = ["s", "m", "h", "d", "w"]
    convert_ratios = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
    time_unit = []
    time_string = time_string.split("/")
    value = 0

    for unit in time_string:
        time_unit.append(unit[-1])

    for unit in time_unit:
        if not unit in smhd:
            unit = "s"

    for i in range(len(time_unit)):
        value += int(time_string[i][:-1]) * convert_ratios[time_unit[i]]

    return value

class Tempute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["tempmute"]["aliases"])
    @commands.has_permissions(kick_members=True)
    async def tempmute(self, ctx, member : discord.Member, duration):
        emoji = self.client.get_emoji(881874686173126666)
        time = convert(duration)

        end_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)

        if time <= 1209600:
            for role in ctx.guild.roles:
                if role.name == 'Muted':
                    await member.add_roles(role)
                    embed = discord.Embed(
                        colour=discord.Colour.from_rgb(255, 158, 253),
                        description=f'{emoji} **{member}** has been muted! (muted until {str(end_date)[:-7]} UTC)',
                        timestamp=ctx.message.created_at
                    )
                    embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
                    await ctx.reply(embed=embed, mention_author=False)

                    await asyncio.sleep(time)
                    await member.remove_roles(role)

                    return
                    
            overwrite = discord.PermissionOverwrite(send_messages=False)
            newRole = await ctx.guild.create_role(name='Muted')

            for channel in ctx.guild.channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                description=f'{emoji} **{member}** has been muted! (muted until {str(end_date)[:-7]} UTC)',
                timestamp=ctx.message.created_at
                )
            embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).display_avatar.url)
            await ctx.reply(embed=embed, mention_author=False)

            await asyncio.sleep(time)
            await member.remove_roles(newRole)

        else:
            await ctx.reply("Tempmutes cannot be longer than 2 weeks (1,209,600 seconds)!", mention_author=False)

def setup(client):
    client.add_cog(Tempute(client))