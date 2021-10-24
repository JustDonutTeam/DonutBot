import asyncio
import discord
import random
import datetime
import json
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

class Giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["giveaway"]["aliases"])
    @commands.has_permissions(manage_roles = True)
    async def giveaway(self, ctx, date, winners, *, prize):
        time = convert(date)
        if time <= 1209600:
            end_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
            emoji = self.client.get_emoji(888793481806512210)

            embed = discord.Embed(
                color = discord.Color.from_rgb(255, 158, 253),
                title = str(emoji) + " " + prize,
                description = f"**Hosted by:** {ctx.author.mention}\n**Ends at:** {str(end_date)[:-7]} UTC",
                timestamp = ctx.message.created_at
            )
            embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).avatar_url)
            message = await ctx.reply(embed=embed, mention_author=False)

            await message.add_reaction(emoji)
            await asyncio.sleep(time)

            fetched_message = await ctx.channel.fetch_message(message.id)

            users = await fetched_message.reactions[0].users().flatten()
            users.pop(users.index(self.client.user))
            winner_list = []

            for i in range(int(winners)):
                user = random.choice(users)

                if user in winner_list and len(users) >= int(winners):
                    while(user in winner_list):
                        user = random.choice(users)
                
                if not user in winner_list:
                    winner_list.append(user)
                    

            winner_string = ""

            for winner_object in winner_list:
                winner_string += (str(winner_object.mention) + " ")

            second_embed = discord.Embed(
                color = discord.Color.from_rgb(255, 158, 253),
                title = str(emoji) + " " + prize,
                description = f"**Hosted by:** {ctx.author.mention}\n**Ended at:** {str(end_date)[:-7]} UTC\n\n**Won by:** {winner_string}",
                timestamp = ctx.message.created_at
            )
            second_embed.set_footer(text=f"Donut", icon_url=self.client.get_user(self.client.user.id).avatar_url)

            await fetched_message.reply(f"{emoji} Congratulations {winner_string[:-1]}, you won **{prize}**!")
            await message.edit(embed=second_embed)

        else:
            await ctx.reply("Giveaways cannot be longer than 2 weeks (1,209,600 seconds)!", mention_author=False)


def setup(client):
    client.add_cog(Giveaway(client))