from .base import SocketInstance
from ..core.client import MinecraftClient


class Player(SocketInstance):
    """Player object for interacting with player-related operations"""

    def __init__(self, client: MinecraftClient, identifier):
        super().__init__("player", client, identifier)
