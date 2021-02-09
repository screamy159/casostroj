from discord.ext import commands
import discord


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="f")
    async def _sendF(self, ctx):
        message = await ctx.send("Press F to pay respect")
        await message.add_reaction("<:regional_indicator_f:>")


def setup(bot):
    bot.add_cog(Random(bot))
