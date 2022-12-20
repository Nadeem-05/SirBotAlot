import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content=True
bot = commands.Bot(command_prefix=">", intents=intents)
version = 1
bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("ODA3OTI2MjA5MDQ0MjgzNDIy.GXtHXK.oDMgkykilcVIl5C2j0yfag9_nB8OSTjUtU4hi0")
