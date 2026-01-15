"""Type stubs for ConnectionManager class.

This module provides type hints for the async WebSocket connection management.
"""

from typing import Any, Callable, Dict, Optional
import asyncio
from websockets.client import WebSocketClientProtocol

class ConnectionManager:
    """Manages async WebSocket connection to Minecraft server.

    Handles:
    - Async connection establishment
    - Message encoding/decoding (Base64 + JSON)
    - Message sending/receiving
    - Receiver task management

    Args:
        host: WebSocket server host (default: "localhost")
        port: WebSocket server port (default: 8765)
    """

    host: str
    port: int
    ws: Optional[WebSocketClientProtocol]
    _receiver_task: Optional[asyncio.Task]
    _connected: bool

    def __init__(self, host: str = "localhost", port: int = 8765) -> None: ...

    async def connect(self) -> None:
        """Establish async WebSocket connection.

        Raises:
            Exception: If connection fails
        """
        ...

    async def disconnect(self) -> None:
        """Close WebSocket connection and cleanup."""
        ...

    def is_connected(self) -> bool:
        """Check if WebSocket is connected.

        Returns:
            True if connected
        """
        ...

    async def send_message(self, message: Dict[str, Any]) -> None:
        """Send message through WebSocket.

        Args:
            message: Message dictionary to send
        """
        ...

    def start_receiver(self, message_handler: Callable[[str], None]) -> None:
        """Start message receiver task.

        Args:
            message_handler: Callback function to handle received messages
        """
        ...

    async def _receiver_loop(self) -> None:
        """Main async receiver loop for incoming messages (runs as task)."""
        ...

    def _encode_message(self, message: Dict[str, Any]) -> str:
        """Encode message to Base64 JSON string.

        Args:
            message: Message dictionary

        Returns:
            Base64 encoded JSON string
        """
        ...

    def _decode_message(self, message: str) -> Dict[str, Any]:
        """Decode Base64 string to message dictionary.

        Args:
            message: Base64 encoded JSON string

        Returns:
            Decoded message dictionary
        """
        ...
