================================================================================
  TOURIST ROUTE OPTIMIZATION PROGRAM "LUTSK KLIKUNS"
================================================================================

TABLE OF CONTENTS
-----------------
1. What the Code Does
2. How the Code Works (Operating Principle)
3. Setup Instructions
4. Program Usage Instructions
5. License and Copyright
6. Contact Information
7. Known Bugs
8. Author Information and Acknowledgments

================================================================================
1. WHAT THE CODE DOES
================================================================================

This program automatically builds the shortest pedestrian route for visiting 
all 21 historical sculptures "Lutsk Klikuns" in the city of Lutsk.

KEY FEATURES:
- Calculation of optimal route between 21 sculptures
- Minimization of total distance (from 18 km to 11.5 km)
- Graphical interface for ease of use
- Ability to choose starting point
- Output of detailed route with distance

WORKFLOW:

Input: 21 sculptures + starting point
       |
       v
Processing: Optimization algorithms
       |
       v
Output: Optimal route 11.5 km

================================================================================
2. HOW THE CODE WORKS (OPERATING PRINCIPLE)
================================================================================

THE PROBLEM
-----------
A tourist wants to visit all 21 sculptures but doesn't know the most efficient 
order. Random search can lead to walking 15-18 km with many unnecessary 
"zigzags".

THE SOLUTION
------------
The program uses two algorithms sequentially:

STEP 1: GREEDY ALGORITHM

What it does:
- Starts from the starting point (e.g., A1)
- At each step, goes to the nearest unvisited sculpture
- Continues until all 21 points are visited

Analogy:
Like a tourist who always chooses the nearest store until buying everything 
on the shopping list.

Result:
Fast route (1 second computation), but not ideal - there may be "zigzags".

--------------------------------------------------------------------------------

STEP 2: 2-OPT OPTIMIZATION

What it does:
- Takes the route from Step 1
- Looks for places where the path crosses or makes unnecessary loops
- Fixes these places, making the route shorter

Analogy:
Like untangling a rope - if there's a crossing or knot, we untangle it to 
make the rope straighter.

Visually:

BEFORE (zigzag):        AFTER (straighter):
  A                        A
   \                        \
    B--D                     B
   /    \                     \
  C      E                     C
                                \
                                 D--E

Result:
Route without unnecessary loops, length decreases by 10-15%.

--------------------------------------------------------------------------------

PROGRAM WORKFLOW DIAGRAM:

+-------------------------------------------------------------+
| 1. DATA INPUT                                               |
|    - 21 sculptures                                          |
|    - 210 distances between them (in meters)                 |
|    - Starting point (A1)                                    |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 2. GRAPH CONSTRUCTION                                       |
|    Function: rozbir()                                       |
|    Creates structure: vertices + edges with weights         |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 3. GREEDY ALGORITHM                                         |
|    Function: greedystart()                                  |
|    Builds initial route (approximately 13 km)               |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 4. 2-OPT OPTIMIZATION                                       |
|    Function: pokrashchty()                                  |
|    Removes zigzags and crossings (approximately 11.5 km)    |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 5. RESULT OUTPUT                                            |
|    - Visit sequence                                         |
|    - Total distance                                         |
|    - Walking time (approximately 3 hours)                   |
+-------------------------------------------------------------+

================================================================================
3. SETUP INSTRUCTIONS
================================================================================

STEP 1: INSTALLING PYTHON
--------------------------

WINDOWS:
1. Download Python from the official website:
   https://www.python.org/downloads/
2. Run the installer
3. IMPORTANT: Check "Add Python to PATH"
4. IMPORTANT: Check "tcl/tk and IDLE" (required for GUI)
5. Click "Install Now"
6. Restart your computer

Verification:
   python --version

Should display: Python 3.x.x

--------------------------------------------------------------------------------

MACOS:
1. Open Terminal
2. Install Homebrew (if not already installed):

   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

3. Install Python:
   brew install python-tk

Verification:
   python3 --version

--------------------------------------------------------------------------------

LINUX (UBUNTU/DEBIAN):
   sudo apt update
   sudo apt install python3 python3-tk

Verification:
   python3 --version

================================================================================

STEP 2: DOWNLOADING THE PROGRAM
--------------------------------

OPTION A: Via Git
   git clone https://github.com/4marchello/lutsk-route-optimizer.git
   cd lutsk-route-optimizer

OPTION B: Download ZIP
1. Download the ZIP archive from GitHub
2. Extract to a convenient folder
3. Open the folder in terminal/command prompt

================================================================================

