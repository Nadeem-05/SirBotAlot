import discord
from discord.ext import commands


class Events(commands.Cog):
    """
    Discord events
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=discord.Game(name="use >help to see what i do"))
        print('Main file loaded.Good to go!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if "hello bot" in message.content.lower():
            # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
            await message.channel.reply('Hello')
            await self.bot.process_commands(message)


def setup(bot):
    await bot.add_cog(Events(bot))
    print("Tools cog loaded successfully")
