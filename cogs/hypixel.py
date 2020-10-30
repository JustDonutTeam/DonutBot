import discord
from discord.ext import commands
import requests
from PIL import Image

def get_rank(id):
    resp=requests.get("https://api.hypixel.net/player?key=06201516-7a36-4c71-af15-3044a421b4ae&uuid="+id).json()
    if "rank" in resp["player"]:
        return resp["player"]["rank"]
    elif "monthlyPackageRank" in resp["player"]:
        return "MVP++"
    elif "newPackageRank" in resp["player"]:
        return resp["player"]["newPackageRank"].replace("_PLUS", "+")
    else:
        return "NONE"

class Hypixel(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def hypixel(self, ctx, username):
        async with ctx.typing():
            embed = discord.Embed(colour=discord.Colour.from_rgb(255, 158, 253), timestamp=ctx.message.created_at,title=username)
            url = "https://gen.plancke.io/exp/"+username+".png"
            myfile = requests.get(url)
            open('lvl.png', 'wb').write(myfile.content)
            url = "https://gen.plancke.io/achievementPoints/"+username+".png"
            myfile = requests.get(url)
            open('ach.png', 'wb').write(myfile.content)
            img = Image.new('RGBA', (910, 80))
            lvl = Image.open('lvl.png')
            ach = Image.open('ach.png')
            comb = img.copy()
            comb.paste(lvl)
            comb.paste(ach,(0,40))
            comb.save("combined.png",quality=95)
            file = discord.File("combined.png")
            embed.set_image(url="attachment://combined.png")
            uuid=requests.get("https://api.mojang.com/users/profiles/minecraft/"+username).json()["id"]
            embed.set_thumbnail(url="https://crafatar.com/avatars/"+uuid)
            embed.add_field(name="Rank",value=get_rank(uuid))
            guildg=requests.get("https://api.hypixel.net/guild?key=06201516-7a36-4c71-af15-3044a421b4ae&player="+uuid).json()
            if guildg["guild"] != None:
                guild=guildg["guild"]["name"]
            else:
                guild="NONE"
            embed.add_field(name="Guild",value=guild)
            fr=requests.get("https://api.hypixel.net/friends?key=06201516-7a36-4c71-af15-3044a421b4ae&uuid="+uuid).json()
            embed.add_field(name="Friends",value=str(len(fr["records"])))
        await ctx.send(embed=embed, file=file)
def setup(client):
    client.add_cog(Hypixel(client))