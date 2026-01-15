"""Type stubs for Entity API module.

This module provides type hints for Entity operations that correspond to
the EntityApiModule.java backend methods.

Note: The level identifier (dimension) is provided during Entity object
construction and is automatically sent as the first argument to all
backend methods.
"""

from typing import Any, Dict, List
from ..core.client import MinecraftClient
from ..core.promise import Promise

class Entity:
    """Represents entity management in a specific level.

    Args:
        client: The MinecraftClient instance
        level_id: Level/dimension identifier (e.g., "minecraft:overworld")

    Example:
        >>> entity = Entity(client, "minecraft:overworld")
        >>> result = entity.spawn("minecraft:zombie", 100, 64, -200).wait()
    """

    def __init__(self, client: MinecraftClient, level_id: str) -> None: ...

    # Entity Creation and Removal
    def spawn(self, entityTypeId: str, x: float, y: float, z: float) -> Promise[Dict[str, Any]]:
        """Spawn entity at position.

        Args:
            entityTypeId: Entity type ID (e.g., "minecraft:zombie", "minecraft:cow")
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            Dictionary with keys:
                - success (bool): Whether spawn succeeded
                - uuid (str, optional): Entity UUID if successful
                - type (str, optional): Entity type
                - x, y, z (float, optional): Spawn coordinates
                - error (str, optional): Error message if failed
        """
        ...

    def remove(self, entityUuid: str) -> Promise[bool]:
        """Remove entity by UUID.

        Args:
            entityUuid: Entity UUID string

        Returns:
            True if successful
        """
        ...

    def kill(self, entityUuid: str) -> Promise[bool]:
        """Kill entity by UUID.

        Args:
            entityUuid: Entity UUID string

        Returns:
            True if successful
        """
        ...

    # Entity Information
    def getInfo(self, entityUuid: str) -> Promise[Dict[str, Any]]:
        """Get detailed entity information.

        Args:
            entityUuid: Entity UUID string

        Returns:
            Dictionary with keys:
                - uuid (str): Entity UUID
                - type (str): Entity type ID
                - x, y, z (float): Position coordinates
                - yaw, pitch (float): Rotation
                - isAlive (bool): Whether entity is alive
                - isOnGround (bool): Whether entity is on ground
                - isSilent (bool): Whether entity is silent
                - isGlowing (bool): Whether entity is glowing
                - isInvulnerable (bool): Whether entity is invulnerable
                - fireImmune (bool): Whether entity is fire immune
                - remainingFireTicks (int): Fire ticks remaining
                - customName (str, optional): Custom name if set
                - velocity (Dict): Velocity vector {x, y, z}
        """
        ...

    def getPosition(self, entityUuid: str) -> Promise[Dict[str, float]]:
        """Get entity position.

        Args:
            entityUuid: Entity UUID string

        Returns:
            Dictionary with keys: x, y, z
        """
        ...

    # Entity Manipulation
    def teleport(self, entityUuid: str, x: float, y: float, z: float) -> Promise[bool]:
        """Teleport entity to coordinates.

        Args:
            entityUuid: Entity UUID string
            x: X coordinate
            y: Y coordinate
            z: Z coordinate

        Returns:
            True if successful
        """
        ...

    def setVelocity(self, entityUuid: str, x: float, y: float, z: float) -> Promise[bool]:
        """Set entity velocity.

        Args:
            entityUuid: Entity UUID string
            x: X velocity
            y: Y velocity
            z: Z velocity

        Returns:
            True if successful
        """
        ...

    # Entity Properties
    def getCustomName(self, entityUuid: str) -> Promise[str]:
        """Get entity custom name.

        Args:
            entityUuid: Entity UUID string

        Returns:
            Custom name or None if not set
        """
        ...

    def setCustomName(self, entityUuid: str, name: str) -> Promise[bool]:
        """Set entity custom name.

        Args:
            entityUuid: Entity UUID string
            name: Custom name text

        Returns:
            True if successful
        """
        ...

    def setGlowing(self, entityUuid: str, glowing: bool) -> Promise[bool]:
        """Set entity glowing effect.

        Args:
            entityUuid: Entity UUID string
            glowing: Whether entity should glow

        Returns:
            True if successful
        """
        ...

    def setInvulnerable(self, entityUuid: str, invulnerable: bool) -> Promise[bool]:
        """Set entity invulnerability.

        Args:
            entityUuid: Entity UUID string
            invulnerable: Whether entity should be invulnerable

        Returns:
            True if successful
        """
        ...

    def setFireTicks(self, entityUuid: str, ticks: int) -> Promise[bool]:
        """Set entity fire ticks.

        Args:
            entityUuid: Entity UUID string
            ticks: Number of fire ticks (20 ticks = 1 second)

        Returns:
            True if successful
        """
        ...

    # Entity Queries
    def getEntitiesInRadius(
        self, x: float, y: float, z: float, radius: float
    ) -> Promise[List[Dict[str, Any]]]:
        """Get all entities within radius of position.

        Args:
            x: Center X coordinate
            y: Center Y coordinate
            z: Center Z coordinate
            radius: Search radius

        Returns:
            List of entity summaries with keys:
                - uuid (str): Entity UUID
                - type (str): Entity type ID
                - x, y, z (float): Position
                - isAlive (bool): Whether alive
                - customName (str, optional): Custom name if set
        """
        ...

    def getEntitiesByType(self, entityTypeId: str) -> Promise[List[Dict[str, Any]]]:
        """Get all entities of specific type.

        Args:
            entityTypeId: Entity type ID (e.g., "minecraft:zombie")

        Returns:
            List of entity summaries
        """
        ...

    def getAllEntities(self) -> Promise[List[Dict[str, Any]]]:
        """Get all entities in the level.

        Returns:
            List of entity summaries
        """
        ...

    def getEntityCount(self) -> Promise[int]:
        """Get total entity count in level.

        Returns:
            Number of entities
        """
        ...

    def getEntityCountByType(self, entityTypeId: str) -> Promise[int]:
        """Get entity count by type.

        Args:
            entityTypeId: Entity type ID

        Returns:
            Number of entities of this type
        """
        ...
