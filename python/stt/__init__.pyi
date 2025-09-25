from typing import Any, Generator, TypeAlias, Union
from types import GenericAlias


__all__ = [
    "dump",
    "dump_iterable",
    "Tree",
    "STTError",
]


class STTError(Exception):
    ...


Tree: TypeAlias = Node | GenericAlias | tuple[Tree, ...] | ellipsis | None
Node: TypeAlias =  Any | GenericAlias | tuple[Node, ...] | ellipsis


def dump(tree: Tree) -> None: ...
def dump_iterable(tree: Tree) -> Generator[Node]: ...