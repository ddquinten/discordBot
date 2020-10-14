import discord
from discord.ext import commands

# Admin commands
#---------------------------------------------------------------------
class _Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# test
	@commands.command(name='test', brief='ADMIN - Just a test command')
	async def test(self, ctx):
		if ctx.message.author.guild_permissions.administrator:
			embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
			embedVar.add_field(name="Test Command", value='This is a test command', inline=False)
			await ctx.channel.send(embed=embedVar)
		else:
			await ctx.channel.send("You do not have permissions for this command")

	# testargs
	@commands.command(name='testargs', brief='ADMIN - Test command args')
	async def testargs(self, ctx, *args):
		if ctx.message.author.guild_permissions.administrator:
			embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
			embedVar.add_field(name="Test Command Arguments", value=str(len(args)) + ' arguments: ' + ', '.join(args), inline=False)
			await ctx.channel.send(embed=embedVar)
		else:
			await ctx.channel.send("You do not have permissions for this command")


def setup(bot):
	bot.add_cog(_Admin(bot))
#---------------------------------------------------------------------