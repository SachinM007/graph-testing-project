import typing
from typing import List, Dict, Set, Optional, Tuple
from dataclasses import dataclass, field

@dataclass
class Vertex:
    """Represents a vertex in the graph."""
    id: str
    data: typing.Any = None
    neighbors: Dict[str, float] = field(default_factory=dict)

class Graph:
    """A comprehensive graph data structure supporting multiple algorithms."""
    
    def __init__(self, directed: bool = False):
        """
        Initialize a graph.
        
        :param directed: Whether the graph is directed or undirected
        """
        self._vertices: Dict[str, Vertex] = {}
        self._directed = directed
    
    def add_vertex(self, vertex_id: str, data: typing.Any = None) -> bool:
        """
        Add a vertex to the graph.
        
        :param vertex_id: Unique identifier for the vertex
        :param data: Optional additional data for the vertex
        :return: Whether vertex was successfully added
        """
        if vertex_id in self._vertices:
            return False
        
        self._vertices[vertex_id] = Vertex(id=vertex_id, data=data)
        return True
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float = 1.0) -> bool:
        """
        Add an edge between two vertices.
        
        :param from_vertex: Source vertex ID
        :param to_vertex: Destination vertex ID
        :param weight: Edge weight
        :return: Whether edge was successfully added
        """
        if from_vertex not in self._vertices or to_vertex not in self._vertices:
            return False
        
        self._vertices[from_vertex].neighbors[to_vertex] = weight
        
        if not self._directed:
            self._vertices[to_vertex].neighbors[from_vertex] = weight
        
        return True
    
    def remove_vertex(self, vertex_id: str) -> bool:
        """
        Remove a vertex and all its associated edges.
        
        :param vertex_id: Vertex to remove
        :return: Whether vertex was successfully removed
        """
        if vertex_id not in self._vertices:
            return False
        
        # Remove edges pointing to this vertex
        for v in self._vertices.values():
            v.neighbors.pop(vertex_id, None)
        
        del self._vertices[vertex_id]
        return True
    
    def dijkstra(self, start: str, end: Optional[str] = None) -> Dict[str, float]:
        """
        Dijkstra's shortest path algorithm.
        
        :param start: Starting vertex
        :param end: Optional destination vertex
        :return: Distances from start vertex
        """
        if start not in self._vertices:
            return {}
        
        unvisited = {v: float('inf') for v in self._vertices}
        unvisited[start] = 0
        visited = {}
        
        while unvisited:
            current = min(unvisited, key=unvisited.get)
            current_distance = unvisited[current]
            
            if end and current == end:
                break
            
            for neighbor, weight in self._vertices[current].neighbors.items():
                if neighbor in visited:
                    continue
                
                new_distance = current_distance + weight
                if new_distance < unvisited.get(neighbor, float('inf')):
                    unvisited[neighbor] = new_distance
            
            visited[current] = current_distance
            del unvisited[current]
        
        return visited
    
    def depth_first_search(self, start: str) -> List[str]:
        """
        Depth-first search traversal.
        
        :param start: Starting vertex
        :return: List of visited vertices
        """
        if start not in self._vertices:
            return []
        
        visited = []
        stack = [start]
        seen = set()
        
        while stack:
            vertex = stack.pop()
            if vertex not in seen:
                visited.append(vertex)
                seen.add(vertex)
                
                # Add unvisited neighbors to stack
                for neighbor in reversed(list(self._vertices[vertex].neighbors.keys())):
                    if neighbor not in seen:
                        stack.append(neighbor)
        
        return visited
    
    def get_connected_components(self) -> List[List[str]]:
        """
        Find all connected components in the graph.
        
        :return: List of connected component vertex lists
        """
        unvisited = set(self._vertices.keys())
        components = []
        
        while unvisited:
            start = next(iter(unvisited))
            component = self.depth_first_search(start)
            components.append(component)
            unvisited -= set(component)
        
        return components
