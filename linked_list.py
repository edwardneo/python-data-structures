class Linked_List():
    """A linked list data structure"""

    empty = ()

    def __init__(self, label, next_node=empty):
        self.label = label
        self.next = next_node
    
    def __str__(self):
        if self.next is Linked_List.empty:
            return self.label
        else:
            return f'{self.label} -> {self.next}'
    
    def __repr__(self):
        if self.next is Linked_List.empty:
            return f'Linked_List({self.label})'
        else:
            return f'Linked_List({repr(self.label)}, {repr(self.next)})'
