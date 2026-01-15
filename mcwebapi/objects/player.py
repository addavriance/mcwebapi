from typing import List

from .base import SocketInstance
from ..core.client import MinecraftClient
from ..types import (
    Position, Rotation, Velocity, Experience, ItemStack,
    MobEffect, Advancements, PlayerInfo
)


class Player(SocketInstance):
    """Player object for interacting with player-related operations."""

    def __init__(self, client: MinecraftClient, identifier: str):
        super().__init__("player", client, identifier)

    async def sendMessage(self, message: str) -> bool:
        """Send message to player."""
        return await super().__getattr__("sendMessage")(message)

    async def getHealth(self) -> float:
        """Get player health."""
        return await super().__getattr__("getHealth")()

    async def setHealth(self, health: float) -> bool:
        """Set player health."""
        return await super().__getattr__("setHealth")(health)

    async def getMaxHealth(self) -> float:
        """Get player maximum health."""
        return await super().__getattr__("getMaxHealth")()

    async def getX(self) -> float:
        """Get player X coordinate."""
        return await super().__getattr__("getX")()

    async def getY(self) -> float:
        """Get player Y coordinate."""
        return await super().__getattr__("getY")()

    async def getZ(self) -> float:
        """Get player Z coordinate."""
        return await super().__getattr__("getZ")()

    async def getPosition(self) -> Position:
        """Get player position."""
        data = await super().__getattr__("getPosition")()
        return Position(**data)

    async def getRotation(self) -> Rotation:
        """Get player rotation."""
        data = await super().__getattr__("getRotation")()
        return Rotation(**data)

    async def getVelocity(self) -> Velocity:
        """Get player velocity."""
        data = await super().__getattr__("getVelocity")()
        return Velocity(**data)

    async def getFood(self) -> int:
        """Get player food level."""
        return await super().__getattr__("getFood")()

    async def getSaturation(self) -> float:
        """Get player saturation level."""
        return await super().__getattr__("getSaturation")()

    async def getExperience(self) -> Experience:
        """Get player experience."""
        data = await super().__getattr__("getExperience")()
        return Experience(**data)

    async def getGameMode(self) -> str:
        """Get player game mode."""
        return await super().__getattr__("getGameMode")()

    async def getInventory(self) -> List[ItemStack]:
        """Get player inventory."""
        data = await super().__getattr__("getInventory")()
        return [ItemStack(**item) for item in data]

    async def getEffects(self) -> List[MobEffect]:
        """Get active potion effects."""
        data = await super().__getattr__("getEffects")()
        return [MobEffect(**effect) for effect in data]

    async def getAdvancements(self) -> Advancements:
        """Get player advancements."""
        data = await super().__getattr__("getAdvancements")()
        return Advancements.from_dict(data)

    async def getPlayerInfo(self) -> PlayerInfo:
        """Get complete player information."""
        data = await super().__getattr__("getPlayerInfo")()
        return PlayerInfo(**data)

    async def getUUID(self) -> str:
        """Get player UUID."""
        return await super().__getattr__("getUUID")()

    async def getWorld(self) -> str:
        """Get player's current world/dimension."""
        return await super().__getattr__("getWorld")()

    async def getPing(self) -> int:
        """Get player ping/latency."""
        return await super().__getattr__("getPing")()

    async def isOnline(self) -> bool:
        """Check if player is online."""
        return await super().__getattr__("isOnline")()

    async def teleport(self, x: float, y: float, z: float) -> bool:
        """Teleport player to coordinates."""
        return await super().__getattr__("teleport")(x, y, z)

    async def setFood(self, food: int) -> bool:
        """Set player food level."""
        return await super().__getattr__("setFood")(food)

    async def setGameMode(self, gamemode: str) -> bool:
        """Set player game mode."""
        return await super().__getattr__("setGameMode")(gamemode)

    async def kick(self, reason: str) -> bool:
        """Kick player from server."""
        return await super().__getattr__("kick")(reason)
