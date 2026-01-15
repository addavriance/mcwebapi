# mcwebapi

# WARNING: This package is under active development.
## This package is not yet ready for production use! Many things and specifications may change



[![PyPI](https://img.shields.io/pypi/v/mcwebapi?style=for-the-badge&logo=pypi&labelColor=black&color=blue)](https://pypi.org/project/mcwebapi/)
[![Python](https://img.shields.io/pypi/pyversions/mcwebapi?style=for-the-badge&logo=python&labelColor=black)](https://pypi.org/project/mcwebapi/)
[![Downloads](https://img.shields.io/pypi/dm/mcwebapi?style=for-the-badge&labelColor=black&color=green)](https://pypi.org/project/mcwebapi/)

Async Python client library for the [Minecraft WebSocket API](https://github.com/addavriance/MinecraftWebsocketAPI) mod. Control your Minecraft server programmatically with a clean, async/await API.

## Quick Start

```python
import asyncio
import math
import random

from mcwebapi import MinecraftAPI

async def main():
    async with MinecraftAPI() as api:
        try:
            player = api.Player("Dev")

            while True:
                position = await player.getPosition()
                x, y, z = position.values()

                s_x, s_y, s_z = math.floor(x), y-0.5, math.floor(z)

                block = api.Block('minecraft:overworld')
                block_info = await block.getBlock(s_x, s_y, s_z)

                available_blocks = ['minecraft:diamond_block', 'minecraft:gold_block', 'minecraft:iron_block']

                if block_info['type'] == 'minecraft:air':
                    await block.setBlock(s_x, s_y, s_z, random.choice(available_blocks))

                await asyncio.sleep(0.1)  # Don't spam the server

        except TimeoutError:
            print("Request timed out")

if __name__ == "__main__":
    asyncio.run(main())
```

## Features

- **Clean Async API**: Modern async/await syntax with asyncio
- **Type-safe**: Full typing support with .pyi stubs for better IDE autocomplete
- **Context manager**: Automatic connection management with async context managers
- **Lightweight**: Minimal dependencies (just `websockets`)
- **Multiple modules**: Player, Level, Block, Server, Entity, and Scoreboard management

## Installation

```bash
pip install mcwebapi
```

## Usage Examples

### Player Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def player_operations():
    async with MinecraftAPI() as api:
        player = api.Player("Steve")

        # Health management
        health = await player.getHealth()
        print(f"Current health: {health}")
        await player.setHealth(20.0)

        # Inventory
        inventory = await player.getInventory()
        print(f"Inventory: {inventory}")
        await player.giveItem("minecraft:diamond", 64)
        await player.clearInventory()

        # Effects
        await player.addEffect("minecraft:speed", 200, 1)
        effects = await player.getEffects()
        print(f"Active effects: {effects}")

        # Teleportation
        await player.teleportToDimension("minecraft:the_nether", 0, 64, 0)

        # Game mode
        await player.setGameMode("creative")

asyncio.run(player_operations())
```

### World Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def world_operations():
    async with MinecraftAPI() as api:
        level = api.Level("minecraft:overworld")

        # Time control
        await level.setDayTime(6000)  # Noon
        is_day = await level.isDay()
        print(f"Is daytime: {is_day}")

        # Weather
        await level.setWeather(True, False)  # Rain, no thunder
        weather = await level.getWeather()
        print(f"Weather: {weather}")

        # Blocks
        block_type = await level.getBlock(0, 64, 0)
        await level.setBlock("minecraft:stone", 0, 64, 0)

        # World info
        levels = await level.getAvailableLevels()
        info = await level.getLevelInfo()

asyncio.run(world_operations())
```

### Block Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def block_operations():
    async with MinecraftAPI() as api:
        block = api.Block("minecraft:overworld")

        # Get block info
        block_info = await block.getBlock(10, 64, 10)
        print(f"Block info: {block_info}")

        # Set block
        await block.setBlock(10, 64, 10, "minecraft:diamond_block")

        # Break block with drops
        await block.breakBlock(10, 64, 10, dropItems=True)

        # Container inventory (chests, barrels, etc.)
        inventory = await block.getInventory(10, 64, 10)

        # Set items in containers
        await block.setInventorySlot(10, 64, 10, slot=0, itemId="minecraft:diamond", count=64)

        # Furnace info
        furnace_info = await block.getFurnaceInfo(10, 64, 10)

asyncio.run(block_operations())
```

### Server Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def server_operations():
    async with MinecraftAPI() as api:
        server = api.Server()

        # Server info
        info = await server.getInfo()
        print(f"Server: {info['version']} - {info['brand']}")
        print(f"TPS: {info['averageTPS']}")

        # Players
        players = await server.getOnlinePlayers()
        print(f"Online players: {players}")

        # Memory usage
        memory = await server.getMemoryUsage()
        print(f"Memory: {memory['used']}/{memory['max']}")

        # Execute command
        result = await server.executeCommand("time set day")

        # Broadcast message
        await server.broadcast("Hello from Python!")

asyncio.run(server_operations())
```

### Entity Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def entity_operations():
    async with MinecraftAPI() as api:
        entity = api.Entity("minecraft:overworld")

        # Spawn entity
        result = await entity.spawn("minecraft:zombie", 100, 64, -200)
        entity_uuid = result['uuid']

        # Get entity info
        info = await entity.getInfo(entity_uuid)
        print(f"Entity: {info}")

        # Teleport entity
        await entity.teleport(entity_uuid, 110, 64, -210)

        # Set custom name
        await entity.setCustomName(entity_uuid, "Bob the Zombie")

        # Make it glow
        await entity.setGlowing(entity_uuid, True)

        # Get entities in radius
        nearby = await entity.getEntitiesInRadius(100, 64, -200, radius=10)
        print(f"Nearby entities: {len(nearby)}")

        # Remove entity
        await entity.remove(entity_uuid)

asyncio.run(entity_operations())
```

### Scoreboard Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def scoreboard_operations():
    async with MinecraftAPI() as api:
        scoreboard = api.Scoreboard()

        # Create objective
        await scoreboard.createObjective("kills", "dummy", "Kill Count")
        await scoreboard.setDisplaySlot("SIDEBAR", "kills")

        # Set scores
        await scoreboard.setScore("kills", "Player1", 10)
        await scoreboard.addScore("kills", "Player1", 5)  # Now 15

        # Get scores
        score = await scoreboard.getScore("kills", "Player1")
        print(f"Player1 kills: {score}")

        # Create team
        await scoreboard.createTeam("red")
        await scoreboard.setTeamColor("red", "RED")
        await scoreboard.setTeamPrefix("red", "[RED] ")
        await scoreboard.addPlayerToTeam("red", "Player1")

        # Get teams
        teams = await scoreboard.getTeams()
        print(f"Teams: {teams}")

asyncio.run(scoreboard_operations())
```

### Concurrent Operations

```python
import asyncio
from mcwebapi import MinecraftAPI

async def concurrent_operations():
    async with MinecraftAPI() as api:
        # Gather multiple operations concurrently
        player1 = api.Player("Steve")
        player2 = api.Player("Alex")

        # Run operations in parallel
        health1, health2 = await asyncio.gather(
            player1.getHealth(),
            player2.getHealth()
        )

        print(f"Steve: {health1}, Alex: {health2}")

        # Set health for both players concurrently
        await asyncio.gather(
            player1.setHealth(20.0),
            player2.setHealth(20.0)
        )

asyncio.run(concurrent_operations())
```

### Manual Connection Management

```python
import asyncio
from mcwebapi import MinecraftAPI

async def manual_connection():
    api = MinecraftAPI(host="192.168.1.100", port=8765, auth_key="secret")

    try:
        await api.connect()

        if api.is_authenticated():
            player = api.Player("Steve")
            health = await player.getHealth()
            print(f"Health: {health}")

    finally:
        await api.disconnect()

asyncio.run(manual_connection())
```

## API Reference

### MinecraftAPI

Main async API class for interacting with the server.

```python
MinecraftAPI(
    host: str = "localhost",
    port: int = 8765,
    auth_key: str = "default-secret-key-change-me",
    timeout: float = 10.0
)
```

**Methods:**
- `async connect()` - Establish connection and authenticate
- `async disconnect()` - Close connection
- `is_connected() -> bool` - Check connection status
- `is_authenticated() -> bool` - Check authentication status
- `async wait_for_pending()` - Wait for all pending requests

**Async Context Manager:**
```python
async with MinecraftAPI() as api:
    # API operations here
    pass
# Auto-disconnects after the block
```

**Modules:**
- `api.Player(identifier)` - Player operations
- `api.Level(level_id)` - World operations
- `api.Block(level_id)` - Block operations
- `api.Server()` - Server management
- `api.Entity(level_id)` - Entity management
- `api.Scoreboard()` - Scoreboard operations

### Async Methods

All API methods return coroutines that must be awaited:

```python
player = api.Player("Steve")

# Await the result
health = await player.getHealth()
print(f"Health: {health}")

# Run multiple operations concurrently
await asyncio.gather(
    player.setHealth(20.0),
    player.setFood(20),
    player.setSaturation(5.0)
)
```

## Server Setup

This client requires the Minecraft WebSocket API mod to be installed on your server.

**Mod Repository:** [MinecraftWebsocketAPI](https://github.com/addavriance/MinecraftWebsocketAPI)

1. Install the NeoForge mod on your Minecraft 1.21.1 server
2. Configure `config/mcwebapi-server.toml`:
   ```toml
   [websocket]
       #WebSocket server port
       # Default: 8765
       # Range: 1000 ~ 65535
       port = 8765
       #Authentication key for binary protocol
       authKey = "default-secret-key-change-me"
       #Enable TLS/SSL encryption
       enableSSL = false
       #Request timeout in seconds
       # Default: 30
       # Range: 1 ~ 300
       timeout = 30
       #Allowed origins for CORS
       allowedOrigins = "*"
       #WebSocket server host
       host = "0.0.0.0"
   ```
3. Restart the server or join the world

## Requirements

- Python 3.8+
- `websockets>=12.0`
- Minecraft 1.21.1 server with mcwebapi mod installed

## Error Handling

```python
import asyncio
from mcwebapi import MinecraftAPI

async def error_handling():
    async with MinecraftAPI() as api:
        try:
            player = api.Player("NonExistentPlayer")
            health = await player.getHealth()  # May return -1.0 for offline players
            print(f"Health: {health}")

        except TimeoutError:
            print("Request timed out")
        except ConnectionError:
            print("Connection error")
        except Exception as e:
            print(f"Error: {e}")

asyncio.run(error_handling())
```

Common exceptions:
- `ConnectionError` - Failed to connect or not authenticated
- `TimeoutError` - Request exceeded timeout duration
- `Exception` - Server-side errors (invalid arguments, method not found, etc.)

## Configuration

### Timeout

Default timeout is 10 seconds. Adjust per instance:

```python
api = MinecraftAPI(timeout=30.0)  # 30 second timeout
```

### Logging

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Development

### Setup

```bash
git clone https://github.com/addavriance/mcwebapi.git
cd mcwebapi
pip install -e .
```

### Running Examples

```bash
python examples/player_operations.py
```

## Protocol Details

The client uses async WebSocket communication with Base64-encoded JSON messages:

**Request:**
```json
{
  "type": "REQUEST",
  "module": "player",
  "method": "getHealth",
  "args": ["Steve"],
  "requestId": "a1b",
  "timestamp": 1699564800.0
}
```

**Response:**
```json
{
  "type": "RESPONSE",
  "status": "SUCCESS",
  "data": 20.0,
  "requestId": "a1b",
  "timestamp": 1699564800000
}
```

## Changelog

### 0.3.0 (Latest)
- ✅ **Full async/await support** - Complete rewrite using asyncio
- ✅ **New modules** - Added Server, Entity, and Scoreboard modules
- ✅ **Type stubs** - Full .pyi stubs for all modules
- ✅ **Better performance** - Native asyncio for efficient concurrent operations
- ❌ **Breaking**: Removed Promise API - use native async/await instead
- ❌ **Breaking**: Minimum Python version is now 3.8

### 0.2.0
- Initial release with Promise-based API

## Roadmap

- [ ] Event subscriptions (player join/leave, block changes)
- [ ] Batch operations API
- [ ] Response caching
- [ ] Reconnection handling
- [ ] SSL/TLS support

## Contributing

Contributions welcome! Please open an issue or PR on [GitHub](https://github.com/addavriance/mcwebapi).

## Links

- **PyPI:** [pypi.org/project/mcwebapi](https://pypi.org/project/mcwebapi/)
- **Server Mod:** [MinecraftWebsocketAPI](https://github.com/addavriance/MinecraftWebsocketAPI)
- **Issues:** [GitHub Issues](https://github.com/addavriance/mcwebapi/issues)
