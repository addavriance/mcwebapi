"""Type stubs for Player API module.

This module provides type hints for Player operations that correspond to
the PlayerApiModule.java backend methods.

Note: The player identifier (username or UUID) is provided during Player
object construction and is automatically sent as the first argument to
all backend methods.
"""

from typing import Any, Dict, List, Optional
from ..core.client import MinecraftClient
from typing import Coroutine, Any

class Player:
    """Represents a Minecraft player.

    Args:
        client: The MinecraftClient instance
        identifier: Player username or UUID
    """

    def __init__(self, client: MinecraftClient, identifier: str) -> None: ...

    # Health & Stats
    def getHealth(self) -> Coroutine[Any, Any, float]:
        """Get player health (hp value or -1.0 if player not found)."""
        ...

    def setHealth(self, health: float) -> Coroutine[Any, Any, bool]:
        """Set player health."""
        ...

    def getMaxHealth(self) -> Coroutine[Any, Any, float]:
        """Get player maximum health."""
        ...

    # Food & Saturation
    def getFood(self) -> Coroutine[Any, Any, int]:
        """Get player food level (0-20)."""
        ...

    def setFood(self, foodLevel: int) -> Coroutine[Any, Any, bool]:
        """Set player food level."""
        ...

    def getSaturation(self) -> Coroutine[Any, Any, float]:
        """Get player saturation level."""
        ...

    def setSaturation(self, saturation: float) -> Coroutine[Any, Any, bool]:
        """Set player saturation level."""
        ...

    # Position & Teleportation
    def getX(self) -> Coroutine[Any, Any, Optional[float]]:
        """Get player X coordinate."""
        ...

    def getY(self) -> Coroutine[Any, Any, Optional[float]]:
        """Get player Y coordinate."""
        ...

    def getZ(self) -> Coroutine[Any, Any, Optional[float]]:
        """Get player Z coordinate."""
        ...

    def getPosition(self) -> Coroutine[Any, Any, Dict[str, float]]:
        """Get player position.

        Returns:
            Dictionary with keys: x, y, z
        """
        ...

    def teleport(self, x: float, y: float, z: float) -> Coroutine[Any, Any, bool]:
        """Teleport player to coordinates."""
        ...

    def teleportTo(self, targetIdentifier: str) -> Coroutine[Any, Any, bool]:
        """Teleport player to another player."""
        ...

    def teleportToDimension(
        self, dimension: str, x: float, y: float, z: float
    ) -> Coroutine[Any, Any, bool]:
        """Teleport player to another dimension.

        Args:
            dimension: Dimension ID (e.g., "minecraft:overworld", "minecraft:the_nether")
            x: X coordinate
            y: Y coordinate
            z: Z coordinate
        """
        ...

    # Rotation & Velocity
    def getRotation(self) -> Coroutine[Any, Any, Dict[str, float]]:
        """Get player rotation.

        Returns:
            Dictionary with keys: yaw, pitch
        """
        ...

    def setRotation(self, yaw: float, pitch: float) -> Coroutine[Any, Any, bool]:
        """Set player rotation."""
        ...

    def getVelocity(self) -> Coroutine[Any, Any, Dict[str, float]]:
        """Get player velocity.

        Returns:
            Dictionary with keys: x, y, z
        """
        ...

    def setVelocity(self, x: float, y: float, z: float) -> Coroutine[Any, Any, bool]:
        """Set player velocity."""
        ...

    # Experience
    def getExperience(self) -> Coroutine[Any, Any, Dict[str, int]]:
        """Get player experience.

        Returns:
            Dictionary with keys: level, total, progress
        """
        ...

    def setExperience(self, level: int) -> Coroutine[Any, Any, bool]:
        """Set player experience level."""
        ...

    # Game Mode
    def getGameMode(self) -> Coroutine[Any, Any, str]:
        """Get player game mode.

        Returns:
            Game mode string (e.g., "SURVIVAL", "CREATIVE", "ADVENTURE", "SPECTATOR")
        """
        ...

    def setGameMode(self, gameMode: str) -> Coroutine[Any, Any, bool]:
        """Set player game mode.

        Args:
            gameMode: Game mode ("SURVIVAL", "CREATIVE", "ADVENTURE", "SPECTATOR")
        """
        ...

    # Inventory & Items
    def getInventory(self) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        """Get player inventory.

        Returns:
            List of items with keys: slot, item, count, damage
        """
        ...

    def clearInventory(self) -> Coroutine[Any, Any, bool]:
        """Clear player inventory."""
        ...

    def getArmor(self) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        """Get player armor.

        Returns:
            List of armor items with keys: slot, item, count, damage
        """
        ...

    def getEnderChest(self) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        """Get player ender chest contents.

        Returns:
            List of items with keys: slot, item, count, damage
        """
        ...

    def giveItem(self, itemId: str, count: int) -> Coroutine[Any, Any, bool]:
        """Give item to player.

        Args:
            itemId: Item resource location (e.g., "minecraft:diamond")
            count: Number of items
        """
        ...

    # Effects
    def getEffects(self) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        """Get player active effects.

        Returns:
            List of effects with keys: effect, amplifier, duration
        """
        ...

    def addEffect(self, effect: str, duration: int, amplifier: int) -> Coroutine[Any, Any, bool]:
        """Add effect to player.

        Args:
            effect: Effect ID (e.g., "minecraft:speed")
            duration: Duration in ticks
            amplifier: Effect amplifier (0 = level 1, 1 = level 2, etc.)
        """
        ...

    def clearEffects(self) -> Coroutine[Any, Any, bool]:
        """Clear all player effects."""
        ...

    # Advancements & Scoring
    def getAdvancements(self) -> Coroutine[Any, Any, Dict[str, Any]]:
        """Get player advancements.

        Returns:
            Complex structure with completed/in-progress advancement lists
        """
        ...

    def grantAdvancement(self, advancementId: str) -> Coroutine[Any, Any, bool]:
        """Grant advancement to player.

        Args:
            advancementId: Advancement resource location (e.g., "minecraft:story/mine_stone")
        """
        ...

    def revokeAdvancement(self, advancementId: str) -> Coroutine[Any, Any, bool]:
        """Revoke advancement from player.

        Args:
            advancementId: Advancement resource location
        """
        ...

    def getScore(self, objective: str) -> Coroutine[Any, Any, int]:
        """Get player score for objective.

        Args:
            objective: Scoreboard objective name

        Returns:
            Score value or -1 if not found
        """
        ...

    def setScore(self, objective: str, score: int) -> Coroutine[Any, Any, bool]:
        """Set player score for objective.

        Args:
            objective: Scoreboard objective name
            score: Score value
        """
        ...

    # Info & Status
    def getUUID(self) -> Coroutine[Any, Any, Optional[str]]:
        """Get player UUID."""
        ...

    def isOnline(self) -> Coroutine[Any, Any, bool]:
        """Check if player is online."""
        ...

    def getPing(self) -> Coroutine[Any, Any, int]:
        """Get player latency in milliseconds.

        Returns:
            Ping value or -1 if offline
        """
        ...

    def getWorld(self) -> Coroutine[Any, Any, str]:
        """Get player current world/dimension.

        Returns:
            Dimension ID (e.g., "minecraft:overworld")
        """
        ...

    def getPlayerInfo(self) -> Coroutine[Any, Any, Dict[str, Any]]:
        """Get comprehensive player information.

        Returns:
            Map with all player stats and information
        """
        ...

    def sendMessage(self, message: str) -> Coroutine[Any, Any, bool]:
        """Send message to player.

        Args:
            message: Message text
        """
        ...

    def kick(self, reason: str) -> Coroutine[Any, Any, bool]:
        """Kick player from server.

        Args:
            reason: Kick reason message
        """
        ...
