import discord
import random
import json
import random
import praw
from discord.ext import commands

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.reddit = None
        if '47_tBA3IUZ9EGw' and 'dOzrCyoH5HuFkbGHiIfD_lhpk8c':
            self.reddit = praw.Reddit(client_id='47_tBA3IUZ9EGw',
            client_secret='dOzrCyoH5HuFkbGHiIfD_lhpk8c', user_agent='DONUT_BOT:%s:1.0' %
            '47_tBA3IUZ9EGw')

    @commands.command(aliases=['shortcuts'])
    async def keyboard(self, ctx):
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Here are all the discord shortcuts!', timestamp=ctx.message.created_at)
        embed.set_image(url='https://cdn.discordapp.com/attachments/739939374581678103/741293165897711636/unknown.png')

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def poll(self, ctx, question, *options):
        if len(options) > 10:
            await ctx.send(':warning: You can only supply a maximum of 10 options')
        else:
            embed = discord.Embed(
                title='Poll',
                description=question,
                color=discord.Colour.from_rgb(255, 158, 253),
                timestamp=ctx.message.created_at)
            fields = [('Options', '\n'.join([f'{numbers[idx]} {option}' for idx, option in enumerate(options)]), False), ('Instructions', 'React to cast a vote', False)]
            
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            message = await ctx.send(embed=embed)

            for emoji in numbers[:len(options)]:
                await message.add_reaction(emoji)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member : discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title=f"{member}'s avatar", timestamp=ctx.message.created_at)
        embed.set_image(url=member.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['user', 'info'])
    async def userinfo(self, ctx, member : discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        
        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Guild name:', value=member.display_name)
        embed.add_field(name='Created at:', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))
        embed.add_field(name='Top role:', value=member.top_role.mention)
        embed.add_field(name='Bot?', value=member.bot)

        await ctx.send(embed=embed)

    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Donut Bot Credits",
            description="Thanks so much to all the people who helped me with developing this epic bot!",
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        embed.add_field(name='Developer:', value='Feeeeddmmmeee#7784')
        embed.add_field(name='Awesome helpers:', value='Luwuke#2795\nPrzebot#2448')
        await ctx.send(embed=embed)

    @commands.command(aliases=['uwu', 'owo', 'owofy', 'uwuify', 'owoify'])
    async def uwufy(self, ctx, *, phrase):
        uwufied = phrase.replace('rl', 'w').replace('RL', 'W').replace('ove', 'uv').replace('the', 'dee').replace('r', 'w')
        await ctx.send(uwufied)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Join our support server here!",
            description="Join the server [here](https://discord.gg/GAPYQa9).",
            timestamp=ctx.message.created_at
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def vbucks(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Get free vbucks!",
            description="Click [this](https://cutt.ly/free-v-bucks-legit) link to get free vbucks.",
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/739939374581678103/740272961516339200/unknown.png')

        await ctx.send(embed=embed)

    @commands.command(aliases=['upper'])
    async def uppercase(self, ctx, *, sentence):
        await ctx.send(sentence.upper())

    @commands.command(aliases=['lower'])
    async def lowercase(self, ctx, *, sentence): 
            await ctx.send(sentence.lower().replace('@everyone', 'everyone'))

    @commands.command()
    async def reverse(self, ctx, *, sentence):
        result = ''
        for letter in sentence:
            result = letter + result
        await ctx.send(result)

    @commands.command(aliases=['rage', 'scream', 'yell', 'shout'])
    async def raged(self, ctx, *, sentence):
        result = ''
        for letter in sentence:
            uporlow = random.randint(0, 1)
            if uporlow == 0:
                result = result + letter.upper()
            else:
                result = result + letter.lower()
        await ctx.send(result)

    @commands.command(aliases=['prefix'])
    async def changeprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[ctx.guild.id] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=f'Prefix has been changed to: "{prefix}"!',
            description='You can now use the new prefix.'
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')

        await ctx.send(embed=embed)

    @commands.command(aliases=['8ball', 'predict'])
    async def _8ball(self, ctx, *, question):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'No idea lmaooo',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again',
            "Don't count on it.",
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.',
            'No.' ]

        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title=':8ball: And the answer is...',
            description=f'{random.choice(responses)}',
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/646009680241623070/740564170964992130/donut-pfp.png')
        
        await ctx.send(embed=embed)

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title=f':boom: Kicked {member.name}',
            timestamp=ctx.message.created_at
        )
        
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title=f':boom: Banned {member.name}',
            timestamp=ctx.message.created_at
        )
        
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title=f'Unbanned {user}',
                    timestamp=ctx.message.created_at
                 )
        
                await ctx.send(embed=embed)
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member : discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == 'Muted':
                await member.add_roles(role)
                embed = discord.Embed(
                    colour=discord.Colour.orange(),
                    title='{} has muted {}'.format(ctx.author,member),
                    timestamp=ctx.message.created_at
                 )
        
                await ctx.send(embed=embed)
                return
        overwrite = discord.PermissionOverwrite(send_messages=False)
        newRole = await guild.create_role(name='Muted')

        for channel in guild.channels:
            await channel.set_permissions(newRole,overwrite=overwrite)

        await member.add_roles(newRole)
        embed = discord.Embed(
            colour=discord.Colour.orange(),
            title='{} has muted {}'.format(ctx.author,member),
            timestamp=ctx.message.created_at
        )
        
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member : discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == 'Muted':
                await member.remove_roles(role)
                embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title='{} has unmuted {}'.format(ctx.author,member),
                    timestamp=ctx.message.created_at
                 )
        
                await ctx.send(embed=embed)
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def lockdown(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(f'I have put `{channel.name}` on lockdown.')
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f'I have put `{channel.name}` on lockdown.')
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f'I have removed `{channel.name}` from lockdown.')

def setup(client):
    client.add_cog(Commands(client))