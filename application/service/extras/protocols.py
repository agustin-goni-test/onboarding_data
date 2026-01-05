from typing import Protocol, Iterable

class CodeNameItem(Protocol):
    code: int
    name: str