STEP 3: RUNNING THE PROGRAM
----------------------------

WINDOWS:
   python route_optimizer.py

MACOS/LINUX:
   python3 route_optimizer.py

Successful launch:
A window with a graphical interface should open.

================================================================================

TROUBLESHOOTING INSTALLATION
-----------------------------

Error: "python is not recognized"
Cause: Python not added to PATH
Solution: 
1. Reinstall Python with "Add to PATH" checked
2. OR add manually to environment variables

Error: "No module named tkinter"
Cause: Tkinter not installed
Solution:
   Ubuntu/Debian: sudo apt install python3-tk
   macOS: brew install python-tk

Error: "Permission denied"
Cause: Insufficient permissions
Solution:
   chmod +x route_optimizer.py

================================================================================
4. PROGRAM USAGE INSTRUCTIONS
================================================================================

PROGRAM INTERFACE
-----------------

+------------------------------------------------------------+
| Route Search (2-opt optimization)           [_][□][X]     |
+------------------------------------------------------------+
|                                                            |
| Edges (A B 10):                                            |
| +--------------------------------------------------------+ |
| | A1 B2 2850                                             | |
| | A1 C3 3260                                             | |
| | B2 C3 1010                                             | |
| | ... (210 lines)                                        | |
| |                                                        | |
| |                                                        | |
| +--------------------------------------------------------+ |
|                                                            |
| Start: [A1      ]                                          |
|                                                            |
|            [ Calculate ]                                   |
|                                                            |
| Result:                                                    |
| +--------------------------------------------------------+ |
| | Route (Optimized):                                     | |
| | A1 -> B2 -> C3 -> D4 -> E5 -> ...                      | |
| |                                                        | |
| | Total weight: 11503.0                                  | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+

================================================================================

STEP-BY-STEP INSTRUCTIONS
--------------------------

STEP 1: DATA INPUT (optional)
By default, the program already contains all 210 distances between sculptures.

Format: Vertex1 Vertex2 Distance_in_meters

Example:
A1 B2 2850
A1 C3 3260
B2 C3 1010

When to modify:
- Adding new sculptures
- Changes in pedestrian paths (repairs, new roads)
- Testing on custom data

--------------------------------------------------------------------------------

STEP 2: CHOOSING STARTING POINT
In the "Start" field, specify the sculpture code from which you'll begin.

Available codes:
A1  - Radyk Zadovolenyi (central park) [default]
B2  - Zustrichayko
C3  - Hnat
D4  - Vasyl "Soloveiko"
E5  - Franyo
F6  - Khvatsko i Prudko
G7  - Knyzhko
H8  - Semen Hust
I9  - Zirko
J10 - Trilinko
K11 - Muzyka
L12 - Vertun
M13 - Vartko i Vartko
N14 - Klikun Andriy
O15 - Stepan
P16 - Kavus
Q17 - Kliuchnyk
R18 - Providnyk
S19 - Bratko i Bratko
T20 - Vohnar
U21 - Mykytovych

How to change:
1. Click on the "Start" field
2. Delete the old value
3. Enter new code (e.g., G7)

--------------------------------------------------------------------------------

STEP 3: ROUTE CALCULATION
1. Click the "Calculate" button
2. Wait 2-5 seconds (depends on computer speed)
3. Result will appear in the "Result" field

What the result shows:

Route (Optimized):
A1 -> B2 -> C3 -> D4 -> E5 -> F6 -> L12 -> N14 -> 
M13 -> O15 -> T20 -> U21 -> S19 -> R18 -> Q17 -> 
P16 -> K11 -> J10 -> I9 -> G7 -> H8

Total weight: 11503.0

Explanation:
- Arrows show the visiting order
- Total weight - total distance in meters (11503 m = 11.5 km)

--------------------------------------------------------------------------------

STEP 4: SAVING RESULTS

OPTION 1: Copy text
1. Select text in the "Result" field
2. Press Ctrl+C (Windows/Linux) or Cmd+C (macOS)
3. Paste into any text editor

OPTION 2: Screenshot
Windows: Win + Shift + S
macOS: Cmd + Shift + 4
Linux: Print Screen

================================================================================

ERROR MESSAGES
--------------

"Specify start"
Cause: "Start" field is empty
Solution: Enter sculpture code (A1, B2, etc.)

"Start A1 is missing"
Cause: Specified sculpture not found in graph
Solution: Check code correctness (capital letters!)

"Graph is empty"
Cause: No distance data
Solution: Insert data in "Edges" field

