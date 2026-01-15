"""Type stubs for MinecraftClient core class.

This module provides type hints for the core client that handles
WebSocket communication and request/response handling.
"""

from typing import Any, Dict, Optional
from .connection import ConnectionManager
from .promise import Promise

class MinecraftClient:
    """Core client for handling WebSocket communication with Minecraft server.

    This is the low-level client that manages:
    - Connection lifecycle
    - Authentication
    - Request/response handling
    - Promise resolution

    Args:
        host: WebSocket server host (default: "localhost")
        port: WebSocket server port (default: 8765)
        auth_key: Authentication key (default: "default-secret-key-change-me")
        timeout: Request timeout in seconds (default: 10.0)
    """

    host: str
    port: int
    auth_key: str
    timeout: float
    connection: ConnectionManager
    pending_requests: Dict[str, Promise[Any]]
    _authenticated: bool

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8765,
        auth_key: str = "default-secret-key-change-me",
        timeout: float = 10.0,
    ) -> None: ...

    def connect(self) -> None:
        """Establish connection and authenticate with server.

        Raises:
            Exception: If connection or authentication fails
        """
        ...

    def disconnect(self) -> None:
        """Close connection and cleanup resources."""
        ...

    def is_authenticated(self) -> bool:
        """Check if authenticated with server.

        Returns:
            True if authenticated
        """
        ...

    def is_connected(self) -> bool:
        """Check if connected to server.

        Returns:
            True if connected
        """
        ...

    def has_pending_requests(self) -> bool:
        """Check if there are pending requests.

        Returns:
            True if there are pending requests
        """
        ...

    def send_request(
        self, module: str, method: str, args: Optional[list] = None
    ) -> Promise[Any]:
        """Send request to server and return Promise.

        Args:
            module: Module name (e.g., "player", "block", "level")
            method: Method name (e.g., "getHealth", "setBlock")
            args: Optional list of arguments

        Returns:
            Promise that will be resolved with the response
        """
        ...

    def _authenticate(self) -> None:
        """Perform authentication flow with server.

        Raises:
            Exception: If authentication fails
        """
        ...

    def _handle_message(self, raw_message: str) -> None:
        """Handle incoming WebSocket message.

        Args:
            raw_message: Raw message string
        """
        ...

    def _generate_request_id(self) -> str:
        """Generate unique request ID.

        Returns:
            Short hexadecimal request ID (1-4 characters)
        """
        ...
