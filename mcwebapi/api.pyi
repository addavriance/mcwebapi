"""Type stubs for MinecraftAPI main class.

This module provides type hints for the high-level async MinecraftAPI interface.
"""

from typing import Optional
from .core.client import MinecraftClient
from .objects.player import Player
from .objects.block import Block
from .objects.level import Level
from .objects.command import Command
from .objects.server import Server
from .objects.entity import Entity
from .objects.scoreboard import Scoreboard

class MinecraftAPI:
    """High-level async API for interacting with Minecraft server via WebSocket.

    Args:
        host: WebSocket server host (default: "localhost")
        port: WebSocket server port (default: 8765)
        auth_key: Authentication key (default: "default-secret-key-change-me")
        timeout: Request timeout in seconds (default: 10.0)

    Example:
        async with MinecraftAPI() as api:
            player = api.Player("Steve")
            health = await player.getHealth()
            print(f"Health: {health}")
    """

    client: MinecraftClient

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8765,
        auth_key: str = "default-secret-key-change-me",
        timeout: float = 10.0,
    ) -> None: ...

    # Connection Management
    async def connect(self) -> None:
        """Establish connection and authenticate with server."""
        ...

    async def disconnect(self) -> None:
        """Close connection to server."""
        ...

    def is_connected(self) -> bool:
        """Check if connected to server.

        Returns:
            True if connected
        """
        ...

    def is_authenticated(self) -> bool:
        """Check if authenticated with server.

        Returns:
            True if authenticated
        """
        ...

    async def wait_for_pending(self) -> None:
        """Wait for all pending requests to complete."""
        ...

    # Async Context Manager
    async def __aenter__(self) -> "MinecraftAPI":
        """Enter async context manager (connects automatically).

        Returns:
            Self instance
        """
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit async context manager (disconnects automatically)."""
        ...

    # Factory Methods
    def Player(self, identifier: str) -> Player:
        """Create a Player instance.

        Args:
            identifier: Player username or UUID

        Returns:
            Player instance
        """
        ...

    def Level(self, identifier: str) -> Level:
        """Create a Level instance.

        Args:
            identifier: Level/dimension ID (e.g., "minecraft:overworld")

        Returns:
            Level instance
        """
        ...

    def Block(self, levelId: str) -> Block:
        """Create a Block instance.

        Args:
            levelId: Level/dimension ID where blocks will be accessed

        Returns:
            Block instance
        """
        ...

    def Command(self) -> Command:
        """Create a Command instance.

        Returns:
            Command instance
        """
        ...

    def Server(self) -> Server:
        """Create a Server instance.

        Returns:
            Server instance
        """
        ...

    def Entity(self, level_id: str) -> Entity:
        """Create an Entity instance.

        Args:
            level_id: Level/dimension ID where entities will be managed

        Returns:
            Entity instance
        """
        ...

    def Scoreboard(self) -> Scoreboard:
        """Create a Scoreboard instance.

        Returns:
            Scoreboard instance
        """
        ...
