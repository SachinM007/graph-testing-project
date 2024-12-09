import unittest
import hypothesis
import hypothesis.strategies as st
from hypothesis import given
from graph_library import Graph

class TestGraphLibrary(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
    
    def test_add_vertex(self):
        self.assertTrue(self.graph.add_vertex('A'))
        self.assertFalse(self.graph.add_vertex('A'))  # Duplicate vertex
    
    def test_add_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.assertTrue(self.graph.add_edge('A', 'B'))
        self.assertFalse(self.graph.add_edge('A', 'C'))  # Non-existent vertex
    
    def test_remove_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B')
        
        self.assertTrue(self.graph.remove_vertex('A'))
        self.assertFalse(self.graph.remove_vertex('A'))  # Already removed
    
    def test_dijkstra(self):
        self.graph = Graph(directed=False)
        vertices = ['A', 'B', 'C', 'D']
        for v in vertices:
            self.graph.add_vertex(v)
        
        edges = [
            ('A', 'B', 4.0),
            ('A', 'C', 2.0),
            ('B', 'D', 3.0),
            ('C', 'D', 1.0)
        ]
        
        for start, end, weight in edges:
            self.graph.add_edge(start, end, weight)
        
        distances = self.graph.dijkstra('A')
        self.assertAlmostEqual(distances['D'], 3.0)
    
    @given(st.lists(st.text(), unique=True))
    def test_add_multiple_vertices(self, vertices):
        """Property-based test for adding multiple vertices"""
        for v in vertices:
            self.graph.add_vertex(v)
        
        self.assertEqual(len(self.graph._vertices), len(vertices))
    
    @given(
        st.lists(st.text(min_size=1), min_size=2, unique=True),
        st.data()
    )
    def test_depth_first_search(self, vertices, data):
        """Property-based test for depth-first search"""
        for v in vertices:
            self.graph.add_vertex(v)
        
        # Randomly add some edges
        for _ in range(len(vertices) * 2):
            start = data.draw(st.sampled_from(vertices))
            end = data.draw(st.sampled_from(vertices))
            self.graph.add_edge(start, end)
        
        result = self.graph.depth_first_search(vertices[0])
        self.assertTrue(len(result) > 0)
        self.assertTrue(vertices[0] in result)

def mutation_test_intentional_bug(graph):
    """Simulate a bug in Dijkstra's algorithm"""
    def buggy_dijkstra(self, start, end=None):
        """Intentionally incorrect implementation"""
        return {}  # Always return empty dict
    
    graph.dijkstra = buggy_dijkstra.__get__(graph)
    return graph

if __name__ == '__main__':
    unittest.main()
