import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, category=''):
        if category == '':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="Need some help?",
                description="This is the list of all categories, use ``.help <category>`` to get some more detailed help on a category!",
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
            embed.add_field(name=':speech_balloon: text', value='A category consisting of some text related commands.')
            embed.add_field(name=':hammer: moderation', value='Moderation related commands (ban, kick etc.)')
            embed.add_field(name=':tools: tools', value='some epic tools')
            embed.add_field(name=':video_game: fun', value='some *funny* commands')
            embed.add_field(name=':camera: image', value='wanna see some cat pics? of course we have even more cool stuff!')

        elif category == 'moderation':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title=":hammer: moderation",
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``kick``, ``ban``, ``unban``, ``clear``, ``mute``, ``unmute``, ``lockdown``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'text':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title=":speech_balloon: text",
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``uwufy``, ``reverse``, ``raged``, ``uppercase``, ``lowercase``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'tools':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title=":tools: tools",
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``changeprefix``, ``icon``, ``support``, ``credits``, ``avatar``, ``userinfo``, ``poll``, ``keyboard``, ``announcement``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'image':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title=":camera: image",
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``hug``, ``cat``, ``panda``, ``wasted``, ``gay``, ``invert``, ``threshold``, ``triggered``, ``yt``,``gif``,``dog``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        
        elif category == 'fun':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title=":video_game: fun",
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``8ball``, ``robux``, ``tf``, ``nuke``, ``fact``, ``chat``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'kick':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="kick command",
                description="Command used to kick a user, required arguments: ``.kick <user>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'ban':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="ban command",
                description="Command used to ban a user, required arguments: ``.ban <user>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'clear':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="clear command",
                description="Command used to delete some messages, required arguments: ``.clear <amount>``, by default the command deletes 5 messages.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'unban':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="unban command",
                description="Command used to unban a user, required arguments: ``.unban <user>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'uwufy':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="uwufy command",
                description="Command used to uwufy some text, required arguments: ``.uwufy <text>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'reverse':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="reverse command",
                description="Command used to reverse some text, required arguments: ``.reverse <text>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'raged':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="raged command",
                description="Command used to modify some text os its written with randomly placed uppercase and lowercase letters, required arguments: ``.raged <text>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'uppercase':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="uppercase command",
                description="Command used to make some text only uppercase, required arguments: ``.uppercase <text>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'lowercase':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="lowercase command",
                description="Command used to make some text only lowercase, required arguments: ``.lowercase <text>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'changeprefix':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="changeprefix command ``(CURRENTLY UNAVAILABLE)``",
                description="Command used to change the server prefix, required arguments: ``.changeprefix <prefix>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'invite':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="invite command",
                description="Sends the link to invite the bot, required arguments: ``.invite``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')


        elif category == 'support':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="support command",
                description="Sends the invite to our support server, required arguments: ``.support``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == '8ball':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="8ball command",
                description="Command used to predict the future, required arguments: ``.8ball <question>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'robux':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="robux command",
                description="Command used to get some free robux, required arguments: ``.robux``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'credits':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="credits command",
                description="Command used to see the credits, required arguments: ``.credits``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'mute':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="mute command",
                description="Mutes the user so that he cannot send messages, required arguments: ``.mute <user>``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'unmute':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="unmute command",
                description="Unmutes the user so he can talk again! required arguments: ``.unmute <user>``, user has to be muted first.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'userinfo':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="info command",
                description="Command used to get some info on a user, required arguments: ``.userinfo <user>``.",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'avatar':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="kick command",
                description="Command used to get a user's avatar, required arguments: ``.avatar <user>``.",
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'lockdown':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="lockdown command",
                description="Command used to put the channel or remove it from lockdown, required arguments: ``.lockdown``.",
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'poll':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="poll command",
                description='Makes a poll, yay!, required arguments: ``.poll "<question>" "<option1>" "<option2>"`` etc.',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'keyboard':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="keyboard command",
                description='Shows all the discord keyboard shortcuts, required arguments: ``.keyboard``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'tf':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="team fortress 2 command",
                description='Shows some info on each of the classes, required arguments: ``.tf <class>`` (class is optional)\n\nPossible classes: ``demoman``, ``engineer``, ``heavy``, ``medic``, ``pyro``, ``spy``, ``sniper``, ``soldier``, ``scout``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'announcement':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="announcement command",
                description='announces some stuff, required arguments: ``.announcement <announcement>``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'nuke':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="nuke command",
                description='nukes a chosen place. Be careful with this command! Required arguments: ``.nuke <destination>``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'icon':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="server icon command",
                description='sends the server icon url. Required arguments: ``.icon``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'fact':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="random facts",
                description='sends a random fact using an API Required arguments: ``.fact``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'hug':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="random anime hugging gif",
                description='sends a random anime hugging gif. Required arguments: ``.hug``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'cat':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="random cat pic",
                description='sends a random cat pic. Required arguments: ``.cat``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'panda':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="random panda pic",
                description='sends a random panda pic. Required arguments: ``.panda``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'wasted':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="edits your pfp",
                description='sends an edited version of your pfp! Required arguments: ``.wasted``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'gay':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="edits your pfp",
                description='sends an edited version of your pfp! Required arguments: ``.gay``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'triggered':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="edits your pfp",
                description='sends an edited version of your pfp! Required arguments: ``.triggered``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'invert':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="edits your pfp",
                description='sends an edited version of your pfp! Required arguments: ``.invert``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        elif category == 'threshold':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="edits your pfp",
                description='sends an edited version of your pfp! Required arguments: ``.threshold``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'gif':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="sends random gif",
                description='sends a random gif with specified tag! Required arguments: ``.gif <tag>``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'chat':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="answers you",
                description='answers your sentence/question! ``.chat <sentence>``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        elif category == 'yt':  
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="sends a youtube comment",
                description='sends a fake youtube comment! Required arguments: ``.yt <member>``',
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))