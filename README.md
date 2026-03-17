# Kruskal's Algorithm for Minimum Spanning Tree (MST)

## Table of Contents
- [What the Code Does](#what-the-code-does)
- [Data Structure](#data-structure)
- [How the Code Works](#how-the-code-works)
- [Setup Instructions](#setup-instructions)
- [Program Usage Instructions](#program-usage-instructions)
- [Comparison with TSP Route](#comparison-with-tsp-route)
- [Known Limitations](#known-limitations)
- [Future Enhancements](#future-enhancements)
- [License and Copyright](#license-and-copyright)
- [Author Information and Acknowledgments](#author-information-and-acknowledgments)
- [Contact Information](#contact-information)
- [Useful Links](#useful-links)

## What the Code Does

This program implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) for the museum road network in Volyn region. The MST provides a baseline for evaluating the efficiency of the TSP route optimization by comparing total distances.

### Key Features
- Constructs minimum spanning tree connecting all museums
- Uses Union-Find (Disjoint Set) data structure for cycle detection
- Calculates theoretical minimum total distance to connect all museums
- Provides benchmark for TSP route evaluation
- Greedy approach ensuring optimal MST solution

### Workflow
```
Input: Museums + road distances between them
       ↓
Processing: Kruskal's Algorithm with Union-Find
       ↓
Output: MST edges + total minimum distance
```

### Purpose in Research

The MST serves as a **lower bound benchmark** for evaluating the TSP route:

**MST (Minimum Spanning Tree):**
- Connects all museums with minimum total distance
- Forms a tree (no cycles)
- Does NOT return to starting point
- Represents theoretical minimum to "reach" all museums

**TSP Route (Traveling Salesman):**
- Visits all museums and returns to start
- Forms a cycle (closed tour)
- Must be longer than MST
- Practical route for tourists

**Evaluation Metric:**
```
Efficiency Ratio = TSP Distance / MST Distance

Typical values:
- Good optimization: 1.3 - 1.5
- Average: 1.5 - 2.0
- Poor: > 2.0
```

## Data Structure

The program works with an edge list representing the road network between museums.

### Input Format

```
Number of vertices: N (museums)
Number of edges: M (road connections)

Edge format: weight vertex1 vertex2

Example:
61.8 Museum1 Museum3
59 Museum2 Museum3
60.6 Museum1 Museum5
```

Where:
- **Weight** = Distance in kilometers between museums
- **Vertex1, Vertex2** = Museum names or identifiers
- **Edges** = Direct road connections

### Graph Properties

- **Undirected Graph:** Roads are bidirectional
- **Weighted Graph:** Each edge has a distance value
- **Connected Graph:** All museums must be reachable
- **No Self-Loops:** Museums don't connect to themselves
- **No Parallel Edges:** Only one direct road between any two museums

## How the Code Works

### The Problem

Given all museums and road distances between them, find the minimum total distance needed to connect all museums with roads, without creating cycles.

### The Solution: Kruskal's Algorithm

Kruskal's algorithm builds the MST by repeatedly adding the shortest available edge that doesn't create a cycle.

---

### Algorithm Steps

**Step 1: Sort Edges**
```
Sort all roads by distance (shortest first)
Example:
32 km:  Museum2 - Museum6
52 km:  Museum2 - Museum7
59 km:  Museum2 - Museum3
60 km:  Museum3 - Museum7
...
```

**Step 2: Initialize Union-Find**
```
Each museum starts in its own group:
{Museum1}, {Museum2}, {Museum3}, ...
```

**Step 3: Process Edges Greedily**
```
For each edge (shortest to longest):
  If the two museums are in different groups:
    Add edge to MST
    Merge their groups
  Else:
    Skip (would create a cycle)
  
  Stop when we have N-1 edges (tree is complete)
```

**Visual Example:**

```
Initial state: 7 separate museums

Add edge 1 (32 km): Museum2 - Museum6
{Museum1}, {Museum2, Museum6}, {Museum3}, {Museum4}, {Museum5}, {Museum7}

Add edge 2 (52 km): Museum2 - Museum7
{Museum1}, {Museum2, Museum6, Museum7}, {Museum3}, {Museum4}, {Museum5}

Add edge 3 (59 km): Museum2 - Museum3
{Museum1}, {Museum2, Museum6, Museum7, Museum3}, {Museum4}, {Museum5}

Continue until all museums connected...
```

---

### Union-Find Data Structure

The program uses **Union-Find (Disjoint Set Union)** to efficiently detect cycles:

**Operations:**

1. **Find(vertex):** Determine which group a museum belongs to
   - Uses path compression for efficiency
   - Returns the "root" representative of the group

2. **Union(vertex1, vertex2):** Merge two groups
   - Connects their root representatives
   - Returns True if merge happened (different groups)
   - Returns False if already in same group (would create cycle)

**Example:**
```python
# Initially: each museum is its own root
connections = {
    "Museum1": "Museum1",
    "Museum2": "Museum2",
    ...
}

# After connecting Museum2 and Museum6:
connections = {
    "Museum1": "Museum1",
    "Museum2": "Museum2",
    "Museum6": "Museum2",  # Museum6 now points to Museum2
    ...
}
```

---

### Program Workflow Diagram

```
┌─────────────────────────────────────────────────────┐
│ 1. DATA INPUT                                       │
│    • Number of museums (vertices)                   │
│    • Number of roads (edges)                        │
│    • Edge list: weight vertex1 vertex2              │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 2. SORT EDGES                                       │
│    Sort all edges by weight (ascending)             │
│    Greedy approach: consider shortest roads first   │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 3. INITIALIZE UNION-FIND                            │
│    Create disjoint sets for each museum             │
│    Each museum starts in its own group              │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 4. KRUSKAL'S GREEDY SELECTION                       │
│    For each edge (shortest to longest):             │
│      • Check if vertices in different groups        │
│      • If yes: add to MST, merge groups             │
│      • If no: skip (would create cycle)             │
│      • Stop when tree complete (N-1 edges)          │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 5. OUTPUT RESULTS                                   │
│    • List of MST edges                              │
│    • Total weight (minimum distance)                │
│    • Benchmark for TSP evaluation                   │
└─────────────────────────────────────────────────────┘
```

## Setup Instructions

### Step 1: Installing Python

#### Windows
1. Download Python from the official website: https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"
5. Restart your computer

Verification:
```bash
python --version
```
Should display: `Python 3.x.x`

#### macOS
1. Open Terminal
2. Install Homebrew (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Install Python:
```bash
brew install python
```

Verification:
```bash
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verification:
```bash
python3 --version
```

### Step 2: Downloading the Program

**Option A: Via Git**
```bash
git clone https://github.com/4marchello/volyn-optimizer.git
cd volyn-optimizer
```

**Option B: Download ZIP**
1. Download the ZIP archive from GitHub
2. Extract to a convenient folder
3. Open the folder in terminal/command prompt

### Step 3: Running the Program

**Windows:**
```bash
python kruskal_mst.py
```

**macOS/Linux:**
```bash
python3 kruskal_mst.py
```

### Troubleshooting Installation

| Error | Cause | Solution |
|-------|-------|----------|
| "python is not recognized" | Python not added to PATH | Reinstall Python with "Add to PATH" checked |
| "Permission denied" | Insufficient permissions | Run `chmod +x kruskal_mst.py` |

## Program Usage Instructions

### Input Format

The program will prompt you for input in the following order:

**Step 1: Number of Vertices (Museums)**
```
Enter the number of vertex: 7
```

**Step 2: Number of Edges (Roads)**
```
Enter the number of edges: 12
```

**Step 3: Edge List**
```
Enter (weight vertex1 vertex2):
61.8 Museum1 Museum3
59 Museum2 Museum3
60.6 Museum1 Museum5
32 Museum2 Museum6
52 Museum2 Museum7
60 Museum3 Museum7
66 Museum3 Museum4
77 Museum4 Museum7
93 Museum3 Museum6
151.1 Museum4 Museum5
```

**Important:**
- Enter each edge on a new line
- Format: `weight vertex1 vertex2`
- Use spaces to separate values
- Vertex names can contain letters and numbers (no spaces)

### Example Session

```
Enter the number of vertex: 7
Enter the number of edges: 10
Enter (weight vertex1 vertex2):
32 M2 M6
52 M2 M7
59 M2 M3
60 M3 M7
60.6 M1 M5
61.8 M1 M3
66 M3 M4
77 M4 M7
93 M3 M6
151.1 M4 M5

MST:
M2 - M6
M2 - M7
M2 - M3
M1 - M5
M1 - M3
M3 - M4
Total distance: 331.4
```

### Understanding the Output

**MST Edges:**
- Lists the roads included in the minimum spanning tree
- Format: `vertex1 - vertex2`
- Each edge connects two museums

**Total Weight:**
- Sum of all edge weights in the MST
- Represents minimum total distance to connect all museums
- Measured in kilometers

### Interpreting Results

**What the MST tells you:**

1. **Minimum Connection Distance:** The theoretical minimum distance needed to connect all museums
2. **Critical Roads:** The roads in the MST are the most important for connectivity
3. **TSP Benchmark:** Compare TSP route distance to MST distance to evaluate efficiency

**Example Analysis:**
```
MST Total Distance: 331.4 km
TSP Route Distance: 423.5 km
Efficiency Ratio: 423.5 / 331.4 = 1.28

Interpretation: The TSP route is only 28% longer than the theoretical 
minimum, indicating good optimization.
```

## Comparison with TSP Route

### Why Compare MST and TSP?

The MST provides a **theoretical lower bound** for the TSP solution:

| Metric | MST | TSP Route |
|--------|-----|-----------|
| **Purpose** | Connect all museums | Visit all museums and return |
| **Structure** | Tree (no cycles) | Cycle (closed tour) |
| **Edges** | N-1 edges | N edges |
| **Starting Point** | Not specified | User-specified |
| **End Point** | Not specified | Returns to start |
| **Distance** | Minimum possible | Always ≥ MST |

### Evaluation Method

```
Step 1: Calculate MST distance (this program)
Step 2: Calculate TSP route distance (Dijkstra + Nearest Neighbor)
Step 3: Compute efficiency ratio

Efficiency Ratio = TSP Distance / MST Distance
```

### Quality Benchmarks

| Ratio | Quality | Interpretation |
|-------|---------|----------------|
| 1.0 - 1.3 | Excellent | Near-optimal solution |
| 1.3 - 1.5 | Good | Efficient route with minor improvements possible |
| 1.5 - 2.0 | Acceptable | Reasonable route, some optimization potential |
| > 2.0 | Poor | Significant optimization needed |

**Note:** For most TSP heuristics, ratios of 1.2-1.5 are typical and considered good results.

### Practical Example

**Museum Network: 7 museums in Volyn region**

```
MST (Minimum Spanning Tree):
- Total Distance: 331.4 km
- Connects all museums with minimum roads
- No return to start

TSP Route (Nearest Neighbor):
- Total Distance: 423.5 km
- Visits all museums and returns to start
- Practical tourist route

Efficiency Analysis:
- Ratio: 423.5 / 331.4 = 1.278
- Quality: Excellent (under 1.3)
- Interpretation: Only 27.8% overhead for completing the tour
```

## Known Limitations

1. **Manual Input:** Requires manual entry of all edges (no file import)
2. **No Visualization:** Text-only output without graphical tree display
3. **Console Interface:** Command-line only, no GUI
4. **Limited Error Handling:** Minimal validation of input format

## Future Enhancements

- File input support for loading edge data from CSV files
- Graphical visualization of the minimum spanning tree
- GUI interface for easier interaction
- Automated comparison tool with TSP route optimizer
- Export results to various formats (JSON, CSV, TXT)

## License and Copyright

### Code License

**MIT License**

Copyright (c) 2025 O.V. Bondaruk by LNTU

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

### Data Copyright

- **Distances between museums:** Obtained from Google Maps API
- **Coordinates:** Open data from regional authorities
- **Museum information:** Public domain data

### Program Usage

**ALLOWED:**

- Personal use
- Educational use
- Code modification
- Distribution with author attribution
- Commercial use (with author's permission)

**PROHIBITED:**

- Claiming as your own work without attribution
- Use for illegal purposes
- Selling without author's permission

### Attribution

When using the code or research results, please add a reference:

```
O.V. Bondaruk. (2025). Kruskal's Algorithm Implementation for Museum Network 
Analysis in Volyn Region. Lutsk National Technical University.
GitHub repository: https://github.com/4marchello/volyn-optimizer
```

## Author Information and Acknowledgments

### Lead Author

**Olena Bondaruk**  
Student PRM-11 course, Faculty of Architecture and Construction  
Lutsk National Technical University, Lutsk, Ukraine

**Contributions:**
- Algorithm implementation
- Software development (Python)
- Testing and validation
- Documentation writing
- Research analysis

### Scientific Supervisor

**Inga Viktorivna Samonenko**  
Associate Professor, Department of Applied Mathematics and Mechanics  
PhD in Statistics from University of Sydney, Australia  
Lutsk National Technical University (LNTU)

**Contributions:**
- Scientific supervision
- Methodological design
- Critical revision

## Contact Information

### Project Author

**Name:** Olena Bondaruk  
**Position:** Student, PRM-11 course  
**Faculty:** Architecture and Construction  
**University:** Lutsk National Technical University  
**City:** Lutsk, Ukraine  
**Email:** 790bondaruk@gmail.com

### Scientific Supervisor

**Name:** Inga Viktorivna Samonenko  
**Position:** Associate Professor, Department of Applied Mathematics and Mechanics  
**Degree:** PhD in Statistics, University of Sydney, Australia  
**Email:** i.samonenko@lntu.edu.ua

### Project Repository

**GitHub:** https://github.com/4marchello/volyn-route-optimizer

## Useful Links

- **Map of museums of Volyn region:** https://www.google.com/maps/d/u/0/edit?mid=1dSWIoi4filqKmLLW23MJxzTv7fm8068&ll=51.23900446473489%2C24.791629999999987&z=8
- **Museum network of Ukraine:** https://museum.mcsc.gov.ua/museums
- **Kruskal's Algorithm (Wikipedia):** https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
- **Minimum Spanning Tree:** https://en.wikipedia.org/wiki/Minimum_spanning_tree
- **Union-Find Data Structure:** https://en.wikipedia.org/wiki/Disjoint-set_data_structure
- **Official Python documentation:** https://docs.python.org/

---

**Last updated:** January 24, 2025
