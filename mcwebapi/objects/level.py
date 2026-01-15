from typing import List

from .base import SocketInstance
from ..core.client import MinecraftClient
from ..types import (
    BlockState, Weather, WorldBorder, SpawnPoint,
    LevelData, ChunkInfo, LevelInfo
)


class Level(SocketInstance):
    """Level object for interacting with world-related operations."""

    def __init__(self, client: MinecraftClient, identifier: str):
        super().__init__("level", client, identifier)

    async def getBlock(self, x: int, y: int, z: int) -> str:
        """Get block type at coordinates."""
        return await super().__getattr__("getBlock")(x, y, z)

    async def setBlock(self, block_id: str, x: int, y: int, z: int) -> bool:
        """Set block at coordinates."""
        return await super().__getattr__("setBlock")(block_id, x, y, z)

    async def getBlockState(self, x: int, y: int, z: int) -> BlockState:
        """Get detailed block state."""
        data = await super().__getattr__("getBlockState")(x, y, z)
        return BlockState(**data)

    async def getDayTime(self) -> int:
        """Get world day time."""
        return await super().__getattr__("getDayTime")()

    async def setDayTime(self, time: int) -> bool:
        """Set world day time."""
        return await super().__getattr__("setDayTime")(time)

    async def getSeed(self) -> int:
        """Get world seed."""
        return await super().__getattr__("getSeed")()

    async def getWeather(self) -> Weather:
        """Get weather information."""
        data = await super().__getattr__("getWeather")()
        return Weather(**data)

    async def setWeather(self, raining: bool, thundering: bool) -> bool:
        """Set weather."""
        return await super().__getattr__("setWeather")(raining, thundering)

    async def getWorldBorder(self) -> WorldBorder:
        """Get world border information."""
        data = await super().__getattr__("getWorldBorder")()
        return WorldBorder(**data)

    async def setWorldBorder(self, center_x: float, center_z: float, size: float) -> bool:
        """Set world border."""
        return await super().__getattr__("setWorldBorder")(center_x, center_z, size)

    async def getSpawnPoint(self) -> SpawnPoint:
        """Get world spawn point."""
        data = await super().__getattr__("getSpawnPoint")()
        return SpawnPoint(**data)

    async def setSpawnPoint(self, x: int, y: int, z: int, angle: float) -> bool:
        """Set world spawn point."""
        return await super().__getattr__("setSpawnPoint")(x, y, z, angle)

    async def getDifficulty(self) -> str:
        """Get world difficulty."""
        return await super().__getattr__("getDifficulty")()

    async def setDifficulty(self, difficulty: str) -> bool:
        """Set world difficulty."""
        return await super().__getattr__("setDifficulty")(difficulty)

    async def getPlayers(self) -> List[str]:
        """Get list of players in world."""
        return await super().__getattr__("getPlayers")()

    async def getPlayerCount(self) -> int:
        """Get player count in world."""
        return await super().__getattr__("getPlayerCount")()

    async def getEntityCount(self) -> int:
        """Get entity count in world."""
        return await super().__getattr__("getEntityCount")()

    async def getLevelData(self) -> LevelData:
        """Get level metadata."""
        data = await super().__getattr__("getLevelData")()
        return LevelData(**data)

    async def getLevelInfo(self) -> LevelInfo:
        """Get complete level information."""
        data = await super().__getattr__("getLevelInfo")()
        return LevelInfo(**data)

    async def getChunkInfo(self, chunk_x: int, chunk_z: int) -> ChunkInfo:
        """Get chunk information."""
        data = await super().__getattr__("getChunkInfo")(chunk_x, chunk_z)
        return ChunkInfo(**data)

    async def isDay(self) -> bool:
        """Check if it's daytime."""
        return await super().__getattr__("isDay")()

    async def isNight(self) -> bool:
        """Check if it's nighttime."""
        return await super().__getattr__("isNight")()

    async def getMoonPhase(self) -> int:
        """Get moon phase."""
        return await super().__getattr__("getMoonPhase")()