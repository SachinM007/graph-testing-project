class Vertex:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        self.neighbors = set()

    def add_neighbor(self, vertex):
        # Add the ID of the vertex to neighbors instead of the vertex object itself
        self.neighbors.add(vertex.id)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            print(f"Vertex '{vertex.id}' added.")
        else:
            print(f"Vertex '{vertex.id}' already exists.")

    def add_edge(self, vertex_id_1, vertex_id_2):
        if vertex_id_1 not in self.vertices or vertex_id_2 not in self.vertices:
            print(f"One or both vertices '{vertex_id_1}', '{vertex_id_2}' not found.")
            return
        
        vertex_1 = self.vertices[vertex_id_1]
        vertex_2 = self.vertices[vertex_id_2]
        vertex_1.add_neighbor(vertex_2)
        vertex_2.add_neighbor(vertex_1)
        print(f"Edge added between '{vertex_id_1}' and '{vertex_id_2}'.")

    def display_graph(self):
        for vertex_id, vertex in self.vertices.items():
            print(f"Vertex '{vertex_id}': Neighbors -> {', '.join(vertex.neighbors)}")
