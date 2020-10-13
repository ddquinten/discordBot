import discord
from discord.ext import commands

# Admin commands
#---------------------------------------------------------------------
class _Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# updatestatus
	@commands.command(name='updatestatus', brief='ADMIN - Updates Bot status', aliases = ["us"], description='Sets the Bot status in the user panel')
	async def updatestatus(self, ctx, *message):
		if ctx.message.author.guild_permissions.administrator:
			embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
			embedVar.add_field(name="Update Status", value="Playing... " + ' '.join(message), inline=False)
			await ctx.channel.send(embed=embedVar)
			await self.bot.change_presence(activity=discord.Game(name=' '.join(message)))
		else:
			await ctx.channel.send("You do not have permissions for this command")


	# reload
	@commands.command(name='reload', brief='ADMIN - Restart Bot', aliases = ["r"])
	async def reload(self, ctx):
		if ctx.message.author.guild_permissions.administrator:
			pass
		else:
			await ctx.channel.send("You do not have permissions for this command")

	# shutdown
	@commands.command(name='shutdown', brief='ADMIN - Turn off Bot', aliases = ["sd"])
	async def shutdown(self, ctx):
		if ctx.message.author.guild_permissions.administrator:
			embedVar = discord.Embed(title='Admin Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
			embedVar.add_field(name="Shutdown", value="Shutting down bot...", inline=False)
			await ctx.channel.send(embed=embedVar)
			if ctx.voice_client is not None:
				await ctx.voice_client.disconnect()
			await self.bot.logout()
		else:
			await ctx.channel.send("You do not have permissions for this command")

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