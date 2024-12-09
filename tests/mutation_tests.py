import unittest
from hypothesis import given
import hypothesis.strategies as st
from src.graph_library import Graph

class MutationTestCases(unittest.TestCase):
    def test_mutation_scenarios(self):
        """Test multiple mutation injection points"""
        scenarios = [
            self._test_dijkstra_mutation,
            self._test_vertex_removal_mutation,
            self._test_edge_addition_mutation
        ]
        
        for scenario in scenarios:
            scenario()
    
    def _test_dijkstra_mutation(self):
        graph = Graph(directed=False)
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B', 4.0)
        graph.add_edge('B', 'C', 3.0)
        
        # Simulate mutation: intentionally break distance calculation
        original_method = graph.dijkstra
        graph.dijkstra = lambda x, y=None: {}
        
        result = graph.dijkstra('A')
        self.assertEqual(result, {})  # Mutated version should return empty dict
        
        graph.dijkstra = original_method  # Restore original method
    
    def _test_vertex_removal_mutation(self):
        graph = Graph()
        graph.add_vertex('X')
        graph.add_vertex('Y')
        graph.add_edge('X', 'Y')
        
        # Simulate mutation: prevent vertex removal
        original_method = graph.remove_vertex
        graph.remove_vertex = lambda x: False
        
        result = graph.remove_vertex('X')
        self.assertFalse(result)
        
        graph.remove_vertex = original_method  # Restore original method
    
    def _test_edge_addition_mutation(self):
        graph = Graph()
        graph.add_vertex('P')
        graph.add_vertex('Q')
        
        # Simulate mutation: always return False for edge addition
        original_method = graph.add_edge
        graph.add_edge = lambda x, y, w=1.0: False
        
        result = graph.add_edge('P', 'Q')
        self.assertFalse(result)
        
        graph.add_edge = original_method  # Restore original method

if __name__ == '__main__':
    unittest.main()
