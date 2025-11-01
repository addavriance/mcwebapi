"""
Minecraft WebAPI Client
A Python client for interacting with Minecraft servers via WebSocket API.
"""

from .api import MinecraftAPI
from .core import MinecraftClient, Promise
from .objects import Player, Level, Command, Block

__version__ = "0.1.0"
__author__ = "addavriance"

__all__ = [
    "MinecraftAPI",
    "MinecraftClient",
    "Promise",
    "Player",
    "Level",
    "Command",
    "Block",
]