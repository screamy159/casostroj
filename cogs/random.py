from discord.ext import commands
import discord


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="f", brief="Press F to pay respect")
    async def _sendF(self, ctx):
        message = await ctx.send("Press F to pay respect")
        await message.add_reaction("🇫")

    @commands.command(name="cmds", brief="Show all commands")
    async def _commands(self, ctx):
        async with ctx.channel.typing():
            embed = discord.Embed(colour=0x8c8dee, title="Commands")
            for command in self.bot.walk_commands():
                embed.add_field(name=command.name,
                                value=command.brief, inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Random(bot))
