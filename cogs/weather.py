import discord
import json
import os
import requests
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from turtle import *
import turtle
import svgwrite
import os
from svg_turtle import SvgTurtle
import json
from PIL import Image, ImageDraw, ImageFont

#weather.py cog by https://github.com/przebor

def picture(inpu):
    responss = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+inpu+"&units=metric&APPID=7c9712e6006142a7ba6a1e5578d8debe")
    responee = responss.content.decode("utf-8")
    response = json.loads(responee)
    if "message" not in response:
        tempe=str(round(response["main"]["temp"]))
        if int(tempe) > 15:
            if int(tempe)>30:
                color('#fa7f4b')
            else:
                color('#f7d263')
        else:
            color('#b0fbff')
        pu();goto(40,-55);pd()
        write(tempe + "\u00B0C", move=False, align="center", font=("Arial", 30, "bold"))
        pu(); goto(0,15); pd();
        write(inpu, move=False, align="center", font=("Arial", 34, "normal"))
def write_file(draw_func, filename, size, inpuu):
    global response
    drawing = svgwrite.Drawing(filename, size=size)
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func(inpuu)
    drawing.save()
    responss = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+inpuu+"&units=metric&APPID=7c9712e6006142a7ba6a1e5578d8debe")
    responee = responss.content.decode("utf-8")
    response = json.loads(responee)
    if "message" not in response:
        print(response["weather"][0]["icon"])
        url = 'http://openweathermap.org/img/wn/'+response["weather"][0]["icon"]+'@2x.png'
        myfile = requests.get(url)
        open('weather.png', 'wb').write(myfile.content)
def mainpog(inpuuu):
    write_file(picture, 'example.svg', size=("300px", "150px"), inpuu=inpuuu)
    if "message" not in response:
        os.system("inkscape -z -e pogoda.png example.svg")
        background = Image.open("pogoda.png")
        foreground = Image.open("weather.png")
        background.paste(foreground, (20, 50))
        background.save("weether.png")

class Weather(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def weather(self,ctx,arg):
        async with ctx.typing():
            print(arg)
            mainpog(arg.lower().title())
            print(response["cod"])
        if "message" in response:
            await ctx.channel.send("Cannot send weather! Error: "+response["message"])
        else:
            await ctx.channel.send(file=discord.File('weether.png'))
def setup(client):
    client.add_cog(Weather(client))