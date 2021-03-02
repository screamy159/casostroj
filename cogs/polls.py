from discord.ext import commands
import discord


class Polls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, ctx):
        print(ctx.emoji.name, ctx.message_id)

    @commands.command(name="createpoll", aliases=["newpoll", "np", "cp"], brief="Create new poll")
    @commands.guild_only()
    async def _createPoll(self, ctx, *, pollName: str):
        msg = await ctx.send("Please wait..")
        embed = discord.Embed(title=pollName)
        db_id = self.bot.db.new_poll(ctx.author.id, pollName, msg.id)
        embed.set_footer(text=f"ID: {db_id}")
        await msg.edit(content=None, embed=embed)
        await ctx.message.delete()

    @commands.command(name="addoption", aliases=["ao", "addanswer"], brief="Add new option")
    @commands.guild_only()
    async def _addOption(self, ctx, qid: int, emoji: str, *, option: str):
        userID, messageID = self.bot.db.get_poll(qid)
        await ctx.message.delete()
        if userID != ctx.author.id:
            await ctx.send("You cannot do that", delete_after=5)
        else:
            msg = await ctx.fetch_message(messageID)
            embed = msg.embeds[0]
            embed.add_field(name=option, value=emoji)
            await msg.edit(embed=embed)
            await msg.add_reaction(emoji)


def setup(bot):
    bot.add_cog(Polls(bot))
