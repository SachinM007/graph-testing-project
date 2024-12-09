import unittest
from hypothesis import given
import hypothesis.strategies as st
from src.graph_library import Graph

class MutationTestCases(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_mutation_scenarios(self):
        """Test multiple mutation injection points"""
        scenarios = [
            self._test_dijkstra_mutation,
            self._test_vertex_removal_mutation,
            self._test_edge_addition_mutation
        ]
        
        for scenario in scenarios:
            scenario()

    def _simulate_mutation(self, graph, method_name, mutation):
        """Helper function to simulate and restore method mutation"""
        original_method = getattr(graph, method_name)
        setattr(graph, method_name, mutation)
        try:
            yield
        finally:
            setattr(graph, method_name, original_method)
    
    def _test_dijkstra_mutation(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge('A', 'B', 4.0)
        self.graph.add_edge('B', 'C', 3.0)
        
        # Simulate mutation: intentionally break distance calculation
        with self._simulate_mutation(
            self.graph, 'dijkstra', lambda x, y=None: {}
        ):
            result = self.graph.dijkstra('A')
            self.assertEqual(result, {})  # Mutated version should return empty dict
    
    def _test_vertex_removal_mutation(self):
        self.graph.add_vertex('X')
        self.graph.add_vertex('Y')
        self.graph.add_edge('X', 'Y')
        
        # Simulate mutation: prevent vertex removal
        with self._simulate_mutation(
            self.graph, 'remove_vertex', lambda x: False
        ):
            result = self.graph.remove_vertex('X')
            self.assertFalse(result)
    
    def _test_edge_addition_mutation(self):
        self.graph.add_vertex('P')
        self.graph.add_vertex('Q')
        
        # Simulate mutation: always return False for edge addition
        with self._simulate_mutation(
            self.graph, 'add_edge', lambda x, y, w=1.0: False
        ):
            result = self.graph.add_edge('P', 'Q')
            self.assertFalse(result)

    @given(st.lists(st.text(min_size=1), unique=True), st.data())
    def test_property_based_mutation(self, vertices, data):
        """Property-based testing with mutations"""
        for v in vertices:
            self.graph.add_vertex(v)
        
        # Dynamically add edges
        for _ in range(len(vertices) * 2):
            start = data.draw(st.sampled_from(vertices))
            end = data.draw(st.sampled_from(vertices))
            self.graph.add_edge(start, end)
        
        # Simulate mutation in DFS
        with self._simulate_mutation(
            self.graph, 'depth_first_search', lambda x: []
        ):
            dfs_result = self.graph.depth_first_search(vertices[0])
            self.assertEqual(dfs_result, [])  # Ensure the mutation affects DFS

if __name__ == '__main__':
    unittest.main()
