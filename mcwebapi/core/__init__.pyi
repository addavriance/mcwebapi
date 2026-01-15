"""Type stubs for mcwebapi.core package.

Core infrastructure for async WebSocket communication and request handling.
"""

from .client import MinecraftClient
from .connection import ConnectionManager

__all__ = [
    "MinecraftClient",
    "ConnectionManager",
]
