from typing import Any, Tuple, Dict

from ..api import MinecraftClient


class SocketInstance:
    """Base class for all API entities"""

    def __init__(self, name: str, client: MinecraftClient):
        self.module_name = name
        self._client = client

    def __getattr__(self, name: str) -> callable:
        def server_method(*args: Any, **kwargs: Any) -> Any:
            final_args = self._process_args(args, kwargs)
            return self._client.send_request(
                module=self.module_name,
                method=name,
                args=final_args
            )

        return server_method

    def _process_args(self, args: Tuple, kwargs: Dict) -> list:
        if not kwargs:
            return list(args)
        return list(args) + list(kwargs.values())