import discord
import requests
import json
from datetime import datetime
from discord.ext import commands

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = json.load(open("help.json", "r"))["weather"]["aliases"])
    async def weather(self, ctx, *, city):
        await ctx.trigger_typing()

        metric = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=bf993c387617d5492410715e9315f630")
        imperial = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=bf993c387617d5492410715e9315f630")
        metric = metric.json()
        imperial = imperial.json()

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=f":pushpin: {metric['name']}",
            url=f"https://openweathermap.org/city/{metric['id']}",
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text=f"Donut x OpenWeatherMap.org", icon_url=self.client.get_user(738788356506386462).avatar_url)
        embed.set_image(url=f"https://open.mapquestapi.com/staticmap/v4/getmap?key=FdslJ2xwoyLBqQreQk5OBLj5AV11wMnu&size=1024,512&zoom=8&center={metric['coord']['lat']},{metric['coord']['lon']}")
        embed.set_thumbnail(url=f"http://openweathermap.org/img/w/{metric['weather'][0]['icon']}.png")

        embed.add_field(name=":thermometer: Temperature:", value=f"{metric['main']['temp']} °C /  {imperial['main']['temp']} °F")
        embed.add_field(name=":small_red_triangle_down: Min:", value=f"{metric['main']['temp_min']} °C /  {imperial['main']['temp_min']} °F")
        embed.add_field(name=":small_red_triangle: Max:", value=f"{metric['main']['temp_max']} °C /  {imperial['main']['temp_max']} °F")

        embed.add_field(name=":sunny: Sunrise:", value=datetime.utcfromtimestamp(metric['sys']['sunrise']).strftime("%I:%M %p UTC"))
        embed.add_field(name=":crescent_moon: Sunset:", value=datetime.utcfromtimestamp(metric['sys']['sunset']).strftime("%I:%M %p UTC"))
        embed.add_field(name=":clock1: Timezone:", value=f"{metric['timezone']/3600}h")

        embed.add_field(name=":droplet: Humidity:", value=f"{metric['main']['humidity']}%")
        embed.add_field(name=":cloud: Clouds:", value=f"{metric['clouds']['all']}%")
        embed.add_field(name=":leaves: Wind:", value=f"{metric['wind']['speed']} m/s")

        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Weather(client))