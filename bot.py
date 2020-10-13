import discord
from datetime import datetime
from discord.ext import commands

# Global vars
#---------------------------------------------------------------------
# File data
with open ("data/botkey.txt") as f:
	TOKEN = f.read()

# Others
bot = commands.Bot(command_prefix='.')


# Command Extensions
#---------------------------------------------------------------------

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name=".help"))
	print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
	await bot.process_commands(message)

# Admin commands
bot.load_extension("cogs.admin")

# Basic commands
bot.load_extension("cogs.user")

# Voice commands
bot.load_extension("cogs.music")



# timed commands
#---------------------------------------------------------------------
# on timer - this case every tenth second of every minute
"""async def user_metrics_background_task():
	await bot.wait_until_ready()
	sent = False
	while not bot.is_closed():
		if (datetime.now().second == 10 and sent == False):
			channel = bot.get_channel(758107394789474346)
			await channel.send('{}'.format('@ComboSpag#9089'))
			sent = True
			"""

#bot.loop.create_task(user_metrics_background_task())
bot.help_command.cog = bot.get_cog("User")
bot.run(TOKEN)
