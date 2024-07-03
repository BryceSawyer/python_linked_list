from node import Node
from typing import Any, Optional, Union

class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size: int = 0

    
    def head_node(self) -> Node:
        if self.is_empty():
            raise ValueError("Empty list")
        return self._head_node
    
    
    def tail_node(self) -> Node:
        if self.is_empty():
            raise ValueError("Empty list")
        elif self.size() == 1:
            return self.head_node()
        else:
            return self._tail_node


    def size(self) -> int:
        return self._size
    
    
    def is_empty(self) -> bool:
        return self._head_node is None
    
    
    def find_node(self, search: Union[Any, int]) -> Optional[Node]:
        if isinstance(search, int):  # Search by index
            if search < 0 or search >= self.size():
                raise IndexError("Index out of range")
            
            current_node = self.head_node()
            for _ in range(search):
                current_node = current_node.next_node()
            return current_node
        else:  # Search by data
            idx = 0
            current_node = self.head_node()
            while current_node:
                if current_node.data() == search:
                    return current_node.data(), idx
                current_node = current_node.next_node()
                idx += 1
            raise ValueError("No Data found")
        
        
    def find_nodes(self, target_idx):
        if target_idx < 0 or target_idx >= self.size():
            raise IndexError("Index out of range")
        
        prev_node = None
        target_node = self.head_node()
        next_node = self.head_node().next_node() if self.head_node() else None
        
        for _ in range(target_idx):
            prev_node = target_node
            target_node = target_node.next_node()
            next_node = target_node.next_node() if target_node else None

        return prev_node, target_node, next_node


    def prepend_node(self, data: Any) -> None:
        new_node = Node(data, self.head_node())
        self._head_node = new_node
        if self.is_empty():
            self._tail_node = new_node
        self._size += 1


    def insert_node_at_idx(self, data: Any, idx: int) -> None:
        if idx < 0 or idx > self.size():
            raise IndexError("Index out of range")
        
        if idx == 0:
            self.prepend_node(data)
        
        elif idx == self.size():
            self.append_node(data)

        else:
            prev_node = self.find_node(idx - 1)
            new_node = Node(data, prev_node.next_node)
            prev_node.next_node = new_node
            self._size += 1


    def append_node(self, data: Any) -> None:
        if self.is_empty():
            new_node = Node(data)
            self._head_node = new_node
            self._tail_node = new_node
        else:
            new_tail = Node(data)
            self._tail_node.set_next_node(new_tail)
            self._tail_node = new_tail
        self._size += 1
        

    def remove_head_node(self):
        if not self.is_empty():
            self._head_node = self._head_node.next_node()
            if not self._head_node:
                self._tail_node = None
            self._size -= 1
            

    def remove_node_at_idx(self, idx: int):
        if self.is_empty() or idx < 0 or idx >= self.size():
            raise IndexError("Index out of range")
        
        if idx == 0:
            self.remove_head_node()

        elif idx == self.size() - 1:
            self.remove_tail_node()

        else:
            prev_node, _, next_node = self.find_nodes(idx)
            prev_node.set_next_node(next_node)
            self._size -= 1

    
    def remove_node_by_data(self, data: Any):
        if not self.is_empty():
            node_to_remove = self.find_node(data)
            self.remove_node_at_idx(node_to_remove[1])
        return
    

    def remove_tail_node(self):
        if not self.is_empty():
            if self.size() == 1:
                self._head_node = None
                self._tail_node = None
            else:
                new_tail = self.find_node(self.size() -2)
                new_tail.set_next_node(None)
                self._tail_node = new_tail
            self._size -= 1


    def stringify_list(self) -> str:
        node = self._head_node
        result = []
        while node:
            result.append(str(node.data()))
            node = node.next_node()
        return " -> ".join(result)     


ll = LinkedList()
# ll.append_node(1)
# ll.append_node(2)
# ll.append_node(3)
# ll.append_node("this")
# ll.append_node(5)
# ll.remove_head_node()
# ll.prepend_node(6)
# ll.remove_tail_node()
# ll.remove_tail_node()
# ll.remove_tail_node()
# ll.remove_tail_node()
# ll.remove_head_node()

# print(ll.find_nodes(3))
# ll.remove_node_at_idx(0)
# ll.remove_node_at_idx(2)
# ll.remove_node_at_idx(1)
ll.remove_node_by_data("this")
ll.remove_node_by_data("this")


print(ll.stringify_list())
print("size", ll.size())
# print("head", ll.head_node().data())
# print("tail", ll.tail_node().data())
