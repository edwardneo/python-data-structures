class Node():
    """A node with a label and a list of edges"""

    def __init__(self, label):
        self.label = label
        self.edges = []
    
    def add_edge(self, edge):
        assert isinstance(edge, Edge)
        assert edge.node1 == self or edge.node2 == self, 'Edge does not contain node.'

        if edge not in self.edges:
            self.edges.append(edge)
    
    def __str__(self):
        return f'({self.label})'

    def __repr__(self):
        return f'Node({self.label})'

class Edge():
    """An edge connecting two nodes"""
    
    def __init__(self, node1, node2):
        assert isinstance(node1, Node) and isinstance(node2, Node), 'Arguments passed in are not nodes'

        self.node1 = node1
        self.node2 = node2
    
    def other_node(self, node):
        assert self.contains_node(node), 'Edge does not contain node.'

        return self.node2 if node == self.node1 else self.node1
    
    def contains_node(self, node):
        assert isinstance(node, Node), 'Argument passed in is not node'
        
        return node == self.node1 or node == self.node2
    
    def __str__(self):
        return f'{self.node1} -- {self.node2}'
    
    def __repr__(self):
        return f'Edge({repr(self.node1)}, {repr(self.node2)})'