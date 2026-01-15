from .base import SocketInstance
from ..core.client import MinecraftClient


class Server(SocketInstance):
    """Server object for server management"""

    def __init__(self, client: MinecraftClient):
        super().__init__("server", client)
