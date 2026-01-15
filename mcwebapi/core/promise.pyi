"""Type stubs for Promise class.

This module provides type hints for the Promise class used for asynchronous operations.
"""

from typing import Any, Callable, Generic, List, Optional, TypeVar

T = TypeVar("T")

class Promise(Generic[T]):
    """Promise for handling asynchronous operations.

    Similar to JavaScript Promises, provides methods for handling
    asynchronous results and errors.

    Args:
        timeout: Maximum time to wait for result in seconds (default: 10.0)

    Example:
        >>> promise = player.getHealth()
        >>> promise.then(lambda health: print(f"Health: {health}"))
        >>> result = promise.wait()
    """

    _completed: bool
    _success: bool
    _result: Optional[T]
    _error: Optional[Exception]
    _callbacks: List[Callable[[T], Any]]
    _timeout: float

    def __init__(self, timeout: float = 10.0) -> None: ...

    def then(self, callback: Callable[[T], Any]) -> "Promise[T]":
        """Add callback to be executed when promise resolves.

        Args:
            callback: Function to call with result

        Returns:
            Self for chaining
        """
        ...

    def wait(self) -> T:
        """Wait synchronously for promise to complete.

        Returns:
            The result value

        Raises:
            Exception: If promise was rejected
            TimeoutError: If promise times out
        """
        ...

    def resolve(self, result: T) -> None:
        """Resolve promise with result.

        Args:
            result: Result value
        """
        ...

    def reject(self, error: Exception) -> None:
        """Reject promise with error.

        Args:
            error: Error exception
        """
        ...

    def is_completed(self) -> bool:
        """Check if promise is completed (resolved or rejected).

        Returns:
            True if completed
        """
        ...

    def is_successful(self) -> bool:
        """Check if promise resolved successfully.

        Returns:
            True if resolved successfully, False if rejected or not completed
        """
        ...
