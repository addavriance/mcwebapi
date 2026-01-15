from .base import SocketInstance
from ..core.client import MinecraftClient
from ..types import BlockInfo, BlockInventory, FurnaceInfo


class Block(SocketInstance):
    """Block object for interacting with blocks and their inventory if present."""

    def __init__(self, client: MinecraftClient, level_id: str):
        super().__init__("block", client, level_id)

    async def getBlock(self, x: int, y: int, z: int) -> BlockInfo:
        """Get block information at coordinates."""
        data = await super().__getattr__("getBlock")(x, y, z)
        return BlockInfo(**data)

    async def setBlock(self, x: int, y: int, z: int, block_id: str) -> bool:
        """Set block at coordinates."""
        return await super().__getattr__("setBlock")(x, y, z, block_id)

    async def breakBlock(self, x: int, y: int, z: int, drop_items: bool = True) -> bool:
        """Break block at coordinates."""
        return await super().__getattr__("breakBlock")(x, y, z, drop_items)

    async def getInventory(self, x: int, y: int, z: int) -> BlockInventory:
        """Get block entity inventory."""
        data = await super().__getattr__("getInventory")(x, y, z)
        return BlockInventory.from_dict(data)

    async def setInventorySlot(self, x: int, y: int, z: int, slot: int, item_id: str, count: int) -> bool:
        """Set block entity inventory slot."""
        return await super().__getattr__("setInventorySlot")(x, y, z, slot, item_id, count);

    async def clearInventory(self, x: int, y: int, z: int) -> bool:
        """Clear block entity inventory."""
        return await super().__getattr__("clearInventory")(x, y, z)

    async def getFurnaceInfo(self, x: int, y: int, z: int) -> FurnaceInfo:
        """Get furnace information."""
        data = await super().__getattr__("getFurnaceInfo")(x, y, z)
        return FurnaceInfo(**data)
