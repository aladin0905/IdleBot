import asyncio
import bisect
from datetime import datetime, timedelta
import json
import math
import os
from pprint import pprint
import sys
import time
import aiohttp
from aiohttp import ClientSession
from tenacity import retry, stop_after_attempt, wait_fixed
import interactions
import interactions as it
from interactions import ( Client,listen,Embed, EmbedField,
                            slash_command,slash_option, Extension,
                            OptionType,SlashCommandOption,SlashCommandChoice,
                            StringSelectOption,StringSelectMenu,
                            Task, IntervalTrigger)
from interactions import SlashContext as SC
from interactions import ComponentContext as CPC 
from interactions.api.events import *
from interactions.api.events import Component
from interactions.ext.paginators import Paginator
from interactions.ext.paginators import Page

import pymongo
from dotenv import load_dotenv
from typing import Dict, Any, Optional


all_skills=["overall","melee","magic","mining","smithing","woodcutting","crafting",
                    "fishing","cooking","tailoring"]

class Player(Extension):
    def __init__(self, client:Client):
        self.bot = client
        self.player_endpoint = "https://query.idleclans.com/api/Player/profile/"
        self.semaphore = asyncio.Semaphore(10)
        self.timeout = aiohttp.ClientTimeout(total=300)
        self.session = None  # Initialize session as None

    async def __aenter__(self):
        # Create the session asynchronously when the bot loads the extension
        if self.session is None:
            self.session = aiohttp.ClientSession(timeout=self.timeout)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Properly close the session when the extension unloads
        if self.session:
            await self.session.close()


    async def get_player_info(self, player_name:str) -> dict:
        if not self.session:
            self.session = aiohttp.ClientSession(timeout=self.timeout)
        url:str = self.player_endpoint+player_name
        async with self.session.get(url=url) as response:
            if response.status in [200, 201]:
                data:dict = await response.json()
                pprint(data)
            else:
                print(f"{player_name} doesn't exist.")


    
        
    @slash_command(name="search_player", description="search for player by name", scopes=[1195866066908360835])
    @slash_option(name='name' ,description="the player's name", opt_type=OptionType.STRING, required=True)
    async def start_event(self, ctx:SC,name:str):
        await self.get_player_info(player_name=name)




















def setup(client : Client):
    Player(client)
    print("player loaded")