# Example

from mcwebapi import MinecraftAPI

with MinecraftAPI(
        # everything by default
) as api:
    position = api.player.getPosition("Dev").wait()
    print(f"Player position: {position}")

    result = api.command.some_method("Lol")

    print(result)  # Error, cuz NYI
