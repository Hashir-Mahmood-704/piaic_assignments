from typing import Callable


def decorator(function: Callable[[str], None]) -> Callable[[str], None]:
    def wrapper(message: str) -> None:
        modifiedMessage = "👻 " * 6
        modifiedMessage = modifiedMessage + message
        modifiedMessage = modifiedMessage + (" 👻" * 6)
        function(modifiedMessage)

    return wrapper


def decorator2(function: Callable[[str], None]) -> Callable[[str], None]:
    def wrapper(message: str) -> None:
        modifiedMessage = "👁️  " * (len(message) // 2)
        modifiedMessage = modifiedMessage + "\n" + message + "\n" + modifiedMessage
        function(modifiedMessage)

    return wrapper
