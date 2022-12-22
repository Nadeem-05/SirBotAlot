import discord
from discord.ext import commands
import os
import asyncio
import logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)
version = 1
bot.remove_command('help')
class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('my_extension')


async def main():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")


asyncio.run(main())
bot.run("ODA3OTI2MjA5MDQ0MjgzNDIy.GXtHXK.oDMgkykilcVIl5C2j0yfag9_nB8OSTjUtU4hi0" , log_handler=handler)