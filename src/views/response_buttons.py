import discord
from handlers.json_handler import save_to_json
from handlers.qradar_handler import send_to_qradar_table

class ResponseButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="OK", style=discord.ButtonStyle.green)
    async def ok_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        username = str(interaction.user)
        save_to_json(username, 'OK')
        await interaction.response.send_message(f'{username} вибрав OK!', ephemeral=True)

    @discord.ui.button(label="NOT OK", style=discord.ButtonStyle.red)
    async def not_ok_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        username = str(interaction.user)
        send_to_qradar_table(username, '{username} NOT OK!')
        await interaction.response.send_message(f'{username} вибрав NOT OK!', ephemeral=True)




