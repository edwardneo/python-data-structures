from graph import Graph
from graph_elements import Edge

class Directed_Edge(Edge):
    def __str__(self):
        return f'{self.node1} --> {self.node2}'
    
    def __repr__(self):
        return f'Directed_Edge({repr(self.node1)}, {repr(self.node2)})'

class Directed_Graph(Graph):
    def add_edge(self, edge):
        assert self.is_edge(edge), 'Not an edge'
        assert edge.node1 in self.nodes, 'Nodes of edge is not in list of nodes'

        self.edges.append(edge)
        edge.node1.add_edge(edge)
    
    def is_edge(self, edge):
        return isinstance(edge, Directed_Edge)
    
    def __repr__(self):
        nodes_string = '[' + ', '.join([repr(node) for node in self.nodes]) + ']'
        edges_string = '[' + ', '.join([repr(edge) for edge in self.edges]) + ']'
        return f'Directed_Graph({nodes_string}, {edges_string})'