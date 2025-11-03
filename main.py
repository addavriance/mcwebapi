# Example
from mcwebapi import MinecraftAPI

if __name__ == "__main__":
    api = MinecraftAPI()

    api.connect()

    player = api.Player("Dev")

    player.getX().then(print)
    player.getY().then(print)
    player.getZ().then(print)

    api.wait_for_pending()
    api.disconnect()
