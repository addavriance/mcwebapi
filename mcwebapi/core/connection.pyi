"""Type stubs for ConnectionManager class.

This module provides type hints for the WebSocket connection management.
"""

from typing import Any, Callable, Dict, Optional
import threading
from websocket import WebSocketApp

class ConnectionManager:
    """Manages WebSocket connection to Minecraft server.

    Handles:
    - Connection establishment
    - Message encoding/decoding (Base64 + JSON)
    - Message sending/receiving
    - Receiver thread management

    Args:
        host: WebSocket server host (default: "localhost")
        port: WebSocket server port (default: 8765)
    """

    host: str
    port: int
    ws: Optional[WebSocketApp]
    receiver_thread: Optional[threading.Thread]
    running: bool
    connected: bool

    def __init__(self, host: str = "localhost", port: int = 8765) -> None: ...

    def connect(self) -> None:
        """Establish WebSocket connection.

        Raises:
            Exception: If connection fails
        """
        ...

    def disconnect(self) -> None:
        """Close WebSocket connection and cleanup."""
        ...

    def is_connected(self) -> bool:
        """Check if WebSocket is connected.

        Returns:
            True if connected
        """
        ...

    def send_message(self, message: Dict[str, Any]) -> None:
        """Send message through WebSocket.

        Args:
            message: Message dictionary to send
        """
        ...

    def start_receiver(self, message_handler: Callable[[str], None]) -> None:
        """Start message receiver thread.

        Args:
            message_handler: Callback function to handle received messages
        """
        ...

    def _receiver_loop(self) -> None:
        """Main receiver loop for incoming messages (runs in separate thread)."""
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
