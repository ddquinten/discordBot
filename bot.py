import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

# Basic Commands

# math
@bot.command(brief='a operator b', description='Add, subtract, multiply, or divide with this simple calculator')
async def math(ctx, *args):
	if len(args) < 3:
		await ctx.channel.send('Error: Not enough arguments\nMust follow format <float> <operator> <float>')
	elif len(args) > 3:
		await ctx.channel.send('Error: Too many arguments\nMust follow format <float> <operator> <float>')
	else:
		try:
			if args[1] == '+':
				await ctx.channel.send(float(args[0]) + float(args[2]))
			elif args[1] == '-':
				await ctx.channel.send(float(args[0]) - float(args[2]))
			elif args[1] == '/':
				if float(args[2]) == 0.0:
					await ctx.channel.send('Undefined')
				else:
					await ctx.channel.send(float(args[0]) / float(args[2]))
			elif args[1] == '*':
				await ctx.channel.send(float(args[0]) * float(args[2]))
			else:
				await ctx.channel.send('Operator must be \" + - * / \"')
		except ValueError:
			await ctx.channel.send('\"a\" and \"b\" of \"a <operator> b\" must be of type float')

# Admin commands

# updatestatus
@bot.command(brief='ADMIN - Updates Bot status', aliases = ["us"], description='Sets the Bot status in the user panel')
async def updatestatus(ctx, *message):
	if ctx.message.author.guild_permissions.administrator:
		embedVar = discord.Embed(title='Title', description="Desc", color=0x00ff00)
		embedVar.add_field(name='Field1', value='hi', inline= False)
		embedVar.add_field(name='Field2', value='hi2', inline= False)
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
@bot.command(brief='ADMIN - Turn off Bot')
async def shutdown(ctx):
	if ctx.message.author.guild_permissions.administrator:
		pass
	else:
		await ctx.channel.send("You do not have permissions for this command")

# test
@bot.command(brief='ADMIN - Just a test command')
async def test(ctx):
	if ctx.message.author.guild_permissions.administrator:
		await ctx.channel.send('This is a test command')
	else:
		await ctx.channel.send("You do not have permissions for this command")

# testargs
@bot.command(brief='ADMIN - Test command args')
async def testargs(ctx, *args):
	if ctx.message.author.guild_permissions.administrator:
		await ctx.channel.send('{} arguments: {}'.format(len(args), ', '.join(args)))
	else:
		await ctx.channel.send("You do not have permissions for this command")

"""@bot.event
async def on_message(message):
	await bot.process_commands(message)"""

bot.run('NzY1MzAxOTAzNzE0MTU2NTQ2.X4S08A.dVabrrfsCmP-l4MdqNb9OJc5gYw')
