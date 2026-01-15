"""Type stubs for mcwebapi.objects package.

Minecraft entity representations (Player, Block, Level, Command).
"""

from .base import SocketInstance
from .player import Player
from .block import Block
from .level import Level
from .command import Command

__all__ = [
    "SocketInstance",
    "Player",
    "Block",
    "Level",
    "Command",
]
