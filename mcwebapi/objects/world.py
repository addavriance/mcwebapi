from .base import SocketInstance
from ..api import MinecraftClient


class World(SocketInstance):
    """World object for interacting with world-related operations"""

    def __init__(self, client: MinecraftClient):
        super().__init__("world", client)