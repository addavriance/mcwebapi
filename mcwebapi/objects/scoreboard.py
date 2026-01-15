from .base import SocketInstance
from ..core.client import MinecraftClient


class Scoreboard(SocketInstance):
    """Scoreboard object for scoreboard management"""

    def __init__(self, client: MinecraftClient):
        super().__init__("scoreboard", client)
