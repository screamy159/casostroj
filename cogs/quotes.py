from os import name
from discord import colour
from discord.ext import commands
import discord


class Quotes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="newquote", aliases=["nq"], brief="Create new quote")
    async def _newQuote(self, ctx, *, quote: str):
        self.bot.db.new_quote(quote, ctx.author.name)
        await ctx.send("Quote added!")

    @commands.command(name="listquotes", aliases=["listquote", "lq"], brief="List all current quotes")
    async def _listQuotes(self, ctx):
        async with ctx.channel.typing():
            quotes = self.bot.db.list_quotes()
            embed = discord.Embed(colour=0x8c8dee, title="Recent Quotes")
            # TODO:
            # SHOW MAXIMALLY 5 LAST QUOTES
            for quote in quotes:
                embed.add_field(
                    name=f"ID: {quote[0]}", value=quote[2], inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Quotes(bot))
