import discord
import requests
from discord.ext import commands
import random

class Reddit(commands.Cog):
    """
    Memes from various subreddits
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        meme = requests.get(f"https://meme-api.com/gimme").json()
        em = discord.Embed(title=f"{meme['title']}",colour=discord.Colour(random.randint(1, 16777215)))
        try:
            em.add_field(name="link", value=f"{meme['postLink']}")
        except:
            em.add_field(name="Error", value="Failed")
        try:
            em.set_image(url=f"{meme['url']}")
        except:
            em.add_field(name="Failed", value="Failed to get meme")
        try:
            em.set_footer(text=f"{meme['ups']} 👍")
        except:
            em.set_footer(text="Failed to get likes")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(Reddit(bot))
    print("Reddit cog loaded Successfully")
