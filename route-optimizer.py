import tkinter as tk
from tkinter import messagebox
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# FUNCTION: rozbir
# PURPOSE: Parses a textual description of a graph and constructs a data structure
# INPUT: txt - text in the format “vertex1 vertex2 weight”
# OUTPUT: graf - dictionary of dictionaries with edge weights
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def rozbir(txt):
    # Structure: {vertex1: {vertex2: weight, ...}, ...}
    graf={}
    ryadky=txt.strip().splitlines()
    for ryad in ryadky:
        ryad=ryad.strip()
        if not ryad or ryad.startswith("#"):
            continue
        #Break the string into parts: vertex1, vertex2, weight
        chast=ryad.split()
        if len(chast)!=3:
            raise ValueError(f"Некоректний рядок: {ryad}")
        v1,v2,vstr=chast[0],chast[1],chast[2]
        try:
            vaga=float(vstr)
        except:
            raise ValueError(f"Некоректна вага: {ryad}")
        if v1 not in graf:
            graf[v1]={}
        if v2 not in graf:
            graf[v2]={}
        # Add an edge from v1 to v2 with weight (undirected graph)
        graf[v1][v2]=vaga
        #Add an edge from v2 to v1 with the same weight (symmetrically)
        graf[v2][v1]=vaga
    if not graf:
        raise ValueError("Граф порожній.")
    
    return graf
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# FUNCTION: rahsumu
# PURPOSE: Calculates the total length of the route
# INPUT: graf - graph, shlyah - list of vertices (route)
# OUTPUT: total distance of the route (or infinity if the path is impossible)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def rahsumu(graf,shlyah):
    # Initialize the sum of distances
    s=0.0
    # We pass through all the pairs of neighboring peaks on the route
    for i in range(len(shlyah)-1):
        # Take the current vertex and the next one
        u,v=shlyah[i],shlyah[i+1]
        # Check if there is an edge between these vertices
        if v in graf[u]:
            # Add the weight of the ribs to the total amount
            s+=graf[u][v]
        else:
            # If there are no ribs, the route is impossible
            return float('inf')
    
    return s
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# FUNCTION: greedystart
# PURPOSE: Greedy route search algorithm (Nearest Neighbor)
# PRINCIPLE OF OPERATION: At each step, we select the nearest unvisited vertex.
# INPUT: graf - graph, start - starting vertex
# OUTPUT: list of vertices in order of visitation
# NOTE: This algorithm is fast but does not guarantee an optimal solution
# Often creates “zigzags” at the end of the route
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def greedystart(graf,start):
    # Checking whether the starting vertex exists in the graph
    if start not in graf:
        raise ValueError(f"Старт {start} відсутній.")
    vidv=[start]
    # Current vertex (where we are now)
    pot=start
    # We will continue until we have visited all the peaks
    while len(vidv)<len(graf):
        # Get all neighbors of the current vertex
        sus=graf[pot]
        # List of candidates for the next step (unvisited neighbors)
        kand=[]
        # We go through all the neighbors
        for v,vaga in sus.items():
            # Add only those that have not yet been visited
            if v not in vidv:
                kand.append((vaga,v))
        # If there are no unvisited neighbors, we stop.
        if not kand:
            break
        # Sort candidates by distance (the closest will be first)
        kand.sort(key=lambda x:x[0])
        # Selecting the nearest peak
        nast=kand[0][1]
        # Add it to the route
        vidv.append(nast)
        # Moving to this peak
        pot=nast
    return vidv
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# FUNCTION: pokrashchty
# PURPOSE: Route optimization using the 2-opt method
# PRINCIPLE OF OPERATION: Finds intersections in the route and corrects them
# 
# ALGORITHM:
# 1. Take two edges in the route: (A->B) and (C->D)
# 2. Check whether the route can be improved by switching: (A->C) and (B->D)
# 3. If the new combination is shorter, apply the change
# 4. Repeat until there are no more improvements
# 
# RESULT: Eliminates “zigzags” and intersections, making the route smoother
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def pokrashchty(graf,shlyah):
    # Create a copy of the original route
    bestshlyah=shlyah[:]
    # Calculate the length of the initial route
    bestdist=rahsumu(graf,bestshlyah)
    # Flag indicating whether there was improvement in this iteration
    pokraschennya=True
    # We continue while there are improvements
    while pokraschennya:
        # First, we assume that there are no improvements.
        pokraschennya=False
        # We go through all possible pairs of edges to check.
        # We start with 1
        # Not to change the starting point A1.
        for i in range(1,len(bestshlyah)-1):
            for j in range(i+1,len(bestshlyah)):
                # Skip adjacent vertices
                if j-i==1:
                    continue
                # Creating a new route with an inverted segment
                newshlyah=bestshlyah[:]
                # Reverse part of the route from i to j
                # Example: [A,B,C,D,E] → reverse [B,C,D] -> [A,D,C,B,E]
                newshlyah[i:j]=bestshlyah[i:j][::-1]
                # Calculating the length of the new route
                dist=rahsumu(graf,newshlyah)
                # If the new route is shorter, we keep it.
                if dist<bestdist:
                    bestshlyah=newshlyah
                    bestdist=dist
                    pokraschennya=True
                    # Found improvements - let's start the cycle again
                    break
            # If improvements are found, we exit both cycles.
            if pokraschennya:
                break
    # Return the optimized route and its length
    return bestshlyah,bestdist


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# FUNCTION: natysk
# PURPOSE: Processes pressing the “Calculate” button
# ACTIONS:
# 1. Reads data from the text field (graph)
# 2. Reads the starting vertex
# 3. Builds a graph from the text
# 4. Applies a greedy algorithm
# 5. Optimizes the result using the 2-opt method
# 6. Outputs the result to the text field
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def natysk():
    # Read text from the graph description field
    tekstreb=txtreb.get("1.0",tk.END)
    # Read the name of the starting vertex
    start=vststart.get().strip()
    # Checking if the starting vertex is specified
    if not start:
        messagebox.showerror("Помилка","Вкажи старт.")
        return
    try:
        # STEP 1: Constructing a graph from a text description
        graf=rozbir(tekstreb)
        # STEP 2: Apply a greedy algorithm (fast but inaccurate)
        pochatkshlyah=greedystart(graf,start)
        # Checking whether we managed to visit all the peaks
        if len(pochatkshlyah)!=len(graf):
            messagebox.showwarning("Увага","Граф розірваний, маршрут неповний!")
        # STEP 3: Optimize the route using the 2-opt method (remove zigzags)
        finalshlyah,suma=pokrashchty(graf,pochatkshlyah)
        # STEP 4: Formulate the text of the result
        rez="Маршрут (Оптимізований):\n"
        rez+=" -> ".join(finalshlyah)
        rez+="\n\nСумарна вага: "+str(suma)
        # STEP 5: Display the result in a text field
        txtrez.config(state="normal")
        txtrez.delete("1.0",tk.END)
        txtrez.insert(tk.END,rez)
        txtrez.config(state="disabled")
    except Exception as pom:
        # Error
        messagebox.showerror("Помилка",str(pom))


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# FUNCTION: golovna
# PURPOSE: Creates a graphical interface for the program
# ELEMENTS:
# - Text field for entering the graph (21 sculptures)
# - Field for selecting the starting point (default A1)
# - “Calculate” button
# - Field for displaying the result (optimal route)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def golovna():
    global txtreb,vststart,txtrez
    vikno=tk.Tk()
    vikno.title("Пошук шляху (2-opt optimization)")
    
    # --- SECTION 1: Graph Input ---
    
    # Header for input field
    tk.Label(vikno,text="Ребра (A B 10):").pack(anchor="w",padx=10,pady=(10,0))
    # Large text field for entering graph edges
    # Format: vertex1 vertex2 distance_in_meters
    txtreb=tk.Text(vikno,width=60,height=15)
    txtreb.pack(padx=10,pady=5)
    # 21 sculpture “Lutsk Criers” with actual distances
    # Data obtained via Google Maps for walking routes
    pryklad="""A1 B2 2850
A1 C3 3260
A1 D4 4390
A1 E5 5040
A1 F6 5390
A1 G7 4470
A1 H8 4250
A1 I9 4840
A1 J10 5030
A1 K11 5070
A1 L12 5900
A1 M13 5820
A1 N14 5840
A1 O15 5850
A1 P16 5220
A1 Q17 5450
A1 R18 5530
A1 S19 5810
A1 T20 6130
A1 U21 6400
B2 C3 1010
B2 D4 2080
B2 E5 2850
B2 F6 3200
B2 G7 2200
B2 H8 1680
B2 I9 2440
B2 J10 2560
B2 K11 2560
B2 L12 3750
B2 M13 3610
B2 N14 3660
B2 O15 3650
B2 P16 2770
B2 Q17 2970
B2 R18 3030
B2 S19 3340
B2 T20 3660
B2 U21 3930
C3 D4 1150
C3 E5 1910
C3 F6 2300
C3 G7 1360
C3 H8 1290
C3 I9 1770
C3 J10 1940
C3 K11 2010
C3 L12 2870
C3 M13 2760
C3 N14 2800
C3 O15 2780
C3 P16 2180
C3 Q17 2390
C3 R18 2410
C3 S19 2750
C3 T20 2910
C3 U21 3200
D4 E5 865
D4 F6 1450
D4 G7 779
D4 H8 1640
D4 I9 1080
D4 J10 1260
D4 K11 1300
D4 L12 2110
D4 M13 1980
D4 N14 2030
D4 O15 2020
D4 P16 1490
D4 Q17 1680
D4 R18 1730
D4 S19 2050
D4 T20 2130
D4 U21 2420
E5 F6 572
E5 G7 1060
E5 H8 1920
E5 I9 1210
E5 J10 1380
E5 K11 1510
E5 L12 1410
E5 M13 1290
E5 N14 1510
E5 O15 1320
E5 P16 1620
E5 Q17 1650
E5 R18 1530
E5 S19 1820
E5 T20 1630
E5 U21 1920
F6 G7 962
F6 H8 1850
F6 I9 1110
F6 J10 1140
F6 K11 1260
F6 L12 949
F6 M13 857
F6 N14 858
F6 O15 815
F6 P16 1390
F6 Q17 1400
F6 R18 1140
F6 S19 1290
F6 T20 1100
F6 U21 1390
G7 H8 910
G7 I9 385
G7 J10 559
G7 K11 598
G7 L12 1530
G7 M13 1420
G7 N14 1420
G7 O15 1440
G7 P16 761
G7 Q17 960
G7 R18 1030
G7 S19 1340
G7 T20 1580
G7 U21 1880
H8 I9 892
H8 J10 991
H8 K11 964
H8 L12 2160
H8 M13 2080
H8 N14 2080
H8 O15 2050
H8 P16 1140
H8 Q17 1380
H8 R18 1460
H8 S19 1790
H8 T20 2110
H8 U21 2380
I9 J10 184
I9 K11 230
I9 L12 1390
I9 M13 1240
I9 N14 1300
I9 O15 1290
I9 P16 373
I9 Q17 602
I9 R18 655
I9 S19 967
I9 T20 1280
I9 U21 1550
J10 K11 154
J10 L12 1220
J10 M13 1110
J10 N14 1140
J10 O15 1120
J10 P16 200
J10 Q17 410
J10 R18 474
J10 S19 774
J10 T20 1090
J10 U21 1360
K11 L12 1340
K11 M13 1210
K11 N14 1240
K11 O15 1240
K11 P16 172
K11 Q17 420
K11 R18 627
K11 S19 926
K11 T20 1250
K11 U21 1520
L12 M13 140
L12 N14 85
L12 O15 135
L12 P16 1390
L12 Q17 1070
L12 R18 784
L12 S19 622
L12 T20 434
L12 U21 723
M13 N14 15
M13 O15 42
M13 P16 1260
M13 Q17 958
M13 R18 622
M13 S19 537
M13 T20 346
M13 U21 640
N14 O15 47
N14 P16 1290
N14 Q17 983
N14 R18 697
N14 S19 534
N14 T20 348
N14 U21 639
O15 P16 1290
O15 Q17 969
O15 R18 690
O15 S19 487
O15 T20 297
O15 U21 590
P16 Q17 356
P16 R18 658
P16 S19 945
P16 T20 1270
P16 U21 1540
Q17 R18 291
Q17 S19 593
Q17 T20 900
Q17 U21 1180
R18 S19 337
R18 T20 621
R18 U21 914
S19 T20 313
S19 U21 583
T20 U21 296"""
    

    txtreb.insert(tk.END,pryklad)
    
    # --- SECTION 2: Choosing a starting point ---
    
    # Create a separate frame for the starting point
    r=tk.Frame(vikno)
    r.pack(anchor="w",padx=10,pady=(5,0))
    # Start
    tk.Label(r,text="Старт:").pack(side=tk.LEFT)
    # Field for entering the name of the starting vertex
    vststart=tk.Entry(r,width=10)
    vststart.pack(side=tk.LEFT,padx=(5,0))
    # A1 start
    vststart.insert(0,"A1")
    
    # --- SECTION 3: Calculation button ---
    
    # Button that launches the optimization algorithm
    tk.Button(vikno,text="Розрахувати",command=natysk).pack(pady=10)
    
    # --- SECTION 4: Outputting the result ---
    
    # Heading for the result field
    tk.Label(vikno,text="Результат:").pack(anchor="w",padx=10)
    # Text field for displaying the optimal route
    # state="disabled" - read-only field
    txtrez=tk.Text(vikno,width=60,height=6,state="disabled")
    txtrez.pack(padx=10,pady=(0,10))
    # Start the main GUI event processing loop
    vikno.mainloop()


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# PROGRAM ENTRY POINT
# Check if the file is run directly (not imported)
# If so, run the main function
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
if __name__=="__main__":
    golovna()


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# GENERAL PROGRAM STRUCTURE:
#
# 1. rozbir() - parses text and builds a graph
# 2. greedystart() - greedy algorithm (fast initial route)
# 3. pokrashchty() - 2-opt optimization (removes zigzags)
# 4. rahsumu() - calculates the length of the route
# 5. natysk() - processes button presses
# 6. golovna() - creates GUI
#
# RESULT:
# Optimal route length ~11.5 km to visit all 21 sculptures
# “Lutsk Criers” starting from point A1 (Radik Zadowolony)
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
