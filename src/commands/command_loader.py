import os
import importlib

async def load_commands(bot):
    for filename in os.listdir('src/commands'):
        if filename.endswith('.py') and filename != '__init__.py' and filename != 'command_loader.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'commands.{module_name}')
            command_class = getattr(module, f'{module_name.capitalize()}Command')
            command_instance = command_class(bot)
            command_instance.register()

            