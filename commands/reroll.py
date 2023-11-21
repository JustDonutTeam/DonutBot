import random
import json
from discord.ext import commands

class Reroll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["reroll"]["aliases"])
    @commands.has_permissions(manage_roles = True)
    async def reroll(self, ctx, message_id, winners = 1):
        emoji = self.client.get_emoji(888793481806512210)
        fetched_message = await ctx.channel.fetch_message(message_id)

        message_embed = fetched_message.embeds
        prize = message_embed[0].to_dict()["title"][30:]

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

        await fetched_message.reply(f"{emoji} Congratulations {winner_string}, you won **{prize}**!")


async def setup(client):
    await client.add_cog(Reroll(client))