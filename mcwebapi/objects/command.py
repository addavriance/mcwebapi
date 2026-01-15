from .base import SocketInstance
from ..core.client import MinecraftClient
from ..types import CommandResult


class Command(SocketInstance):
    """Command object for executing server commands."""

    def __init__(self, client: MinecraftClient):
        super().__init__("command", client)

    async def executeCommand(self, command: str) -> CommandResult:
        """Execute a server command."""
        data = await super().__getattr__("executeCommand")(command)
        return CommandResult(**data)