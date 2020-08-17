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
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``changeprefix``, ``support``, ``credits``, ``avatar``, ``userinfo``, ``poll``, ``keyboard``, ``announcement``",
                timestamp=ctx.message.created_at
                )
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        
        elif category == 'fun':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title=":video_game: fun",
                description="This is the list of all commands from this category, use ``.help <command>`` to get some more detailed help on a command!\n\n``8ball``, ``vbucks``, ``tf``",
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

        elif category == 'vbucks':
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(255, 158, 253),
                title="vbucks command",
                description="Command used to get some free vbucks, required arguments: ``.vbucks``.",
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


        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))