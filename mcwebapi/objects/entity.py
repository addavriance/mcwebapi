from .base import SocketInstance
from ..core.client import MinecraftClient


class Entity(SocketInstance):
    """Entity object for entity management"""

    def __init__(self, client: MinecraftClient, level_id: str):
        super().__init__("entity", client, level_id)
