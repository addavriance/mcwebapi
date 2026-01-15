"""Type stubs for mcwebapi.objects package.

Minecraft entity representations (Player, Block, Level, Command).
"""

from .base import SocketInstance
from .player import Player
from .block import Block
from .level import Level
from .command import Command
from .server import Server
from .entity import Entity
from .scoreboard import Scoreboard

__all__ = [
    "SocketInstance",
    "Player",
    "Block",
    "Level",
    "Command",
    "Server",
    "Entity",
    "Scoreboard",
]
