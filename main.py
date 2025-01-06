import os
import interactions as it
from interactions import Client, Intents, listen
from interactions.api.events import *
from interactions import slash_command, SlashContext
from dotenv import load_dotenv
#import logging

load_dotenv('.env')



bot = Client(basic_logging=True, 
             intents=Intents.GUILDS | Intents.DEFAULT,
             sync_ext=True, 
             sync_interactions=True,
             delete_unused_commands=True, 
             send_command_tracebacks=False)
#logging.basicConfig(level=logging.DEBUG)


@listen(Ready)
async def on_ready():
    await bot.change_presence(activity=it.Activity(name="Idle Clans",type= it.ActivityType.WATCHING))
    print(f"Logged in as {bot.user.username}!")
    await bot.synchronise_interactions()

bot.load_extension("cogs.player")
#bot.load_extension("cogs.clan") 
#bot.load_extension("cogs.market") 
#init the players log file




bot.start(token=os.getenv("TOKEN"))

