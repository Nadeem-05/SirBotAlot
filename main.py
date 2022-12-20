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

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")
            await bot.start("ODA3OTI2MjA5MDQ0MjgzNDIy.GXtHXK.oDMgkykilcVIl5C2j0yfag9_nB8OSTjUtU4hi0")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.

