"""Type stubs for Command API module.

This module provides type hints for Command operations.

Note: The backend Server API module is currently not implemented in the Java backend,
so specific command methods are not yet defined. Methods can be added dynamically
once the backend implements them.
"""

from ..core.client import MinecraftClient
from .base import SocketInstance

class Command(SocketInstance):
    """Command object for executing server commands.

    Args:
        client: The MinecraftClient instance

    Note: This class currently has no predefined methods as the backend
    Server API module is empty. Methods will be dynamically created based
    on future backend implementations.
    """

    def __init__(self, client: MinecraftClient) -> None: ...