"Graph is disconnected, route incomplete"
Cause: Not all sculptures are connected
Solution: Add missing edges or remove isolated vertices

================================================================================
5. LICENSE AND COPYRIGHT
================================================================================

CODE LICENSE
------------

MIT License

Copyright (c) 2025 [A. S. Osadchyi, M. S. Vavdiiuk by LNTU]

Permission is hereby granted, free of charge, to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of this software, 
provided that the above copyright notice is preserved.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

================================================================================

DATA COPYRIGHT
--------------
- Distances between sculptures: Obtained from Google Maps API
- Coordinates: Open data from Lutsk City Council
- Sculpture names: "Lutsk Klikuns" project, Lutsk City Council

================================================================================

PROGRAM USAGE
-------------

ALLOWED:
- Personal use
- Educational use
- Code modification
- Distribution with author attribution
- Commercial use (with author's permission)

PROHIBITED:
- Claiming as your own work without attribution
- Use for illegal purposes
- Selling without author's permission

================================================================================

ATTRIBUTION
-----------
When using the code or research results, please add a reference:

[A. S. Osadchyi, M. S. Vavdiiuk]. (2025). Optimization of Pedestrian Tourist 
Routes Using Graph Theory Algorithms: A Case Study of "Lutsk Klikuns". 
GitHub repository: https://github.com/4marchello/lutsk-route-optimizer

================================================================================
6. CONTACT INFORMATION
================================================================================

PROJECT AUTHORS
---------------
Name: Marko Vavdiiuk, Arsen Osadchyi
Position: Students, PRM-11 course
Faculty: Architecture and Construction
University: Lutsk National Technical University
City: Lutsk, Ukraine

CONTACT AUTHORS
---------------
Email: markoo.vavdiyuk@gmail.com / jdtaaa000@gmail.com

SCIENTIFIC SUPERVISOR
---------------------
Name: Inga Viktorivna Samonenko
Position: Associate Professor, Department of Applied Mathematics and Mechanics
Degree: PhD in Statistics, University of Sydney, Australia
Email: i.samonenko@lntu.edu.ua

PROJECT REPOSITORY
------------------
GitHub: https://github.com/4marchello/lutsk-route-optimizer

================================================================================

KNOWN LIMITATIONS
-----------------

1. MAXIMUM 50 VERTICES:
   For larger numbers, computation time grows exponentially

2. COMPLETE GRAPH ONLY:
   If there's no path between two sculptures, route will be incomplete

3. NO ELEVATION CONSIDERATION:
   Program doesn't account for ascents/descents (only horizontal distance)

4. NO GPX EXPORT:
   Result cannot be loaded into GPS navigator (planned in v2.0)

================================================================================

8. AUTHOR INFORMATION AND ACKNOWLEDGMENTS
================================================================================

LEAD AUTHORS
------------
Marko Vavdiiuk
Student PRM-11 course, Faculty of Architecture and Construction
Lutsk National Technical University, Lutsk, Ukraine

Arsen Osadchyi
Student PRM-11 course, Faculty of Architecture and Construction
Lutsk National Technical University, Lutsk, Ukraine

Contributions:
- Development of optimization algorithms
- Software implementation (Python)
- Collection of distance data
- Testing and debugging
- Documentation writing

================================================================================

SCIENTIFIC SUPERVISOR
---------------------
Inga Viktorivna Samonenko
Associate Professor, Department of Applied Mathematics and Mechanics
PhD in Statistics from University of Sydney, Australia
Lutsk National Technical University (LNTU)

Contributions:
- Scientific consulting
- Methodology selection
- Work review

================================================================================

DISCLAIMER
----------

This program is provided "as is" without any warranties. The authors are not 
responsible for:
- Inaccuracies in distance data
- Changes in city infrastructure
- Closure of access to certain locations
- Physical injuries during route navigation
- Data loss or equipment damage

RECOMMENDATIONS:
- Always verify route relevance before departure
- Consider weather conditions and time of day
- Wear comfortable shoes and clothing
- Carry water and snacks
- Inform loved ones about your route

================================================================================

ADDITIONAL RESOURCES
--------------------

USEFUL LINKS:
- Official "Lutsk Klikuns" project website: 
  https://www.lutskrada.gov.ua/pages/lutski-klykuny
- Interactive map of Lutsk: https://www.google.com/maps

================================================================================

Last updated: January 13, 2025

GLORY TO UKRAINE!

================================================================================
                          END OF DOCUMENT
================================================================================

[README_EN.md](https://github.com/user-attachments/files/24596908/README_EN.md)
