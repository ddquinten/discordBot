import discord
from discord.ext import commands

# Voice commands
#---------------------------------------------------------------------
class Voice(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='summon', brief='Summons bot to user VC')
	async def summon(self, ctx):
		voice_channel = ctx.message.author.voice.channel
		if voice_channel != None:
			#channel=voice_channel.name - for printing the channel name
			await voice_channel.connect()

	@commands.command(name='disconnect', brief='Disconnects bot from VCs', aliases = ["dc"])
	async def disconnect(self, ctx):
		if ctx.voice_client is not None:
			await ctx.voice_client.disconnect()

def setup(bot):
	bot.add_cog(Voice(bot))
#---------------------------------------------------------------------