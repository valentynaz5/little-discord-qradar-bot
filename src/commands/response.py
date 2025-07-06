from discord.ext import commands
from views.response_buttons import ResponseButtons

class ResponseCommand:
    def __init__(self, bot):
        self.bot = bot

    def register(self):
        @self.bot.command()
        async def send_message(ctx):
            view = ResponseButtons()
            await ctx.send("Виберіть опцію:", view=view)




