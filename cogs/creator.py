import discord
from discord.ext import commands

CREATOR_ID = 346221622979461120
# Admin commands
#---------------------------------------------------------------------
class __Creator(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# updatestatus
	@commands.command(name='updatestatus', brief='CREATOR - Updates Bot status', aliases = ["us"], description='Sets the Bot status in the user panel', hidden=True)
	async def updatestatus(self, ctx, *message):
		if ctx.message.author.id == CREATOR_ID:
			embedVar = discord.Embed(title='Creator Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
			embedVar.add_field(name="Update Status", value="Playing... " + ' '.join(message), inline=False)
			await ctx.channel.send(embed=embedVar)
			await self.bot.change_presence(activity=discord.Game(name=' '.join(message)))
		else:
			await ctx.channel.send("You do not have permissions for this command")

	# reload
	@commands.command(name='reload', brief='CREATOR - Restart Bot', aliases = ["r"], hidden=True)
	async def reload(self, ctx):
		if ctx.message.author.id == CREATOR_ID:
			pass
		else:
			await ctx.channel.send("You do not have permissions for this command")

	# shutdown
	@commands.command(name='shutdown', brief='CREATOR - Turn off Bot', aliases = ["sd"], hidden=True)
	async def shutdown(self, ctx):
		if ctx.message.author.id == CREATOR_ID:
			embedVar = discord.Embed(title='Creator Command', description="Called by " + ctx.message.author.name, color=0x6700F3)
			embedVar.add_field(name="Shutdown", value="Shutting down bot...", inline=False)
			await ctx.channel.send(embed=embedVar)
			if ctx.voice_client is not None:
				await ctx.voice_client.disconnect()
			await self.bot.logout()
		else:
			await ctx.channel.send("You do not have permissions for this command")

def setup(bot):
	bot.add_cog(__Creator(bot))
#---------------------------------------------------------------------