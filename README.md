```markdown
# Graph Library Testing Project

## Overview
This project demonstrates a comprehensive testing approach for a Python graph library, showcasing advanced software testing techniques including unit testing, property-based testing, and mutation testing. The library is designed to solve common graph problems such as finding shortest paths, exploring connected components, and more.

## Example Usage
```python
from src.graph_library import Graph

# Create a directed graph
graph = Graph(directed=True)

# Add vertices and edges
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_edge('A', 'B', weight=3.5)

# Find shortest paths using Dijkstra's algorithm
distances = graph.dijkstra('A')
print("Shortest distances:", distances)

# Perform depth-first search
dfs_result = graph.depth_first_search('A')
print("DFS traversal:", dfs_result)
```

## Project Structure
```
graph-testing-project/
│
├── src/                # Source code
│   └── graph_library.py
├── tests/              # Test suite
│   ├── test_graph.py
│   └── mutation_tests.py
├── requirements.txt    # Project dependencies
```

## Features
- **Comprehensive Graph Library**
  - Directed and undirected graph support
  - Implements key graph algorithms:
    - Dijkstra's shortest path
    - Depth-first search (DFS)
    - Connected components detection
- **Advanced Testing Techniques**
  - Unit Testing
  - Property-based Testing
  - Mutation Testing
  - Code Coverage Analysis

## Prerequisites
- Python 3.8+
- pip package manager

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/graph-testing-project.git
   cd graph-testing-project
   ```

2. Create a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
### Unit Tests
Run all unit tests:
```bash
python -m unittest discover tests/
```

### Property-based Tests
Leverage Hypothesis for property-based testing:
```bash
pytest tests/test_graph.py
```

### Mutation Testing
Use `mutmut` to simulate bugs and evaluate test effectiveness:
```bash
mutmut run
```

### Code Coverage
Generate a coverage report:
```bash
coverage run -m unittest discover tests/
coverage report -m
```

## Testing Approaches
### Unit Testing
- Validates individual methods and components.
- Covers edge cases and expected behaviors.

### Property-based Testing
- Uses Hypothesis to generate test cases dynamically.
- Ensures robustness across varied graph scenarios.

### Mutation Testing
- Intentionally introduces bugs into the code.
- Validates the effectiveness of the test suite.
- Helps identify untested behaviors or edge cases.

## Performance Metrics
- **Test Coverage**: Aim for >80%.
- **Mutation Score**: Minimize undetected mutations to improve test reliability.

## Contact
**Sachin Miryala**  
📧 sm4335@nau.edu  
```
