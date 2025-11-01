from .base import SocketInstance
from ..api import MinecraftClient


class Level(SocketInstance):
    """Level object for interacting with world-related operations"""

    def __init__(self, client: MinecraftClient):
        super().__init__("level", client)