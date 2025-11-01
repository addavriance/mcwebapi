from .base import SocketInstance
from ..api import MinecraftClient


class Player(SocketInstance):
    """Player object for interacting with player-related operations"""

    def __init__(self, client: MinecraftClient):
        super().__init__("player", client)