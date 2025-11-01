from .base import SocketInstance
from ..api import MinecraftClient


class Block(SocketInstance):
    """Block object for interacting with blocks, and their inventory if present"""

    def __init__(self, client: MinecraftClient):
        super().__init__("block", client)