import discord
from discord.ext import commands
import database
import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_prefix(bot, message):
    if not message.guild:
        return '.'
    return bot.db.fetch_prefix(message.guild.id)


cogs = ["admin", "random", "quotes", "polls"]
bot = commands.Bot(command_prefix=get_prefix,
                   owner_id=311178459919417344, intents=discord.Intents.default())


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name)
    print('------')

    for x in cogs:
        bot.load_extension(f"cogs.{x}")
        print(x, "loaded!")


@bot.event
async def on_guild_join(guild):
    bot.db.add_prefix(guild.id, ".")


@bot.event
async def on_guild_remove(guild):
    bot.db.remove_prefix(guild.id)


@bot.command(brief="Loads extension")
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    print(extension, "loaded!")


@bot.command(brief="Unload extension")
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    print(extension, "unloaded!")


@bot.command(brief="Reload extension")
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    print(extension, "reloaded!")

bot.db = database.db()
bot.run(os.environ["TOKEN"])
