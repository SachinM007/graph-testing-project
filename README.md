# Graph Library Testing Project

## Overview
This project demonstrates a comprehensive testing approach for a Python graph library, showcasing advanced software testing techniques including unit testing, property-based testing, and mutation testing.

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
└── .github/            # CI/CD workflow
    └── workflows/
        └── python-tests.yml
```

## Features
- Comprehensive Graph Library
  - Supports directed and undirected graphs
  - Implements key graph algorithms
    - Dijkstra's shortest path
    - Depth-first search
    - Connected components detection

- Advanced Testing Techniques
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

2. Create virtual environment
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
```bash
python -m unittest discover tests/
```

### Property-based Tests
```bash
pytest tests/test_graph.py
```

### Mutation Testing
```bash
mutmut run
```

### Code Coverage
```bash
coverage run -m unittest discover tests/
coverage report -m
```

## Testing Approaches
### Unit Testing
- Validates individual methods and components
- Checks edge cases and expected behaviors

### Property-based Testing
- Uses Hypothesis to generate test cases
- Validates graph operations across multiple scenarios
- Discovers unexpected behaviors

### Mutation Testing
- Intentionally introduces bugs
- Validates test suite's effectiveness
- Identifies potential weaknesses in testing

## Performance Metrics
- Test Coverage: Aim for >80%
- Mutation Score: Minimize undetected mutations

## Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request


## Contact
Sachin Miryala
sm4335@nau.edu
```
