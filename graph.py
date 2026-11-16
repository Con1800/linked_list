class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""
        for node, neighbors in self.adj_list:
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists already")

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