import heapq


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    # Display graph
    def __repr__(self):
        graph_str = ""

        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"

        return graph_str

    # Add node
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists already")

    # Remove node
    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node does not exist")

        for neighbors in self.adj_list.values():
            to_remove = set()

            for neighbor in neighbors:
                neighbor_node = (
                    neighbor[0] if isinstance(neighbor, tuple)
                    else neighbor
                )

                if neighbor_node == node:
                    to_remove.add(neighbor)

            neighbors.difference_update(to_remove)

        del self.adj_list[node]

    # Add edge
    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        edge = to_node if weight is None else (to_node, weight)
        self.adj_list[from_node].add(edge)

        if not self.directed:
            reverse_edge = (
                from_node if weight is None
                else (from_node, weight)
            )

            self.adj_list[to_node].add(reverse_edge)

    # Remove edge
    def remove_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            raise ValueError("Edge does not exist")

        neighbors = self.adj_list[from_node]

        edge = next(
            (n for n in neighbors
             if (n[0] if isinstance(n, tuple) else n) == to_node),
            None
        )

        if edge is None:
            raise ValueError("Edge does not exist")

        neighbors.remove(edge)

        if not self.directed:
            reverse_neighbors = self.adj_list[to_node]

            reverse_edge = next(
                (n for n in reverse_neighbors
                 if (n[0] if isinstance(n, tuple) else n) == from_node),
                None
            )

            if reverse_edge is not None:
                reverse_neighbors.remove(reverse_edge)

    # Get neighbors
    def get_neighbors(self, node):
        return self.adj_list.get(node, set())

    # Check node
    def has_node(self, node):
        return node in self.adj_list

    # Check edge
    def has_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            return False

        for neighbor in self.adj_list[from_node]:
            neighbor_node = (
                neighbor[0] if isinstance(neighbor, tuple)
                else neighbor
            )

            if neighbor_node == to_node:
                return True

        return False

    # Get all nodes
    def get_nodes(self):
        return list(self.adj_list.keys())

    # Get all edges
    def get_edges(self):
        edges = []

        for from_node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to_node, weight = neighbor
                    edges.append((from_node, to_node, weight))
                else:
                    edges.append((from_node, neighbor))

        return edges

    # Breadth First Search
    def bfs(self, start):
        if start not in self.adj_list:
            raise ValueError("Starting node does not exist")

        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                for neighbor in self.get_neighbors(node):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]

                    if neighbor not in visited:
                        queue.append(neighbor)

        return order

    # Depth First Search
    def dfs(self, start):
        if start not in self.adj_list:
            raise ValueError("Starting node does not exist")

        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbors = self.get_neighbors(node)

                neighbor_nodes = [
                    n[0] if isinstance(n, tuple) else n
                    for n in neighbors
                ]

                for neighbor in sorted(neighbor_nodes, reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order

    # Dijkstra's Algorithm
    def dijkstra(self, start):
        if start not in self.adj_list:
            raise ValueError("Starting node does not exist")

        distances = {
            node: float('inf')
            for node in self.adj_list
        }

        previous = {
            node: None
            for node in self.adj_list
        }

        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(
                priority_queue
            )

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.get_neighbors(current_node):

                if isinstance(neighbor, tuple):
                    neighbor_node, weight = neighbor
                else:
                    neighbor_node = neighbor
                    weight = 1

                if weight < 0:
                    raise ValueError(
                        "Dijkstra does not support negative weights"
                    )

                distance = current_distance + weight

                if distance < distances[neighbor_node]:
                    distances[neighbor_node] = distance
                    previous[neighbor_node] = current_node

                    heapq.heappush(
                        priority_queue,
                        (distance, neighbor_node)
                    )

        return distances, previous

    # Find shortest path between two nodes
    def shortest_path(self, start, end):
        distances, previous = self.dijkstra(start)

        if end not in self.adj_list:
            raise ValueError("Destination node does not exist")

        if distances[end] == float('inf'):
            return [], float('inf')

        path = []
        current_node = end

        while current_node is not None:
            path.append(current_node)
            current_node = previous[current_node]

        path.reverse()

        return path, distances[end]


# =================================
# TESTING
# =================================

graph = Graph(directed=False)

graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 10)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 4)
graph.add_edge("C", "D", 1)

print("GRAPH:")
print(graph)

print("NODES:")
print(graph.get_nodes())

print("EDGES:")
print(graph.get_edges())

print("BFS:")
print(graph.bfs("A"))

print("DFS:")
print(graph.dfs("A"))

print("DIJKSTRA:")
distances, previous = graph.dijkstra("A")
print(distances)

print("SHORTEST PATH:")
path, distance = graph.shortest_path("A", "D")
print("Path:", path)
print("Distance:", distance)
