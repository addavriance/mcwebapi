from .core import MinecraftClient
from .objects import Player, World, Command


class MinecraftAPI:
    """
    High-level API client for Minecraft WebSocket API.

    Provides easy access to various entities (player, world, command, system)
    with a clean, intuitive interface.
    """

    def __init__(
            self,
            host: str = "localhost",
            port: int = 8765,
            auth_key: str = "default-secret-key-change-me",
            timeout: float = 10.0,
    ):
        self._client = MinecraftClient(host, port, auth_key, timeout)

        # Initialize entity instances
        self.player = Player(self._client)
        self.world = World(self._client)
        self.command = Command(self._client)

    def connect(self) -> None:
        """Connect to the Minecraft server."""
        self._client.connect()

    def disconnect(self) -> None:
        """Disconnect from the Minecraft server."""
        self._client.disconnect()

    def is_connected(self) -> bool:
        """Check if connected to server."""
        return self._client.is_connected()

    def is_authenticated(self) -> bool:
        """Check if authenticated with server."""
        return self._client.is_authenticated()

    def __enter__(self) -> "MinecraftAPI":
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.disconnect()