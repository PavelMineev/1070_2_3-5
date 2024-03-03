import discord
from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Бот запущен")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Google API code
    await bot.process_commands(message)


bot.run(TOKEN)