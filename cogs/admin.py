import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changeprefix", aliases=["prefix"], brief="Change command prefix")
    @commands.has_permissions(administrator=True)
    async def _chp(self, ctx, prefix: str):
        self.bot.db.update_prefix(ctx.guild.id, prefix)
        await ctx.send(f"Prefix se záhadně změnil na {prefix}")


def setup(bot):
    bot.add_cog(Admin(bot))
