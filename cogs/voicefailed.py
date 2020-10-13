import discord
import youtube_dl
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

from discord.ext import commands

# Voice commands
#---------------------------------------------------------------------
class Voice(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# summon
	@commands.command(name='summon', brief='Summons bot to user VC')
	async def summon(self, ctx):
		voice_channel = ctx.message.author.voice.channel
		if voice_channel != None:
			#channel=voice_channel.name - for printing the channel name
			await voice_channel.connect()

	# disconnect
	@commands.command(name='disconnect', brief='Disconnects bot from VCs', aliases = ["dc"])
	async def disconnect(self, ctx):
		if ctx.voice_client is not None:
			await ctx.voice_client.disconnect()



	# play
	@commands.command(pass_context=True)
	async def play(self, ctx, url: str):
		song_there = os.path.isfile("song.mp3")
		try:
			if song_there:
				os.remove("song.mp3")
		except PermissionError:
			await ctx.send("Wait for the current playing music end or use the 'stop' command")
			return

		voice = get(self.bot.voice_clients, guild=ctx.guild)
		ydl_opts = {
		'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
				}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		for file in os.listdir("./"):
			if file.endswith(".mp3"):
				os.rename(file, 'song.mp3')
		voice.play(discord.FFmpegPCMAudio("song.mp3"))
		voice.volume = 100



def setup(bot):
	bot.add_cog(Voice(bot))



#---------------------------------------------------------------------