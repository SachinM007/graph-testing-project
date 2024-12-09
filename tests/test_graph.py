import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from graph_library import Graph, Vertex  # Your imports should work now
import unittest
from hypothesis import given
import hypothesis.strategies as st


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_vertex(self):
        vertex = Vertex("A")
        self.graph.add_vertex(vertex)
        self.assertIn("A", self.graph.vertices)

    def test_add_edge(self):
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        self.graph.add_vertex(vertex_a)
        self.graph.add_vertex(vertex_b)
        self.graph.add_edge("A", "B")
        self.assertIn("B", self.graph.vertices["A"].neighbors)
        self.assertIn("A", self.graph.vertices["B"].neighbors)

    def test_add_edge_with_missing_vertex(self):
        vertex_a = Vertex("A")
        self.graph.add_vertex(vertex_a)
        self.graph.add_edge("A", "B")
        self.assertNotIn("B", self.graph.vertices)
        self.assertEqual(self.graph.vertices["A"].neighbors, set())

    def test_duplicate_edge(self):
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        self.graph.add_vertex(vertex_a)
        self.graph.add_vertex(vertex_b)
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "B")  # Adding the same edge again
        self.assertEqual(len(self.graph.vertices["A"].neighbors), 1)  # Only one neighbor should be added

    def test_display_graph(self):
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        self.graph.add_vertex(vertex_a)
        self.graph.add_vertex(vertex_b)
        self.graph.add_edge("A", "B")
        self.graph.display_graph()

if __name__ == "__main__":
    unittest.main()
