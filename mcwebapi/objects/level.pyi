"""Type stubs for Level/World API module.

This module provides type hints for Level/World operations that correspond to
the WorldApiModule.java backend methods.

Note: The level identifier (dimension) is provided during Level object
construction and is automatically sent as the first argument to all
backend methods.
"""

from typing import Any, Dict, List, Optional
from ..core.client import MinecraftClient
from ..core.promise import Promise

class Level:
    """Represents a Minecraft world/dimension level.

    Args:
        client: The MinecraftClient instance
        identifier: Level/dimension ID (e.g., "minecraft:overworld", "minecraft:the_nether", "minecraft:the_end")

    Example:
        >>> level = Level(client, "minecraft:overworld")
        >>> time = level.getDayTime().wait()
    """

    def __init__(self, client: MinecraftClient, identifier: str) -> None: ...

    # Block Operations
    def setBlock(self, blockId: str, x: int, y: int, z: int) -> Promise[bool]:
        """Set block at position.

        Args:
            blockId: Block type ID (e.g., "minecraft:stone")
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            True if successful
        """
        ...

    def getBlock(self, x: int, y: int, z: int) -> Promise[str]:
        """Get block type at position.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            Block type ID
        """
        ...

    def getBlockState(self, x: int, y: int, z: int) -> Promise[Dict[str, Any]]:
        """Get detailed block state information.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            Dictionary with keys:
                - block (str): Block type ID
                - properties (Dict): Block state properties
                - destroySpeed (float): Block hardness
                - lightEmission (int): Light emission level
        """
        ...

    # Time & Weather
    def getDayTime(self) -> Promise[int]:
        """Get current day time in ticks.

        Returns:
            Day time (0-24000 ticks)
        """
        ...

    def setDayTime(self, time: int) -> Promise[bool]:
        """Set day time.

        Args:
            time: Day time in ticks (0-24000)

        Returns:
            True if successful
        """
        ...

    def getTotalTime(self) -> Promise[int]:
        """Get total world time since creation.

        Returns:
            Total game time in ticks
        """
        ...

    def isDay(self) -> Promise[bool]:
        """Check if it's daytime.

        Returns:
            True if daytime
        """
        ...

    def isNight(self) -> Promise[bool]:
        """Check if it's nighttime.

        Returns:
            True if nighttime
        """
        ...

    def getMoonPhase(self) -> Promise[int]:
        """Get current moon phase.

        Returns:
            Moon phase (0-7)
        """
        ...

    def getWeather(self) -> Promise[Dict[str, Any]]:
        """Get weather information.

        Returns:
            Dictionary with keys:
                - isRaining (bool): Whether it's raining
                - isThundering (bool): Whether it's thundering
                - rainLevel (float): Rain intensity
                - thunderLevel (float): Thunder intensity
        """
        ...

    def setWeather(self, raining: bool, thundering: bool) -> Promise[bool]:
        """Set weather.

        Args:
            raining: Whether it should rain
            thundering: Whether it should thunder

        Returns:
            True if successful
        """
        ...

    # World Border
    def getWorldBorder(self) -> Promise[Dict[str, Any]]:
        """Get world border information.

        Returns:
            Dictionary with keys:
                - centerX (float): Border center X
                - centerZ (float): Border center Z
                - size (float): Border size
                - damagePerBlock (float): Damage per block outside
                - damageSafeZone (float): Safe zone size
                - warningTime (int): Warning time
                - warningBlocks (int): Warning distance
        """
        ...

    def setWorldBorder(self, centerX: float, centerZ: float, size: float) -> Promise[bool]:
        """Set world border.

        Args:
            centerX: Border center X coordinate
            centerZ: Border center Z coordinate
            size: Border diameter size

        Returns:
            True if successful
        """
        ...

    # Terrain & Height
    def getHeight(self, x: int, z: int, heightmapType: str) -> Promise[int]:
        """Get terrain height at position.

        Args:
            x: X coordinate
            z: Z coordinate
            heightmapType: Heightmap type (e.g., "MOTION_BLOCKING", "WORLD_SURFACE", "OCEAN_FLOOR")

        Returns:
            Height Y coordinate
        """
        ...

    def getLightLevel(self, x: int, y: int, z: int) -> Promise[int]:
        """Get light level at position.

        Args:
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            Light level (0-15)
        """
        ...

    # Spawn & Difficulty
    def getSpawnPoint(self) -> Promise[Dict[str, Any]]:
        """Get world spawn point.

        Returns:
            Dictionary with keys:
                - x (int): Spawn X coordinate
                - y (int): Spawn Y coordinate
                - z (int): Spawn Z coordinate
                - angle (float): Spawn angle
        """
        ...

    def setSpawnPoint(self, x: int, y: int, z: int, angle: float) -> Promise[bool]:
        """Set world spawn point.

        Args:
            x: Spawn X coordinate
            y: Spawn Y coordinate
            z: Spawn Z coordinate
            angle: Spawn angle

        Returns:
            True if successful
        """
        ...

    def getDifficulty(self) -> Promise[str]:
        """Get world difficulty.

        Returns:
            Difficulty string ("PEACEFUL", "EASY", "NORMAL", "HARD")
        """
        ...

    def setDifficulty(self, difficulty: str) -> Promise[bool]:
        """Set world difficulty.

        Args:
            difficulty: Difficulty level ("PEACEFUL", "EASY", "NORMAL", "HARD")

        Returns:
            True if successful
        """
        ...

    # Entities & Players
    def getPlayers(self) -> Promise[List[str]]:
        """Get list of player names in this level.

        Returns:
            List of player names
        """
        ...

    def getEntities(self) -> Promise[List[str]]:
        """Get list of entity type IDs in this level.

        Returns:
            List of entity type IDs
        """
        ...

    def getEntityCount(self) -> Promise[int]:
        """Get total entity count in level.

        Returns:
            Number of entities
        """
        ...

    def getPlayerCount(self) -> Promise[int]:
        """Get player count in level.

        Returns:
            Number of players
        """
        ...

    def sendMessageToAll(self, message: str) -> Promise[bool]:
        """Send message to all players in level.

        Args:
            message: Message text

        Returns:
            True if successful
        """
        ...

    # Chunks
    def getChunkInfo(self, chunkX: int, chunkZ: int) -> Promise[Dict[str, Any]]:
        """Get chunk information.

        Args:
            chunkX: Chunk X coordinate
            chunkZ: Chunk Z coordinate

        Returns:
            Dictionary with keys:
                - isLoaded (bool): Whether chunk is loaded
                - inhabitedTime (int): Time chunk has been inhabited
                - chunkX (int): Chunk X coordinate
                - chunkZ (int): Chunk Z coordinate
        """
        ...

    def loadChunk(self, chunkX: int, chunkZ: int) -> Promise[bool]:
        """Load chunk.

        Args:
            chunkX: Chunk X coordinate
            chunkZ: Chunk Z coordinate

        Returns:
            True if successful
        """
        ...

    def unloadChunk(self, chunkX: int, chunkZ: int) -> Promise[bool]:
        """Unload chunk.

        Args:
            chunkX: Chunk X coordinate
            chunkZ: Chunk Z coordinate

        Returns:
            True if successful
        """
        ...

    # World Info
    def getSeed(self) -> Promise[int]:
        """Get world seed.

        Returns:
            World seed
        """
        ...

    def getLevelInfo(self) -> Promise[Dict[str, Any]]:
        """Get comprehensive level information.

        Returns:
            Complete world statistics map
        """
        ...

    def getLevelData(self) -> Promise[Dict[str, Any]]:
        """Get level data.

        Returns:
            Dictionary with keys:
                - levelName (str): Level name
                - hardcore (bool): Hardcore mode enabled
                - allowCommands (bool): Commands allowed
                - gameType (str): Default game type
        """
        ...

    def getAvailableLevels(self) -> Promise[List[str]]:
        """Get list of all available dimensions.

        Returns:
            List of dimension IDs (e.g., ["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"])
        """
        ...

    # Advanced
    def explode(self, x: float, y: float, z: float, power: float, fire: bool) -> Promise[bool]:
        """Create explosion at position.

        Args:
            x: Explosion X coordinate
            y: Explosion Y coordinate
            z: Explosion Z coordinate
            power: Explosion power
            fire: Whether explosion causes fire

        Returns:
            True if successful
        """
        ...
