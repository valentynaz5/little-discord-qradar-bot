import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN
from commands.command_loader import load_commands

class Bot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix='@', intents=intents)
        self.bot.event(self.on_ready)
        
    async def on_ready(self):
        await load_commands(self.bot)

    def run(self):
        self.bot.run(DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    bot = Bot()
    bot.run()







