"""Type stubs for base SocketInstance class.

This module provides type hints for the base class that all Minecraft
API objects inherit from.
"""

from typing import Callable, Dict, Tuple
from ..core.client import MinecraftClient
from typing import Coroutine, Any

class SocketInstance:
    """Base class for all Minecraft API objects.

    This class handles dynamic method dispatching to the backend server.
    Methods are created dynamically based on backend module definitions.

    Args:
        name: Module name (e.g., "player", "block", "level")
        client: The MinecraftClient instance
        *args: Entry arguments that are automatically prepended to all method calls
    """

    name: str
    client: MinecraftClient
    entry_args: Tuple[Any, ...]

    def __init__(self, name: str, client: MinecraftClient, *args: Any) -> None: ...

    def __getattr__(self, name: str) -> Callable[..., Coroutine[Any, Any, Any]]:
        """Dynamically create method that sends request to backend.

        Args:
            name: Method name

        Returns:
            Callable that returns a Promise when invoked
        """
        ...

    def _process_args(self, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> list:
        """Process arguments for server call.

        Combines entry_args with method arguments.

        Args:
            args: Method positional arguments
            kwargs: Method keyword arguments (currently not used)

        Returns:
            List of arguments to send to server
        """
        ...
