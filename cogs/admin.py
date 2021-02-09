import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["prefix"])
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix: str):
        self.bot.db.update_prefix(ctx.guild.id, prefix)
        await ctx.send(f"Prefix se záhadně změnil na {prefix}")
    
def setup(bot):
    bot.add_cog(Admin(bot))
