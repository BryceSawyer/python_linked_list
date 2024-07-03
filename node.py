from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next_node: Optional["Node"] = None):
        self._data = data
        self._next_node = next_node
    
    def data(self) -> Any:
        return self._data
    
    def set_data(self, data: Any) -> None:
        self._data = data

    def next_node(self) -> Optional["Node"]:
        return self._next_node
    
    def set_next_node(self, next_node: Optional["Node"]) -> None:
        self._next_node = next_node