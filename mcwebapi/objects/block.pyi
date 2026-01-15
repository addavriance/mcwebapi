"""Type stubs for Block API module.

This module provides type hints for Block operations that correspond to
the BlockApiModule.java backend methods.

Note: The level identifier (dimension) is provided during Block object
construction and is automatically sent as the first argument to all
backend methods.
"""

from typing import Any, Dict, List, Optional
from ..core.client import MinecraftClient
from ..core.promise import Promise

class Block:
    """Represents a block or block position in Minecraft.

    Args:
        client: The MinecraftClient instance
        levelId: Level/dimension identifier (e.g., "minecraft:overworld")

    Example:
        >>> block = Block(client, "minecraft:overworld")
        >>> block_info = block.getBlock(100, 64, -200).wait()
    """

    def __init__(self, client: MinecraftClient, levelId: str) -> None: ...

    # Block Inspection
    def getBlock(self, x: int, y: int, z: int) -> Promise[Dict[str, Any]]:
        """Get detailed block information at position.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            Dictionary with keys:
                - type (str): Block type ID
                - x (int): X coordinate
                - y (int): Y coordinate
                - z (int): Z coordinate
                - properties (Dict[str, str]): Block state properties
                - lightLevel (int): Total light level
                - skyLight (int): Sky light level
                - blockLight (int): Block light level
                - hasBlockEntity (bool): Whether block has block entity
                - blockEntityType (str, optional): Block entity type if present
        """
        ...

    # Block Manipulation
    def setBlock(self, x: int, y: int, z: int, blockId: str) -> Promise[bool]:
        """Set block at position.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate
            blockId: Block type ID (e.g., "minecraft:stone")

        Returns:
            True if successful
        """
        ...

    def breakBlock(self, x: int, y: int, z: int, dropItems: bool) -> Promise[bool]:
        """Break block at position.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate
            dropItems: Whether to drop items when breaking

        Returns:
            True if successful
        """
        ...

    # Container Operations
    def getInventory(self, x: int, y: int, z: int) -> Promise[Dict[str, Any]]:
        """Get inventory of container block (chest, barrel, etc.).

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            Dictionary with keys:
                - blockType (str): Block type
                - hasBlockEntity (bool): Has block entity
                - blockEntityType (str, optional): Block entity type
                - inventory (List[Dict], optional): List of items if container
                    Each item has: slot, item, count, maxStackSize, damage, maxDamage, displayName
                - size (int): Inventory size
                - error (str, optional): Error message if not a container
        """
        ...

    def setInventorySlot(
        self, x: int, y: int, z: int, slot: int, itemId: str, count: int
    ) -> Promise[bool]:
        """Set item in container inventory slot.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate
            slot: Inventory slot index
            itemId: Item resource location (e.g., "minecraft:diamond")
            count: Number of items

        Returns:
            True if successful
        """
        ...

    def clearInventory(self, x: int, y: int, z: int) -> Promise[bool]:
        """Clear container inventory.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            True if successful
        """
        ...

    # Furnace Operations
    def getFurnaceInfo(self, x: int, y: int, z: int) -> Promise[Dict[str, Any]]:
        """Get furnace information.

        Args:
            x: Block X coordinate
            y: Block Y coordinate
            z: Block Z coordinate

        Returns:
            Dictionary with keys:
                - type (str): Furnace type
                - isBurning (bool): Whether furnace is active
                - burnTime (int): Remaining burn time
                - cookTime (int): Current cook time
                - cookTimeTotal (int): Total cook time required
                - input (str, optional): Input item type
                - inputCount (int, optional): Input item count
                - fuel (str, optional): Fuel item type
                - fuelCount (int, optional): Fuel item count
                - output (str, optional): Output item type
                - outputCount (int, optional): Output item count
        """
        ...
