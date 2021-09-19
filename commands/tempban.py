import discord
import json
import asyncio
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

class Tempban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["tempban"]["aliases"])
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member : discord.Member, duration, *, reason=None):
        time = convert(duration)

        end_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)

        if time <= 1209600:
            await member.ban(reason=reason)
            leave = self.client.get_emoji(881870169918562345)
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                description=f'{leave} **{member}** has been banned! (banned until {str(end_date)[:-7]} UTC)',
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=f"Donut", icon_url=self.client.get_user(738788356506386462).avatar_url)

            await ctx.reply(embed=embed, mention_author=False)
            await asyncio.sleep(time)
            await ctx.guild.unban(member)

        else:
            await ctx.reply("Tempbans cannot be longer than 2 weeks (1,209,600 seconds)!", mention_author=False)

def setup(client):
    client.add_cog(Tempban(client))