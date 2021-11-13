from linked_list import Linked_List

class Doubly_Linked_List(Linked_List):
    """A doubly linked list data structure"""

    empty = ()

    def __init__(self, label, prev_node=empty, next_node=empty):
        self.prev = prev_node
        super().__init__(label, next_node)
    
    def forward_str(self):
        if self.next is Doubly_Linked_List.empty:
            return str(self.label)
        else:
            return f'{self.label} -> {self.next.forward_str()}'
    
    def backward_str(self):
        if self.prev is Doubly_Linked_List.empty:
            return str(self.label)
        else:
            return f'{self.prev.backward_str()} <- {self.label}'
    
    def __str__(self):
        string = str(self.label)
        if self.prev is not Doubly_Linked_List.empty:
            string = f'{self.prev.backward_str()} <- ' + string
        if self.next is not Doubly_Linked_List.empty:
            string = string + f' -> {self.next.forward_str()}'
        return string
    
    def __repr__(self):
        if self.prev is Doubly_Linked_List.empty and self.next is Doubly_Linked_List.empty:
            return f'Doubly_Linked_List({repr(self.label)})'
        elif self.next is Doubly_Linked_List.empty:
            return f'Doubly_Linked_List({repr(self.label)}, {repr(self.prev)})'
        elif self.prev is Doubly_Linked_List.empty:
            return f'Doubly_Linked_List({repr(self.label)}, next_node={repr(self.next)}'
        else:
            return f'Doubly_Linked_List({repr(self.label)}, {repr(self.prev)}, {repr(self.next)})'