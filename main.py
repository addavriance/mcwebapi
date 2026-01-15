# Example - Async/Await API
import asyncio
from mcwebapi import MinecraftAPI


async def main():
    """Example showing basic async usage of mcwebapi."""

    # Using async context manager (recommended)
    async with MinecraftAPI() as api:
        player = api.Player("Dev")

        # Get player coordinates
        x = await player.getX()
        y = await player.getY()
        z = await player.getZ()

        print(f"Player position: x={x}, y={y}, z={z}")

        # Or get all at once
        position = await player.getPosition()
        print(f"Full position: {position}")

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
