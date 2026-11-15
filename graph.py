class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, from_node, to_node, weight=None):
        pass

    def remove(self, from_node, to_node):
        pass

    def get_neighbors(self, node):
        pass

    def has_node(self, node):
        pass

    def has_edge(self, from_node, to_node):
        pass

    def get_nodes(self):
        pass

    def get_egdes(self):
        pass

    def bfs(self, start):
        pass

    def dfs(self, start):
        pass