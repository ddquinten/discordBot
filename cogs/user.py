import discord
import random
from discord.ext import commands
from pathlib import Path

path = str(Path(__file__).parent / "../data")
with open (path + "/insidejokeList.txt") as f:
	IJList = f.readlines()
with open (path + "/insidejokes.txt") as f:
	insidejokes = f.readlines()
with open (path + "/doggourls.txt") as f:
	dogURLs = f.readlines()

# User commands
#---------------------------------------------------------------------
class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# math
	@commands.command(name='math', brief='a operator b', description='Operators:\nAddtion ~ +\nSubtraction ~ -\nMultiplication ~ *\nDivision ~ /\nModulo ~ %\nAND ~ &\nOR ~ |\nXOR ~ ^\n\n*Note* Bitwise operators must use integer type! Otherwise will trungit cate', usage = '<number> <operator> <number>')
	async def math(self, ctx, *args):
		length = len(args)
		if length < 3:
			await ctx.channel.send('Error: Not enough arguments\nUse "' + self.bot.command_prefix + 'help math" to view syntax')
		elif length > 3:
			await ctx.channel.send('Error: Too many arguments\nUse "' + self.bot.command_prefix + 'help math" to view syntax')
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
					await ctx.channel.send('Invalid Operator. Use "' + self.bot.command_prefix + 'help math" to view list of operaters')
			except ValueError:
				await ctx.channel.send('\"a\" and \"b\" of \"a <operator> b\" must be a number')

	# doggo
	@commands.command(name="doggo",brief='Doggo?', description='Random Doggo Pic!')
	async def doggo(self, ctx):
		ran = random.randrange(0, len(dogURLs))
		embedVar = discord.Embed(color=0x6700f3)
		embedVar.set_image(url=dogURLs[ran])
		await ctx.channel.send(embed=embedVar)

	# inside joke
	@commands.command(name="insidejoke", brief='If you get it, you get it...', description='Server Memez\nJoke number is optional\n' + '\n'.join(IJList), usage="<joke_number>")
	async def insidejoke(self, ctx, joke = None):
		ran = random.randrange(0,len(insidejokes))
		if joke is not None:
			try:
				ran = int(joke)
			except:
				pass
		await ctx.channel.send(insidejokes[ran])

def setup(bot):
	bot.add_cog(User(bot))


#---------------------------------------------------------------------