from discord.ext import commands

class HelloCommand:
    def __init__(self, bot):
        self.bot = bot

    def register(self):
        @self.bot.command()
        async def hello(ctx):
            await ctx.send('Привіт')




