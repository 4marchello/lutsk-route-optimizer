# Tourist Route Optimization Program "Lutsk Klikuns"

## 📋 Table of Contents

- [What the Code Does](#what-the-code-does)
- [Data Files](#data-files)
- [How the Code Works](#how-the-code-works)
- [Setup Instructions](#setup-instructions)
- [Program Usage Instructions](#program-usage-instructions)
- [License and Copyright](#license-and-copyright)
- [Contact Information](#contact-information)
- [Known Bugs](#known-bugs)
- [Author Information and Acknowledgments](#author-information-and-acknowledgments)

## What the Code Does

This program automatically builds the **shortest pedestrian route** for visiting all 21 historical sculptures "Lutsk Klikuns" in the city of Lutsk, Ukraine.

### Key Features

- Calculation of optimal route between 21 sculptures
- Minimization of total distance (from 18 km to 11.5 km)
- Graphical interface for ease of use
- Ability to choose starting point
- Output of detailed route with distance

### Workflow

```
Input: 21 sculptures + starting point
       ↓
Processing: Optimization algorithms
       ↓
Output: Optimal route 11.5 km
```
## Data Files

The repository includes an Excel file **`Table_for_the_graph_Lutsk_Klikuns___.xlsx`** containing two important data sheets:

### 1. Distance Matrix

A 21×21 symmetric matrix containing pedestrian walking distances (in meters) between all pairs of sculptures. The distances were measured using Google Maps API along actual pedestrian paths.

**Structure:**
- **Rows/Columns:** Each sculpture (A1 through U21)
- **Values:** Distance in meters between sculpture pairs
- **Coordinates:** GPS coordinates for each sculpture location

**Example:**
```
        A1    B2    C3    D4    ...
A1      0     2850  3260  4390  ...
B2      2850  0     1010  2080  ...
C3      3260  1010  0     1150  ...
...
```

This matrix represents a **complete weighted graph** where:
- Vertices = sculptures
- Edges = pedestrian paths
- Weights = distances in meters

### 2. Laplacian Matrix

The **Laplacian matrix** (also called admittance matrix or Kirchhoff matrix) is a fundamental matrix representation in graph theory used for analyzing graph properties.

**Mathematical definition:**
```
L = D - A
```

Where:
- **L** = Laplacian matrix
- **D** = Degree matrix (diagonal matrix with vertex degrees)
- **A** = Adjacency matrix (connections between vertices)

**For our complete graph:**
```
L[i,i] = 20     (degree of each vertex, since connected to all other 20 vertices)
L[i,j] = -1     (for i ≠ j, indicating connection between vertices)
```

**Example:**
```
      A1   B2   C3   D4   ...
A1    20   -1   -1   -1   ...
B2    -1   20   -1   -1   ...
C3    -1   -1   20   -1   ...
...
```

**Applications of Laplacian Matrix:**
- **Spectral graph theory:** Eigenvalues reveal graph connectivity
- **Network analysis:** Studying information flow through the graph
- **Community detection:** Identifying clusters in the graph
- **Random walks:** Analyzing probabilistic path selection
- **Graph partitioning:** Dividing the graph into subgraphs

**Important properties:**
1. Symmetric matrix (L = Lᵀ)
2. Row and column sums equal zero
3. Smallest eigenvalue is always 0
4. Number of zero eigenvalues = number of connected components

For our complete graph with 21 vertices, the Laplacian matrix helps verify that all sculptures are interconnected and validates the completeness of our distance data.

## How the Code Works

### The Problem

A tourist wants to visit all 21 sculptures but doesn't know the most efficient order. Random search can lead to walking 15-18 km with many unnecessary "zigzags".

### The Solution

The program uses two algorithms sequentially:

#### Step 1: Greedy Algorithm

**What it does:**
- Starts from the starting point (e.g., A1)
- At each step, goes to the nearest unvisited sculpture
- Continues until all 21 points are visited

**Analogy:**  
Like a tourist who always chooses the nearest store until buying everything on the shopping list.

**Result:**  
Fast route (1 second computation), but not ideal - there may be "zigzags".

#### Step 2: 2-opt Optimization

**What it does:**
- Takes the route from Step 1
- Looks for places where the path crosses or makes unnecessary loops
- Fixes these places, making the route shorter

**Analogy:**  
Like untangling a rope - if there's a crossing or knot, we untangle it to make the rope straighter.

**Visual representation:**

```
BEFORE (zigzag):        AFTER (straighter):
  A                        A
   \                        \
    B--D                     B
   /    \                     \
  C      E                     C
                                \
                                 D--E
```

**Result:**  
Route without unnecessary loops, length decreases by 10-15%.

### Program Workflow Diagram

```
┌─────────────────────────────────────────────────────┐
│ 1. DATA INPUT                                       │
│    • 21 sculptures                                  │
│    • 210 distances between them (in meters)         │
│    • Starting point (A1)                            │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 2. GRAPH CONSTRUCTION                               │
│    Function: rozbir()                               │
│    Creates structure: vertices + edges with weights │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 3. GREEDY ALGORITHM                                 │
│    Function: greedystart()                          │
│    Builds initial route (~13 km)                    │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 4. 2-OPT OPTIMIZATION                               │
│    Function: pokrashchty()                          │
│    Removes zigzags and crossings (~11.5 km)         │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│ 5. RESULT OUTPUT                                    │
│    • Visit sequence                                 │
│    • Total distance                                 │
│    • Walking time (~3 hours)                        │
└─────────────────────────────────────────────────────┘
```

## Setup Instructions

### Step 1: Installing Python

#### Windows

1. Download Python from the official website: https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT:** Check "Add Python to PATH"
4. **IMPORTANT:** Check "tcl/tk and IDLE" (required for GUI)
5. Click "Install Now"
6. Restart your computer

**Verification:**
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
brew install python-tk
```

**Verification:**
```bash
python3 --version
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-tk
```

**Verification:**
```bash
python3 --version
```

### Step 2: Downloading the Program

#### Option A: Via Git

```bash
git clone https://github.com/4marchello/lutsk-route-optimizer.git
cd lutsk-route-optimizer
```

#### Option B: Download ZIP

1. Download the ZIP archive from GitHub
2. Extract to a convenient folder
3. Open the folder in terminal/command prompt

### Step 3: Running the Program

#### Windows

```bash
python route_optimizer.py
```

#### macOS/Linux

```bash
python3 route_optimizer.py
```

**Successful launch:**  
A window with a graphical interface should open.

### Troubleshooting Installation

**Error: "python is not recognized"**
- **Cause:** Python not added to PATH
- **Solution:** Reinstall Python with "Add to PATH" checked, or add manually to environment variables

**Error: "No module named tkinter"**
- **Cause:** Tkinter not installed
- **Solution:**
  - Ubuntu/Debian: `sudo apt install python3-tk`
  - macOS: `brew install python-tk`

**Error: "Permission denied"**
- **Cause:** Insufficient permissions
- **Solution:** `chmod +x route_optimizer.py`

## Program Usage Instructions

### Program Interface

```
┌────────────────────────────────────────────────────┐
│ Route Search (2-opt optimization)      [_][□][×]   │
├────────────────────────────────────────────────────┤
│                                                    │
│ Edges (A B 10):                                    │
│ ┌────────────────────────────────────────────────┐ │
│ │ A1 B2 2850                                     │ │
│ │ A1 C3 3260                                     │ │
│ │ B2 C3 1010                                     │ │
│ │ ... (210 lines)                                │ │
│ └────────────────────────────────────────────────┘ │
│                                                    │
│ Start: [A1      ]                                  │
│                                                    │
│            [ Calculate ]                           │
│                                                    │
│ Result:                                            │
│ ┌────────────────────────────────────────────────┐ │
│ │ Route (Optimized):                             │ │
│ │ A1 → B2 → C3 → D4 → E5 → ...                   │ │
│ │                                                │ │
│ │ Total weight: 11503.0                          │ │
│ └────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────┘
```

### Step-by-Step Instructions

#### Step 1: Data Input (optional)

By default, the program already contains all 210 distances between sculptures.

**Format:** `Vertex1 Vertex2 Distance_in_meters`

**Example:**
```
A1 B2 2850
A1 C3 3260
B2 C3 1010
```

**When to modify:**
- Adding new sculptures
- Changes in pedestrian paths (repairs, new roads)
- Testing on custom data

#### Step 2: Choosing Starting Point

In the "Start" field, specify the sculpture code from which you'll begin.

**Available codes:**

| Code | Sculpture Name | 
|------|----------------|
| A1 | Radyk Zadovolenyi |
| B2 | Zustrichayko |
| C3 | Hnat |
| D4 | Vasyl "Soloveiko" |
| E5 | Franyo |
| F6 | Khvatsko i Prudko |
| G7 | Knyzhko |
| H8 | Semen Hust |
| I9 | Zirko |
| J10 | Trilinko |
| K11 | Muzyka |
| L12 | Vertun |
| M13 | Vartko i Vartko |
| N14 | Klikun Andriy |
| O15 | Stepan |
| P16 | Kavus |
| Q17 | Kliuchnyk |
| R18 | Providnyk |
| S19 | Bratko i Bratko |
| T20 | Vohnar |
| U21 | Mykytovych |

**How to change:**
1. Click on the "Start" field
2. Delete the old value
3. Enter new code (e.g., `G7`)

#### Step 3: Route Calculation

1. Click the **"Calculate"** button
2. Wait 2-5 seconds (depends on computer speed)
3. Result will appear in the "Result" field

**What the result shows:**

```
Route (Optimized):
A1 → B2 → C3 → D4 → E5 → F6 → L12 → N14 → 
M13 → O15 → T20 → U21 → S19 → R18 → Q17 → 
P16 → K11 → J10 → I9 → G7 → H8

Total weight: 11503.0
```

**Explanation:**
- Arrows (→) show the visiting order
- Total weight = total distance in meters (11503 m = 11.5 km)

#### Step 4: Saving Results

**Option 1: Copy text**
1. Select text in the "Result" field
2. Press `Ctrl+C` (Windows/Linux) or `Cmd+C` (macOS)
3. Paste into any text editor

**Option 2: Screenshot**
- Windows: `Win + Shift + S`
- macOS: `Cmd + Shift + 4`
- Linux: `Print Screen`

### Error Messages

| Error Message | Cause | Solution |
|--------------|-------|----------|
| "Specify start" | "Start" field is empty | Enter sculpture code (A1, B2, etc.) |
| "Start A1 is missing" | Specified sculpture not found | Check code correctness (capital letters!) |
| "Graph is empty" | No distance data | Insert data in "Edges" field |
| "Graph is disconnected" | Not all sculptures connected | Add missing edges or remove isolated vertices |

## License and Copyright

### Code License

**MIT License**

Copyright (c) 2025 A. S. Osadchyi, M. S. Vavdiiuk by LNTU

Permission is hereby granted, free of charge, to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, provided that the above copyright notice is preserved.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.**

### Data Copyright

- **Distances between sculptures:** Obtained from Google Maps API
- **Coordinates:** Open data from Lutsk City Council
- **Sculpture names:** "Lutsk Klikuns" project, Lutsk City Council

### Program Usage

**ALLOWED:**
- ✅ Personal use
- ✅ Educational use
- ✅ Code modification
- ✅ Distribution with author attribution
- ✅ Commercial use (with author's permission)

**PROHIBITED:**
- ❌ Claiming as your own work without attribution
- ❌ Use for illegal purposes
- ❌ Selling without author's permission

### Attribution

When using the code or research results, please add a reference:

```
A. S. Osadchyi, M. S. Vavdiiuk. (2025). Optimization of Pedestrian Tourist 
Routes Using Graph Theory Algorithms: A Case Study of "Lutsk Klikuns". 
GitHub repository: https://github.com/4marchello/lutsk-route-optimizer
```

## Contact Information

### Project Authors

**Names:** Marko Vavdiiuk, Arsen Osadchyi  
**Position:** Students, PRM-11 course  
**Faculty:** Architecture and Construction  
**University:** Lutsk National Technical University  
**City:** Lutsk, Ukraine

### Contact Authors

**Email:** markoo.vavdiyuk@gmail.com / jdtaaa000@gmail.com

### Scientific Supervisor

**Name:** Inga Viktorivna Samonenko  
**Position:** Associate Professor, Department of Applied Mathematics and Mechanics  
**Degree:** PhD in Statistics, University of Sydney, Australia  
**Email:** i.samonenko@lntu.edu.ua

### Project Repository

**GitHub:** https://github.com/4marchello/lutsk-route-optimizer

## Known Bugs

Currently no critical bugs reported.

### Known Limitations

1. **Maximum 50 vertices:** For larger numbers, computation time grows exponentially

2. **Complete graph only:** If there's no path between two sculptures, route will be incomplete

3. **No elevation consideration:** Program doesn't account for ascents/descents (only horizontal distance)

4. **No GPX export:** Result cannot be loaded into GPS navigator (planned in v2.0)

## Author Information and Acknowledgments

### Lead Authors

**Marko Vavdiiuk**  
Student PRM-11 course, Faculty of Architecture and Construction  
Lutsk National Technical University, Lutsk, Ukraine

**Arsen Osadchyi**  
Student PRM-11 course, Faculty of Architecture and Construction  
Lutsk National Technical University, Lutsk, Ukraine

**Contributions:**
- Development of optimization algorithms
- Software implementation (Python)
- Collection of distance data
- Testing and debugging
- Documentation writing

### Scientific Supervisor

**Inga Viktorivna Samonenko**  
Associate Professor, Department of Applied Mathematics and Mechanics  
PhD in Statistics from University of Sydney, Australia  
Lutsk National Technical University (LNTU)

**Contributions:**
- Scientific consulting
- Methodology selection
- Work review

## Disclaimer

This program is provided "as is" without any warranties. The authors are not responsible for:
- Inaccuracies in distance data
- Changes in city infrastructure
- Closure of access to certain locations
- Physical injuries during route navigation
- Data loss or equipment damage

### Recommendations

- Always verify route relevance before departure
- Consider weather conditions and time of day
- Wear comfortable shoes and clothing
- Carry water and snacks
- Inform loved ones about your route


### Useful Links

- **Official "Lutsk Klikuns" project website:** https://www.lutskrada.gov.ua/pages/lutski-klykuny
- **Interactive map of Lutsk:** https://www.google.com/maps

**Last updated:** January 17, 2025

**Glory to Ukraine!** 🇺🇦
