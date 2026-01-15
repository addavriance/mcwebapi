"""Type stubs for mcwebapi package.

Minecraft WebSocket API - A Python client library for interacting with
Minecraft servers via WebSocket API.
"""

from .api import MinecraftAPI
from .core.client import MinecraftClient
from .core.promise import Promise
from .objects.player import Player
from .objects.block import Block
from .objects.level import Level
from .objects.command import Command
from .objects.server import Server
from .objects.entity import Entity
from .objects.scoreboard import Scoreboard

__version__: str

__all__ = [
    "MinecraftAPI",
    "MinecraftClient",
    "Promise",
    "Player",
    "Block",
    "Level",
    "Command",
    "Server",
    "Entity",
    "Scoreboard",
]
