from typing import List

from .base import SocketInstance
from ..core.client import MinecraftClient
from ..types import EntitySpawnResult, EntityInfo, EntitySummary, Position


class Entity(SocketInstance):
    """Entity object for entity management."""

    def __init__(self, client: MinecraftClient, level_id: str):
        super().__init__("entity", client, level_id)

    async def spawn(self, entity_type_id: str, x: float, y: float, z: float) -> EntitySpawnResult:
        """Spawn entity at coordinates."""
        data = await super().__getattr__("spawn")(entity_type_id, x, y, z)
        return EntitySpawnResult(**data)

    async def remove(self, entity_uuid: str) -> bool:
        """Remove entity by UUID."""
        return await super().__getattr__("remove")(entity_uuid)

    async def kill(self, entity_uuid: str) -> bool:
        """Kill entity by UUID."""
        return await super().__getattr__("kill")(entity_uuid)

    async def getInfo(self, entity_uuid: str) -> EntityInfo:
        """Get entity information."""
        data = await super().__getattr__("getInfo")(entity_uuid)
        return EntityInfo.from_dict(data)

    async def getPosition(self, entity_uuid: str) -> Position:
        """Get entity position."""
        data = await super().__getattr__("getPosition")(entity_uuid)
        return Position(**data)

    async def teleport(self, entity_uuid: str, x: float, y: float, z: float) -> bool:
        """Teleport entity to coordinates."""
        return await super().__getattr__("teleport")(entity_uuid, x, y, z)

    async def setVelocity(self, entity_uuid: str, x: float, y: float, z: float) -> bool:
        """Set entity velocity."""
        return await super().__getattr__("setVelocity")(entity_uuid, x, y, z)

    async def getCustomName(self, entity_uuid: str) -> str:
        """Get entity custom name."""
        return await super().__getattr__("getCustomName")(entity_uuid)

    async def setCustomName(self, entity_uuid: str, name: str) -> bool:
        """Set entity custom name."""
        return await super().__getattr__("setCustomName")(entity_uuid, name)

    async def setGlowing(self, entity_uuid: str, glowing: bool) -> bool:
        """Set entity glowing."""
        return await super().__getattr__("setGlowing")(entity_uuid, glowing)

    async def setInvulnerable(self, entity_uuid: str, invulnerable: bool) -> bool:
        """Set entity invulnerable."""
        return await super().__getattr__("setInvulnerable")(entity_uuid, invulnerable)

    async def setFireTicks(self, entity_uuid: str, ticks: int) -> bool:
        """Set entity fire ticks."""
        return await super().__getattr__("setFireTicks")(entity_uuid, ticks)

    async def getEntitiesInRadius(self, x: float, y: float, z: float, radius: float) -> List[EntitySummary]:
        """Get entities within radius."""
        data = await super().__getattr__("getEntitiesInRadius")(x, y, z, radius)
        return [EntitySummary(**entity) for entity in data]

    async def getEntitiesByType(self, entity_type_id: str) -> List[EntitySummary]:
        """Get all entities of specific type."""
        data = await super().__getattr__("getEntitiesByType")(entity_type_id)
        return [EntitySummary(**entity) for entity in data]

    async def getAllEntities(self) -> List[EntitySummary]:
        """Get all entities in level."""
        data = await super().__getattr__("getAllEntities")()
        return [EntitySummary(**entity) for entity in data]

    async def getEntityCount(self) -> int:
        """Get total entity count."""
        return await super().__getattr__("getEntityCount")()

    async def getEntityCountByType(self, type_id) -> int:
        """Get entity count by type."""
        return await super().__getattr__("getEntityCountByType")(type_id)
