# mcwebapi

[![PyPI](https://img.shields.io/pypi/v/mcwebapi?style=for-the-badge&logo=pypi&labelColor=black&color=blue)](https://pypi.org/project/mcwebapi/)
[![Python](https://img.shields.io/pypi/pyversions/mcwebapi?style=for-the-badge&logo=python&labelColor=black)](https://pypi.org/project/mcwebapi/)
[![License](https://img.shields.io/pypi/l/mcwebapi?style=for-the-badge&labelColor=black)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/mcwebapi?style=for-the-badge&labelColor=black&color=green)](https://pypi.org/project/mcwebapi/)

Python client library for the [Minecraft WebSocket API](https://github.com/addavriance/MinecraftWebsocketAPI) mod. Control your Minecraft server programmatically with a clean, async-ready API.

## Installation

```bash
pip install mcwebapi
```

## Quick Start

```python
from mcwebapi import MinecraftAPI

# Context manager automatically connects and authenticates
with MinecraftAPI(
    host="localhost",
    port=8765,
    auth_key="your-secret-key"
) as api:
    # Get player position
    position = api.player.getPosition("Steve").wait()
    print(f"Player at: {position}")
    
    # Send a message
    api.player.sendMessage("Steve", "Hello from Python!").wait()
    
    # Teleport player
    api.player.teleport("Steve", 100, 64, 100).wait()
    
    # Set a block
    api.level.setBlock("minecraft:overworld", "minecraft:diamond_block", 0, 64, 0).wait()
```

## Features

- **Clean API**: Intuitive method names matching the server mod
- **Promise-based**: Async-ready with `.wait()` for synchronous calls or `.then()` for callbacks
- **Type-safe**: Full typing support for better IDE autocomplete
- **Context manager**: Automatic connection management
- **Lightweight**: Minimal dependencies (just `websocket-client`)

## Usage Examples

### Player Operations

```python
with MinecraftAPI() as api:
    # Health management
    health = api.player.getHealth("Steve").wait()
    api.player.setHealth("Steve", 20.0).wait()
    
    # Inventory
    inventory = api.player.getInventory("Steve").wait()
    api.player.giveItem("Steve", "minecraft:diamond", 64).wait()
    api.player.clearInventory("Steve").wait()
    
    # Effects
    api.player.addEffect("Steve", "minecraft:speed", 200, 1).wait()
    effects = api.player.getEffects("Steve").wait()
    
    # Teleportation
    api.player.teleportToDimension("Steve", "minecraft:the_nether", 0, 64, 0).wait()
    
    # Game mode
    api.player.setGameMode("Steve", "creative").wait()
```

### World Operations

```python
with MinecraftAPI() as api:
    # Time control
    api.level.setDayTime("minecraft:overworld", 6000).wait()  # Noon
    is_day = api.level.isDay("minecraft:overworld").wait()
    
    # Weather
    api.level.setWeather("minecraft:overworld", True, False).wait()  # Rain, no thunder
    
    # Blocks
    block = api.level.getBlock("minecraft:overworld", 0, 64, 0).wait()
    api.level.setBlock("minecraft:overworld", "minecraft:stone", 0, 64, 0).wait()
    
    # World info
    levels = api.level.getAvailableLevels().wait()
    info = api.level.getLevelInfo("minecraft:overworld").wait()
```

### Block Operations

```python
with MinecraftAPI() as api:
    # Get block info
    block_info = api.block.getBlock("minecraft:overworld", 10, 64, 10).wait()
    
    # Container inventory
    inventory = api.block.getInventory("minecraft:overworld", 10, 64, 10).wait()
    
    # Set items in containers
    api.block.setInventorySlot(
        "minecraft:overworld", 10, 64, 10,
        slot=0,
        itemId="minecraft:diamond",
        count=64
    ).wait()
    
    # Furnace operations
    furnace = api.block.getFurnaceInfo("minecraft:overworld", 10, 64, 10).wait()
    
    # Fill area (max 10k blocks)
    api.block.fillArea(
        "minecraft:overworld",
        0, 64, 0,  # From
        10, 64, 10,  # To
        "minecraft:glass"
    ).wait()
```

### Async Patterns

#### Using Promises with Callbacks

```python
from mcwebapi import MinecraftAPI

api = MinecraftAPI()
api.connect()

# Chain callbacks
api.player.getPosition("Steve").then(
    lambda pos: print(f"Position: {pos}")
)

# Handle multiple requests
positions = []
for player in ["Steve", "Alex", "Notch"]:
    api.player.getPosition(player).then(
        lambda pos, p=player: positions.append({p: pos})
    )
```

#### Manual Connection Management

```python
from mcwebapi import MinecraftAPI

api = MinecraftAPI(host="192.168.1.100", port=8765, auth_key="secret")

try:
    api.connect()
    
    if api.is_authenticated():
        result = api.player.getHealth("Steve").wait()
        print(result)
        
finally:
    api.disconnect()
```

## API Reference

### MinecraftAPI

Main API class for interacting with the server.

```python
MinecraftAPI(
    host: str = "localhost",
    port: int = 8765,
    auth_key: str = "default-secret-key-change-me",
    timeout: float = 10.0
)
```

**Methods:**
- `connect()` - Establish connection and authenticate
- `disconnect()` - Close connection
- `is_connected() -> bool` - Check connection status
- `is_authenticated() -> bool` - Check authentication status

**Modules:**
- `api.player` - Player operations
- `api.level` - World operations
- `api.block` - Block operations
- `api.command` - Command execution (if implemented server-side)

### Promise API

All API calls return a `Promise` object:

```python
promise = api.player.getHealth("Steve")

# Wait synchronously
result = promise.wait()

# Or use callbacks
promise.then(lambda health: print(f"Health: {health}"))

# Check status
if promise.is_completed():
    if promise.is_successful():
        print(promise.result)
```

## Server Setup

This client requires the Minecraft WebSocket API mod to be installed on your server.

**Mod Repository:** [MinecraftWebsocketAPI](https://github.com/addavriance/MinecraftWebsocketAPI)

1. Install the NeoForge mod on your Minecraft 1.21.1 server
2. Configure `config/mcwebapi-server.toml`:
   ```toml
   [websocket]
       host = "0.0.0.0"
       port = 8765
       authKey = "your-secret-key"
   ```
3. Restart the server

## Requirements

- Python 3.7+
- `websocket-client>=1.3.0`
- Minecraft server with mcwebapi mod installed

## Error Handling

```python
from mcwebapi import MinecraftAPI

with MinecraftAPI() as api:
    try:
        result = api.player.getHealth("NonExistentPlayer").wait()
    except TimeoutError:
        print("Request timed out")
    except Exception as e:
        print(f"Error: {e}")
```

Common exceptions:
- `ConnectionError` - Failed to connect or not authenticated
- `TimeoutError` - Request exceeded timeout duration
- `Exception` - Server-side errors (player not found, invalid arguments, etc.)

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

### Testing

```bash
# Run example
python main.py

# With custom server
python main.py --host 192.168.1.100 --port 8765 --key mysecret
```

## Protocol Details

The client uses WebSocket communication with Base64-encoded JSON messages:

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

## Roadmap

- [ ] Async/await support with asyncio
- [ ] Connection pooling
- [ ] Automatic reconnection
- [ ] Event subscriptions (player join/leave, block changes)
- [ ] Batch operations
- [ ] Response caching

## Contributing

Contributions welcome! Please open an issue or PR on [GitHub](https://github.com/addavriance/mcwebapi).

## License

MIT License - see [LICENSE](LICENSE) file

## Links

- **PyPI:** [pypi.org/project/mcwebapi](https://pypi.org/project/mcwebapi/)
- **Server Mod:** [MinecraftWebsocketAPI](https://github.com/addavriance/MinecraftWebsocketAPI)
- **Issues:** [GitHub Issues](https://github.com/addavriance/mcwebapi/issues)
