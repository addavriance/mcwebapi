# mcwebapi Examples

This directory contains practical examples demonstrating various features of the Minecraft WebSocket API client.

## Prerequisites

1. **Minecraft server** with the WebSocket API mod installed and running
2. **Python 3.12+** with mcwebapi installed
3. **Server configuration** matching the examples (default: localhost:8765)

## Running Examples

Each example is a standalone script. Run them with:

```bash
python examples/01_basic_usage.py
```

Make sure you're connected to a Minecraft server with a player named "Dev" (or modify the player name in the scripts).

## Examples Overview

### 🎯 Beginner Examples

#### 01_basic_usage.py
**Basic API operations and server information**

Learn the fundamentals:
- Connecting to the API
- Getting player information (health, position, game mode)
- Retrieving server statistics
- Using dataclass types with dot notation

```bash
python examples/01_basic_usage.py
```

---

### 🏗️ Block Manipulation

#### 02_block_bridge.py
**Automatic bridge builder that follows the player**

Creates glass blocks under the player as they walk for 10 seconds.

Features:
- Real-time position tracking
- Dynamic block placement
- Loop-based automation

```bash
python examples/02_block_bridge.py
```

#### 04_tower_builder.py
**Builds a colorful rainbow tower**

Constructs a 20-block tall tower with different colored wool blocks and a beacon on top.

Features:
- Multi-block structures
- Layer-by-layer construction
- Player teleportation

```bash
python examples/04_tower_builder.py
```

#### 12_particle_circle.py
**Animated glowing circle**

Creates a circle of glowstone blocks that pulses and disappears.

Features:
- Circle geometry with math
- Block animation
- Sequential placement/removal

```bash
python examples/12_particle_circle.py
```

---

### 👤 Player Operations

#### 03_player_monitor.py
**Real-time player statistics monitor**

Live updating dashboard showing player stats, position, rotation, and status.

Features:
- Continuous monitoring loop
- Terminal screen updates
- Multiple concurrent data fetches
- Status indicators (health bars, etc.)

Press `Ctrl+C` to stop.

```bash
python examples/03_player_monitor.py
```

#### 10_potion_effects.py
**Potion effects manager**

Applies and manages various potion effects on the player.

Features:
- Multiple effect application
- Effect inspection
- Timed effects
- Effect clearing

```bash
python examples/10_potion_effects.py
```

#### 11_inventory_manager.py
**Inventory inspection and management**

Displays inventory contents and gives items to the player.

Features:
- Inventory listing
- Item counting and grouping
- Giving items
- Armor inspection

```bash
python examples/11_inventory_manager.py
```

---

### 🌍 World Control

#### 09_world_controller.py
**World settings and environment control**

Demonstrates control over time, weather, and world properties.

Features:
- Time of day cycling
- Weather manipulation (rain, thunder, clear)
- World information retrieval
- Spawn point inspection

```bash
python examples/09_world_controller.py
```

---

### 🚀 Advanced Automation

#### 05_teleport_circle.py
**Circular teleportation animation**

Teleports the player in a smooth circular path around a center point.

Features:
- Mathematical circle calculation
- Smooth teleportation
- Progress tracking

```bash
python examples/05_teleport_circle.py
```

#### 07_entity_spawner.py
**Entity spawning in circular pattern**

Spawns various friendly mobs in a circle around the player.

Features:
- Multiple entity types
- Circle positioning with trigonometry
- Entity manipulation (custom names, glowing effect)
- Entity information retrieval

```bash
python examples/07_entity_spawner.py
```

---

### 📊 Monitoring & Management

#### 06_server_monitor.py
**Real-time server performance monitor**

Live dashboard displaying server TPS, memory usage, and player count.

Features:
- Performance metrics (TPS)
- Memory usage visualization
- Player list
- Auto-updating display

Press `Ctrl+C` to stop.

```bash
python examples/06_server_monitor.py
```

#### 08_scoreboard_manager.py
**Scoreboard and team management**

Creates objectives, manages scores, and sets up teams.

Features:
- Objective creation
- Score management
- Team creation and configuration
- Display slot configuration
- Leaderboard generation

```bash
python examples/08_scoreboard_manager.py
```

---

## Common Patterns

### Async Context Manager (Recommended)

```python
async with MinecraftAPI() as api:
    player = api.Player("Dev")
    position = await player.getPosition()
    print(f"Position: {position.x}, {position.y}, {position.z}")
```

### Manual Connection Management

```python
api = MinecraftAPI()
try:
    await api.connect()
    # Your code here
finally:
    await api.disconnect()
```

### Using Dataclass Types

```python
from mcwebapi.types import Position, PlayerInfo

position: Position = await player.getPosition()
print(position.x)  # IDE suggests x, y, z

info: PlayerInfo = await player.getPlayerInfo()
print(info.health)  # IDE suggests all fields
```

### Real-time Monitoring Loop

```python
while True:
    info = await player.getPlayerInfo()
    print(f"Health: {info.health}")
    await asyncio.sleep(1)  # Update every second
```

### Block Manipulation Loop

```python
for i in range(10):
    await block_api.setBlock(x, y + i, z, "minecraft:stone")
    await asyncio.sleep(0.1)  # Small delay for effect
```

## Customization

All examples use these default settings:
- **Host**: localhost
- **Port**: 8765
- **Player**: "Dev"
- **Auth Key**: "default-secret-key-change-me"

To modify, edit the connection parameters:

```python
async with MinecraftAPI(
    host="your-server.com",
    port=8765,
    auth_key="your-secret-key"
) as api:
    # Your code
```

Or change the player name:

```python
player = api.Player("YourUsername")
```

## Tips

1. **Run one at a time**: Some examples modify the world, so run them individually
2. **Watch the game**: Many examples create visual effects - watch your Minecraft client!
3. **Check server logs**: Useful for debugging connection issues
4. **Modify values**: Change block types, colors, radii, etc. to experiment
5. **Combine examples**: Mix and match concepts to create your own automations

## Troubleshooting

**Connection refused**
- Ensure Minecraft server is running
- Verify WebSocket API mod is installed
- Check host/port settings

**Authentication failed**
- Verify auth_key matches server configuration
- Check server logs for details

**Player not found**
- Make sure player "Dev" exists and is online
- Or change the player name in the script

## Next Steps

- Combine multiple examples to create complex automations
- Create your own scripts using these as templates
- Explore the full API documentation
- Build mini-games or server management tools

Happy coding! 🚀
