"""Type stubs for mcwebapi.core package.

Core infrastructure for WebSocket communication and request handling.
"""

from .client import MinecraftClient
from .connection import ConnectionManager
from .promise import Promise

__all__ = [
    "MinecraftClient",
    "ConnectionManager",
    "Promise",
]
