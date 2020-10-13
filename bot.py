import discord
import random
from datetime import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
# timed commands
"""
async def user_metrics_background_task():
	await bot.wait_until_ready()
	sent = False
	while not bot.is_closed():
		if (datetime.now().second == 10 and sent == False):
			channel = bot.get_channel(758107394789474346)
			await channel.send('@ComboSpag#9089')
			sent = True
			"""


@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

# Basic Commands

# math
@bot.command(brief='a operator b', description='Operators:\nAddtion ~ +\nSubtraction ~ -\nMultiplication ~ *\nDivision ~ /\nModulo ~ %\nAND ~ &\nOR ~ |\nXOR ~ ^\n\n*Note* Bitwise operators must use integer type! Otherwise will trungit cate', usage = '<number> <operator> <number>')
async def math(ctx, *args):
	length = len(args)
	if length < 3:
		await ctx.channel.send('Error: Not enough arguments\nUse "' + bot.command_prefix + 'help math" to view syntax')
	elif length > 3:
		await ctx.channel.send('Error: Too many arguments\nUse "' + bot.command_prefix + 'help math" to view syntax')
	else:

		try:
			a = float(args[0])
			b = float(args[2])
			if args[1] == '+':
				await ctx.channel.send(a + b)
			elif args[1] == '-':
				await ctx.channel.send(a - b)
			elif args[1] == '/':
				if b == 0:
					await ctx.channel.send('Undefined')
				else:
					await ctx.channel.send(a / b)
			elif args[1] == '%':
				if b == 0.0:
					await ctx.channel.send('Undefined')
				else:
					await ctx.channel.send(a % b)
			elif args[1] == '*':
				await ctx.channel.send(int(a) * int(b))
			elif args[1] == '^':
				await ctx.channel.send(int(a) ^ int(b))
			elif args[1] == '&':
				await ctx.channel.send(int(a) & int(b))
			elif args[1] == '|':
				await ctx.channel.send(int(a) | int(b))
			else:
				await ctx.channel.send('Invalid Operator. Use "' + bot.command_prefix + 'help math" to view list of operaters')
		except ValueError:
			await ctx.channel.send('\"a\" and \"b\" of \"a <operator> b\" must be a number')

# doggo
@bot.command(brief='Doggo?', description='Random Doggo Pic!')
async def doggo(ctx):
	embedVar = discord.Embed(color=0x6700f3)
	embedVar.set_image(url='https://dogtime.com/assets/uploads/2018/10/puppies-cover-1280x720.jpg')
	await ctx.channel.send(embed=embedVar)

# inside joke
@bot.command(brief='Doggo?', description='Random Doggo Pic!')
async def insidejoke(ctx, joke = None):
	ran = random.randrange(0,7)
	if joke is not None:
		try:
			ran = int(joke)
		except:
			pass

	if ran == 0:
		await ctx.channel.send(':purple_circle: PURPLE VENTED!!')
	elif ran == 1:
		await ctx.channel.send(':question: Which Oscar?? :question:')
	elif ran == 2:
		await ctx.channel.send('tm8?')
	elif ran == 3:
		await ctx.channel.send("What's the compiler flag to make this work?")
	elif ran == 4:
		await ctx.channel.send('Guys, that was a question.')
	elif ran == 5:
		await ctx.channel.send('BRING BACK TONY!!!')
	elif ran == 6:
		await ctx.channel.send('BOOOOOSTED DONDE ESTAS :hot_face:')
	else:
		await ctx.channel.send("What's the odds that it's me?")

# Admin commands

# updatestatus
@bot.command(brief='ADMIN - Updates Bot status', aliases = ["us"], description='Sets the Bot status in the user panel')
async def updatestatus(ctx, *message):
	if ctx.message.author.guild_permissions.administrator:
		embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
		embedVar.add_field(name="Update Status", value="Playing... " + ' '.join(message), inline=False)
		await ctx.channel.send(embed=embedVar)
		await bot.change_presence(activity=discord.Game(name=' '.join(message)))
	else:
		await ctx.channel.send("You do not have permissions for this command")


# reload
@bot.command(brief='ADMIN - Restart Bot', aliases = ["r"])
async def reload(ctx):
	if ctx.message.author.guild_permissions.administrator:
		pass
	else:
		await ctx.channel.send("You do not have permissions for this command")

# shutdown
@bot.command(brief='ADMIN - Turn off Bot', aliases = ["sd"])
async def shutdown(ctx):
	if ctx.message.author.guild_permissions.administrator:
		embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
		embedVar.add_field(name="Shutdown", value="Shutting down bot...", inline=False)
		await ctx.channel.send(embed=embedVar)
		await bot.logout()
	else:
		await ctx.channel.send("You do not have permissions for this command")

# test
@bot.command(brief='ADMIN - Just a test command')
async def test(ctx):
	if ctx.message.author.guild_permissions.administrator:
		embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
		embedVar.add_field(name="Test Command", value='This is a test command', inline=False)
		await ctx.channel.send(embed=embedVar)
	else:
		await ctx.channel.send("You do not have permissions for this command")

# testargs
@bot.command(brief='ADMIN - Test command args')
async def testargs(ctx, *args):
	if ctx.message.author.guild_permissions.administrator:
		embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
		embedVar.add_field(name="Test Command Arguments", value=str(len(args)) + ' arguments: ' + ', '.join(args), inline=False)
		await ctx.channel.send(embed=embedVar)
	else:
		await ctx.channel.send("You do not have permissions for this command")

"""@bot.event
async def on_message(message):
	await bot.process_commands(message)"""

#bot.loop.create_task(user_metrics_background_task())
bot.run('token')
