"""Type stubs for Server API module.

This module provides type hints for Server operations that correspond to
the ServerApiModule.java backend methods.

Note: Server module methods don't require an identifier, as they operate
on the global server instance.
"""

from typing import Any, Dict, List
from ..core.client import MinecraftClient
from typing import Coroutine, Any

class Server:
    """Represents the Minecraft server.

    Args:
        client: The MinecraftClient instance
    """

    def __init__(self, client: MinecraftClient) -> None: ...

    # Server Information
    def getInfo(self) -> Coroutine[Any, Any, Dict[str, Any]]:
        """Get comprehensive server information.

        Returns:
            Dictionary with keys:
                - version (str): Server version
                - brand (str): Server brand (e.g., "NeoForge")
                - motd (str): Message of the day
                - maxPlayers (int): Maximum player count
                - onlinePlayerCount (int): Current online players
                - difficulty (str): Server difficulty
                - isHardcore (bool): Hardcore mode enabled
                - defaultGameMode (str): Default game mode
                - ticksRunning (int): Total ticks
                - averageTPS (float): Average TPS
        """
        ...

    def getVersion(self) -> Coroutine[Any, Any, str]:
        """Get server version string."""
        ...

    def getBrand(self) -> Coroutine[Any, Any, str]:
        """Get server brand (e.g., "NeoForge", "Forge", "Paper")."""
        ...

    def getMotd(self) -> Coroutine[Any, Any, str]:
        """Get message of the day."""
        ...

    def getMaxPlayers(self) -> Coroutine[Any, Any, int]:
        """Get maximum player count."""
        ...

    def getOnlinePlayerCount(self) -> Coroutine[Any, Any, int]:
        """Get current online player count."""
        ...

    def getOnlinePlayers(self) -> Coroutine[Any, Any, List[str]]:
        """Get list of online player names."""
        ...

    def getOnlinePlayerUUIDs(self) -> Coroutine[Any, Any, List[str]]:
        """Get list of online player UUIDs."""
        ...

    # Performance Metrics
    def getTPS(self) -> Coroutine[Any, Any, float]:
        """Get current server TPS (ticks per second).

        Returns:
            TPS value (max 20.0)
        """
        ...

    def getAverageTPS(self) -> Coroutine[Any, Any, float]:
        """Get average server TPS.

        Returns:
            Average TPS value (max 20.0)
        """
        ...

    def getTickCount(self) -> Coroutine[Any, Any, int]:
        """Get total ticks since server start."""
        ...

    def getUptime(self) -> Coroutine[Any, Any, int]:
        """Get server uptime in milliseconds."""
        ...

    def getMemoryUsage(self) -> Coroutine[Any, Any, Dict[str, int]]:
        """Get JVM memory usage.

        Returns:
            Dictionary with keys:
                - max (int): Max memory
                - total (int): Total allocated memory
                - free (int): Free memory
                - used (int): Used memory
        """
        ...

    # Server Settings
    def getDifficulty(self) -> Coroutine[Any, Any, str]:
        """Get server difficulty.

        Returns:
            Difficulty string ("PEACEFUL", "EASY", "NORMAL", "HARD")
        """
        ...

    def setDifficulty(self, difficulty: str) -> Coroutine[Any, Any, bool]:
        """Set server difficulty.

        Args:
            difficulty: Difficulty level ("PEACEFUL", "EASY", "NORMAL", "HARD")

        Returns:
            True if successful
        """
        ...

    def isHardcore(self) -> Coroutine[Any, Any, bool]:
        """Check if server is in hardcore mode."""
        ...

    def getDefaultGameMode(self) -> Coroutine[Any, Any, str]:
        """Get default game mode for new players."""
        ...

    def setDefaultGameMode(self, gameMode: str) -> Coroutine[Any, Any, bool]:
        """Set default game mode.

        Args:
            gameMode: Game mode ("survival", "creative", "adventure", "spectator")

        Returns:
            True if successful
        """
        ...

    # Server Management
    def executeCommand(self, command: str) -> Coroutine[Any, Any, Dict[str, Any]]:
        """Execute console command.

        Args:
            command: Command to execute (without leading /)

        Returns:
            Dictionary with keys:
                - success (bool): Whether command succeeded
                - error (str, optional): Error message if failed
        """
        ...

    def broadcast(self, message: str) -> Coroutine[Any, Any, bool]:
        """Broadcast message to all players.

        Args:
            message: Message text

        Returns:
            True if successful
        """
        ...

    def save(self) -> Coroutine[Any, Any, bool]:
        """Save all worlds.

        Returns:
            True if successful
        """
        ...

    def stop(self) -> Coroutine[Any, Any, bool]:
        """Stop the server.

        Returns:
            True if stop initiated
        """
        ...

    # Whitelist Management
    def getWhitelist(self) -> Coroutine[Any, Any, List[str]]:
        """Get whitelisted player names."""
        ...

    def isWhitelistEnabled(self) -> Coroutine[Any, Any, bool]:
        """Check if whitelist is enabled."""
        ...

    def setWhitelistEnabled(self, enabled: bool) -> Coroutine[Any, Any, bool]:
        """Enable or disable whitelist.

        Args:
            enabled: Whether whitelist should be enabled

        Returns:
            True if successful
        """
        ...

    # Operators and Bans
    def getOperators(self) -> Coroutine[Any, Any, List[str]]:
        """Get list of operator names."""
        ...

    def getBannedPlayers(self) -> Coroutine[Any, Any, List[str]]:
        """Get list of banned player names."""
        ...

    def getBannedIPs(self) -> Coroutine[Any, Any, List[str]]:
        """Get list of banned IP addresses."""
        ...
