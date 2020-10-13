import asyncio
import discord
import youtube_dl
import json
import urllib.parse, urllib.request
import re
import os
from os import system
from discord.ext import commands
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
	'format': 'm4a',
	'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
	'restrictfilenames': True,
	'noplaylist': True,
	'nocheckcertificate': True,
	'ignoreerrors': False,
	'logtostderr': False,
	'quiet': True,
	'no_warnings': True,
	'default_search': 'auto',
	'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
	'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
	def __init__(self, source, *, data, volume=0.5):
		super().__init__(source, volume)

		self.data = data

		self.title = data.get('title')
		self.url = data.get('url')

	@classmethod
	async def from_url(cls, url, *, loop=None, stream=False):
		loop = loop or asyncio.get_event_loop()
		data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
		if 'entries' in data:
			# take first item from a playlist
			data = data['entries'][0]

		#filename = data['url'] if stream else ytdl.prepare_filename(data)
		for file in os.listdir("./"):
			if file.endswith(".m4a"):
				os.rename(file,'song.m4a')
		return cls(discord.FFmpegPCMAudio('song.m4a', **ffmpeg_options), data=data)


class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def join(self, ctx):
		"""Joins a voice channel"""
		voice_channel = ctx.message.author.voice.channel
		if voice_channel != None:
			await voice_channel.connect()

	@commands.command()
	async def search(self, ctx, *args):
		"""Searches youtube with given search"""
		search = " ".join(args)
		qry_str = urllib.parse.urlencode({
			'search_query': search
		})
		htm_content = urllib.request.urlopen(
			'http://www.youtube.com/results?' + qry_str
		)

		search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())

		embedVar = discord.Embed(title='Youtube Search - ' + search, color=0x6700F3)
		for i in range(0, 10):
			qry_str = urllib.parse.urlencode({
			'format': 'json',
			'url': 'https://www.youtube.com/watch?v=' + search_results[i]
			})
			
			with urllib.request.urlopen('https://www.youtube.com/oembed?' + qry_str) as response:
				data = json.loads(response.read().decode())
				embedVar.add_field(name="\u200b", value= data['title'] + "\n" + str(i+1) + ' http://www.youtube.com/watch?v=' + search_results[i], inline=False)
		await ctx.channel.send(embed=embedVar)#'https://www.youtube.com/watch?v=' + search_results[0])

	@commands.command()
	async def play(self, ctx, *, url):
		"""Plays from a url (almost anything youtube_dl supports)"""
		song_there = os.path.isfile("song.m4a")
		try:
			if song_there:
				os.remove("song.m4a")
		except PermissionError:
			await ctx.send("Wait for the current playing music end or use the 'stop' command")
			return

		async with ctx.typing():
			player = await YTDLSource.from_url(url, loop=self.bot.loop)
			ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send('Now playing: {}'.format(player.title))

	@commands.command()
	async def stream(self, ctx, *, url):
		"""Streams from a url (same as yt, but doesn't predownload)"""

		async with ctx.typing():
			player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
			ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

		await ctx.send('Now playing: {}'.format(player.title))

	@commands.command()
	async def volume(self, ctx, volume: int):
		"""Changes the player's volume"""

		if ctx.voice_client is None:
			return await ctx.send("Not connected to a voice channel.")

		ctx.voice_client.source.volume = volume / 100
		await ctx.send("Changed volume to {}%".format(volume))

	@commands.command(name='pause', brief='Pauses current playing music')
	async def pause(self, ctx):
		if ctx.voice_client.is_playing():
			ctx.voice_client.pause()
		else:
			await ctx.channel.send("There is no music currently playing")

	@commands.command(name='stop', brief='Stops current playing music')
	async def stop(self, ctx):
		if ctx.voice_client.is_playing():
			ctx.voice_client.stop()
		else:
			await ctx.channel.send("There is no music currently playing")

	@commands.command(name='resume', brief='Resumes playing music')
	async def resume(self, ctx):
		if ctx.voice_client.is_paused():
			ctx.voice_client.resume()
		else:
			await ctx.channel.send("There is no music currently playing")

	@commands.command(name='disconnect', brief='Disconnects bot from VCs', aliases = ["dc"])
	async def disconnect(self, ctx):
		"""Stops and disconnects the bot from voice"""
		await ctx.voice_client.disconnect()

	@play.before_invoke
	#@yt.before_invoke
	@stream.before_invoke
	async def ensure_voice(self, ctx):
		if ctx.voice_client is None:
			if ctx.author.voice:
				await ctx.author.voice.channel.connect()
			else:
				await ctx.send("You are not connected to a voice channel.")
				raise commands.CommandError("Author not connected to a voice channel.")
		elif ctx.voice_client.is_playing():
			ctx.voice_client.stop()

def setup(bot):
	bot.add_cog(Music(bot))
#---------------------------------------------------------------------

"""
	@commands.command()
	async def play(self, ctx, *, query):
		#Plays a file from the local filesystem

		source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
		ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

		await ctx.send('Now playing: {}'.format(query))
"""