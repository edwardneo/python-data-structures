from graph_elements import Node, Edge

class Graph():
    """A graph made up of nodes and edges"""

    def __init__(self, nodes, edges):
        assert all([isinstance(node, Node) for node in nodes]), 'Nodes argument is not list of nodes'
        assert all([isinstance(edge, Edge) for edge in edges]), 'Edges argument is not list of edges'

        for edge in edges:
            assert edge.node1 in nodes and edge.node2 in nodes, 'Nodes of edge is not in list of nodes'

        self.nodes = nodes
        self.edges = edges

        self.add_edges(self.edges)
    
    def add_node(self, node):
        assert isinstance(node, Node), 'Not a node'

        self.nodes.append(node)
    
    def add_edge(self, edge):
        assert isinstance(edge, Edge), 'Not an edge'
        assert edge.node1 in self.nodes and edge.node2 in self.nodes, 'Nodes of edge is not in list of nodes'

        self.edges.append(edge)
        edge.node1.add_edge(edge)
        edge.node2.add_edge(edge)
    
    def add_edges(self, edges):
        for edge in edges:
            assert edge.node1 in self.nodes and edge.node2 in self.nodes, 'Nodes of edge is not in list of nodes'

            edge.node1.add_edge(edge)
            edge.node2.add_edge(edge)
    
    def __str__(self):
        string_lst = []
        nodes_returned = []

        for edge in self.edges:
            string_lst.append(str(edge))
            nodes_returned.append(edge.node1)
            nodes_returned.append(edge.node2)

        for node in self.nodes:
            if node not in nodes_returned:
                string_lst.append(str(node))
        
        return '\n'.join(string_lst)
    
    def __repr__(self):
        nodes_string = '[' + ', '.join([repr(node) for node in self.nodes]) + ']'
        edges_string = '[' + ', '.join([repr(edge) for edge in self.edges]) + ']'
        return f'Graph({nodes_string}, {edges_string})'