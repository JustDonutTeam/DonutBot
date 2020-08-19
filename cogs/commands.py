import discord
import random
import json
import random
from discord.ext import commands

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Invite Donut to your server!",
            description="Invite the bot [here](https://discord.com/api/oauth2/authorize?client_id=738788356506386462&permissions=8&scope=bot).",
            timestamp=ctx.message.created_at
        )
        await ctx.send(embed=embed)

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

    @commands.command(aliases=['bucks', 'roblox'])
    async def robux(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(255, 158, 253),
            title="Get free robux!",
            description="Click [this](http://bit.do/free-robux-legit) link to get free robux.",
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(url='https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/roblox.png')

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

    @commands.command(aliases=['teamfortress', 'tf2', 'teamfortress2'])
    async def tf(self, ctx, classes=None):
        if classes == 'demoman':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Demoman', timestamp=ctx.message.created_at,
            description='The Demoman is a scrumpy-swilling demolitions expert from the Scottish town of Ullapool, and is one of the most versatile members of the team. A master of explosives, the Demoman strategically deals massive amounts of indirect and mid-range splash damage. Armed with his Grenade Launcher and Stickybomb Launcher, the Demoman uses his one good eye and the knowledge of his surrounding environment for well-timed sticky bomb detonations that send enemies skyward, often in many pieces. Should anyone get past his explosive ordinance, however, they will be shocked to learn the Demoman is extremely proficient at melee combat, being one of the deadliest melee users in the game, with a variety of powerful melee unlocks in his arsenal.\n\n``One crossed wire, one wayward pinch of potassium chlorate, one errant twitch...and kablooie!`` — The Demoman on occupational hazards')
            embed.set_thumbnail(url='https://prod.wiki.tf/w/images/thumb/0/06/DemomanVidSplash.png/300px-DemomanVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'engineer':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Engineer', timestamp=ctx.message.created_at,
            description="The Engineer is a soft-spoken, amiable Texan from Bee Cave, Texas, USA with an interest in all mechanical things. He specializes in constructing and maintaining Buildings that provide support to his team, rather than fighting at the front lines, making him the most suitable for defense. The Engineer's various gadgets include the Sentry Gun, an automated turret that fires at any enemy in range, the Dispenser, a device that restores the health and ammunition of nearby teammates, and Teleporters that quickly transport players from point A to point B.\n\n``Hey look, buddy. I'm an engineer — that means I solve problems. Not problems like 'What is beauty?' because that would fall within the purview of your conundrums of philosophy. I solve practical problems.`` — The Engineer on his profession")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/2/21/EngineerVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'heavy':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Heavy', timestamp=ctx.message.created_at,
            description="The Heavy Weapons Guy, more commonly known as the Heavy, is a towering hulk of a man hailing from the USSR. He is the largest and possibly most dangerous class in Team Fortress 2. Boasting the most default health and devastating firepower from his trusty Minigun, the Heavy is no pushover. The Heavy's Minigun can inflict heavy damage at a high rate of fire, allowing him to mow down opposing babies, cowards, and teeny-men in seconds. The Heavy's movement speed is his main weakness. Upon revving up or firing his Minigun, his already unimpressive speed drops down to an even lower amount, making him a very easy target for Snipers and Spies. His slow speed makes him more dependent on support from Medics and Engineers to keep him in the fight. Aside from decimating entire teams, the Heavy is able to provide further support for his comrades with an often required health boost via his Sandvich, which, when consumed, is capable of healing him to full health. It can also be dropped to provide an instant 50% health boost to his teammates, systematically equal to a Medium Health kit. However, if the Heavy isn't careful, an enemy may pick up the dropped Sandvich for a health boost of their own.\n\n``Some people think they can outsmart me. Maybe... maybe. I have yet to meet one that can outsmart bullet.`` — The Heavy on intelligence")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/6/6c/HeavyVidSplash.png/300px-HeavyVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'medic':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Medic', timestamp=ctx.message.created_at,
            description="The Medic is a Teutonic man of medicine from Stuttgart, Germany. While he may have a tenuous adherence to medical ethics, he is nonetheless the primary healing class of the team. Although the Medic's Syringe Gun and Bonesaw aren't the most excellent weapons for direct combat, he can typically still be found near the front lines, healing wounded teammates while trying to stay out of enemy fire.\n\n``... Let's go practice medicine.`` — The Medic")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/9/93/MedicVidSplash.png/300px-MedicVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'pyro':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Pyro', timestamp=ctx.message.created_at,
            description="The Pyro is a mumbling pyromaniac of indeterminate origin who has a burning passion for all things fire related. As shown in Meet the Pyro, the Pyro appears to be insane and delusional, living in a utopian fantasy world known as Pyroland.\n\n``I fear no man. But that... thing... It scares me.`` — The Heavy on the Pyro")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/7/75/PyroVidSplash.png/300px-PyroVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'spy':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Spy', timestamp=ctx.message.created_at,
            description="Hailing from an indeterminate region of France, the Spy is an enthusiast of sharp suits and even sharper knives. Using a unique array of cloaking watches, he can render himself invisible or even fake his own death, leaving unaware opponents off-guard. His Disguise Kit lets him take on the form of any class on either team, allowing him to blend in while behind enemy lines before stabbing his unsuspecting" + ' "teammates" ' + "in the back. In fact, a swift backstab with any of the Spy's knives will kill most foes in a single hit - provided they aren't under the effects of any type of invulnerability, or some other form of immense damage reduction.\n\n``This Spy has already breached our defenses... You've seen what he's done to our colleagues! And worst of all: He could be any one of us.`` — The BLU Spy on the RED Spy")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/9/9a/SpyVidSplash.png/300px-SpyVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'sniper':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Sniper', timestamp=ctx.message.created_at,
            description="Hailing from the lost country of New Zealand and raised in the unforgiving Australian outback, the Sniper is a tough and ready crack shot. The Sniper's main role on the battlefield is to pick off important enemy targets from afar using his Sniper Rifle and its ability to deal guaranteed critical hits with a headshot (with some exceptions). He is effective at long range, but weakens with proximity, where he is forced to use his Submachine Gun or his Kukri. As a result, the Sniper tends to perch on higher grounds or in hard-to-see places, where he can easily pin down enemies at chokepoints.\n\n``Snipin's a good job, mate! It's challengin' work, outta doors. I guarantee you'll not go hungry. 'Cause at the end of the day, long as there's two people left on the planet, someone is gonna want someone dead.`` — The Sniper on his profession")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/e/ea/SniperVidSplash.png/300px-SniperVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'soldier':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Soldier', timestamp=ctx.message.created_at,
            description="The Soldier is a crazed, jingoistic patriot from Midwest, USA. Tough and well-armed, he is versatile, capable of both offense and defense, and a great starter class to get familiar with the game.\n\n``If fighting is sure to result in victory, then you must fight!`` — The Soldier on the art of war")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/c/c9/SoldierVidSplash.png/300px-SoldierVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == 'scout':
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Scout', timestamp=ctx.message.created_at,
            description="Born and raised in Boston, Massachusetts, USA, the Scout is a fast-running scrapper with a baseball bat and a snarky " + '"in-your-face"' + " attitude. He is the fastest and most mobile mercenary on the battlefield unassisted. His Double Jump leaves slower opponents such as the Heavy struggling to keep up and helps him navigate the terrain while dodging oncoming bullets and projectiles. Carrying a Scattergun, a Pistol, and a Bat, the Scout is an ideal class for aggressive fighting and flanking. The Scout is a great class for quick " + '"hit-and-run"' + " tactics that can either sap away enemies' health or kill them outright due to his ability to get in, do damage, and dash away before even being noticed. However, the Scout is tied with the Engineer, Sniper, and Spy for having the lowest health of any class, leaving him vulnerable when he is on the front line; a fair trade-off for his ability to run in and out of a contested hot-spot very quickly, letting him lead the team to victory without the other team even noticing in time.\n\n``Grass grows, birds fly, sun shines, and brother, I hurt people.`` — The Scout on the facts of life")
            embed.set_thumbnail(url='https://wiki.teamfortress.com/w/images/thumb/a/aa/ScoutVidSplash.png/300px-ScoutVidSplash.png')
            await ctx.send(embed=embed)
        elif classes == None:
            embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Team Fortress 2', timestamp=ctx.message.created_at,
            description="Team Fortress 2, the successor to Team Fortress and Team Fortress Classic, was developed by Valve as part of the game compilation The Orange Box and released in 2007 for game consoles and for computers via Steam. It sports a cartoon-like visual style and greatly expands on the gameplay found in its predecessors. Although the abilities of a number of classes have changed from earlier Team Fortress incarnations, the basic elements of each class have remained unchanged. The Steam release of Team Fortress 2 adopted a free to play model in June 2011, with all revenue originating either from microtransaction payments of items in the Mann Co. Store or fees charged for buying items in the Steam Community Market, which opened in beta December 12, 2012.")
            embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/7ad21446-0af2-4334-ac21-c5a0b6308d04/d78kp9s-07d61235-7c6a-4faf-a76f-1b0b1bf8dfc4.png')
            await ctx.send(embed=embed)

    @commands.command(aliases=['announce'])
    @commands.has_permissions(manage_guild=True)
    async def announcement(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 158, 253), title='Announcement', timestamp=ctx.message.created_at, description=message)
        embed.set_footer(text=f'Announced by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['prefix'])
    async def changeprefix(self, ctx):
        await ctx.send(':warning: this command is currently unavailable due to some problems. Im gonna try to fix it as soon as possible.')

    '''@commands.command(aliases=['prefix'])
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

        await ctx.send(embed=embed)'''

def setup(client):
    client.add_cog(Commands(client))