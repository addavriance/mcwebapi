import asyncio
from mcwebapi import MinecraftAPI


async def main():
    """Example showing dataclass usage with IDE autocomplete."""

    # Using async context manager (recommended)
    async with MinecraftAPI() as api:
        player = api.Player("Dev")

        # Get player coordinates (typed as float)
        x = await player.getX()
        y = await player.getY()
        z = await player.getZ()

        print(f"Player position: x={x}, y={y}, z={z}")

        # Or get all at once
        position = await player.getPosition()
        print(f"Full position: x={position.x}, y={position.y}, z={position.z}")

        # Get player health and food
        health = await player.getHealth()
        food = await player.getFood()

        print(f"Health: {health}, Food: {food}")

        # Example: Concurrent operations
        print("\nGathering multiple values concurrently...")
        health, food, gamemode = await asyncio.gather(
            player.getHealth(),
            player.getFood(),
            player.getGameMode()
        )

        print(f"Health: {health}, Food: {food}, GameMode: {gamemode}")

        player_info = await player.getPlayerInfo()
        print(f"\nPlayer Info:")
        print(f"  Name: {player_info.name}")
        print(f"  UUID: {player_info.uuid}")
        print(f"  Health: {player_info.health}/{player_info.maxHealth}")
        print(f"  Game Mode: {player_info.gameMode}")
        print(f"  World: {player_info.world}")
        print(f"  Is Flying: {player_info.isFlying}")


async def advanced_example():
    """Example showing manual connection management."""

    api = MinecraftAPI(host="localhost", port=8765, timeout=10.0)

    try:
        await api.connect()
        print(f"Connected: {api.is_connected()}")
        print(f"Authenticated: {api.is_authenticated()}")

        player = api.Player("Dev")
        health = await player.getHealth()
        print(f"Player health: {health}")

    finally:
        await api.disconnect()


if __name__ == "__main__":
    # Run the main example
    asyncio.run(main())

    # Uncomment to run advanced example
    # asyncio.run(advanced_example())
