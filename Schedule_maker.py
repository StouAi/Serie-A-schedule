
import pulp
import time
import matplotlib.pyplot as plt


stats = int(input("Enter 1 to see the graph representing calculation time based on minum number of matches between the same teams: "))

if stats == 1:
    # X-axis values: Minimum number of matches between games of the same teams
    x = [2, 3, 4, 5, 6, 7, 8]

    # Y-axis values: Time taken in seconds
    y = [330, 900, 1300, 1e5, 1e5, 1e5, 1e5]  # Using 1e5 to represent impractically long times

    plt.plot(x, y, marker='o')
    plt.xlabel("Minimum number of matches between games of the same teams")
    plt.ylabel("Time taken in seconds (log scale)")
    plt.title("Time taken based on selection")
    plt.yscale('log')  # Set y-axis to logarithmic scale
    plt.grid(True, which="both", ls="--")
    plt.show()
while True:
    selection = int(input("Enter the minumum number of matches between games of the same teams(2-8): "))
    if selection > 8 or selection < 2:
        print("Please enter a number valid number")
    else:
        break

teams = [
    "Atalanta",       # 0
    "Bologna",        # 1
    "Cagliari",       # 2
    "Roma",           # 3
    "Empoli",         # 4
    "Fiorentina",     # 5
    "Lazio",          # 6
    "Hellas Verona",  # 7
    "Internazionale", # 8
    "AC Milan",       # 9
    "Juventus",       # 10
    "Napoli",         # 11
    "Udinese",        # 12
    "Torino",         # 13
    "Genoa",          # 14
    "Lecce",          # 15
    "Como" ,          # 16
    "Venezia",        # 17
    "Monza",          # 18
    "Parma"           # 19
    
]



time_now = time.time()
num_teams = len(teams)
num_matchdays = 2 * (num_teams - 1)
print(num_matchdays)
# HOME = 1, AWAY = 0

# x = 1 when team i plays at home versus team j on matchday k
x = pulp.LpVariable.dicts("x", (range(num_teams), range(num_teams), range(num_matchdays)), 0, 1, pulp.LpBinary)

# y = 1 when team i plays at home on matchday k
y = pulp.LpVariable.dicts("y", (range(num_teams), range(num_matchdays)), 0, 1, pulp.LpBinary)

# Create the problem
problem = pulp.LpProblem("Schedule", pulp.LpMinimize)

# Connect y to x
for i in range(num_teams):
    for k in range(num_matchdays):
        problem += y[i][k] == pulp.lpSum([x[i][j][k] for j in range(num_teams)])

# Constraint 1: Each team plays exactly one game on each matchday
for i in range(num_teams):
    for k in range(num_matchdays):
        problem += pulp.lpSum([x[i][j][k] + x[j][i][k] for j in range(num_teams) if j != i]) == 1

# Constraint 2: Each team plays against each other team twice (both home and away) over the entire season
for i in range(num_teams):
    for j in range(num_teams):
        if i != j:
            problem += pulp.lpSum([x[i][j][k] for k in range(num_matchdays)]) == 1
            problem += pulp.lpSum([x[j][i][k] for k in range(num_matchdays)]) == 1

# Constraint 3: Each pair of teams plays once in each half of the season
half_matchdays = num_matchdays // 2
for i in range(num_teams):
    for j in range(num_teams):
        if i != j:
            problem += pulp.lpSum([x[i][j][k] + x[j][i][k] for k in range(half_matchdays)]) == 1
            problem += pulp.lpSum([x[i][j][k] + x[j][i][k] for k in range(half_matchdays, num_matchdays)]) == 1

# Constraint 4: Each team plays at most two consecutive home or away games
for i in range(num_teams):
    for k in range(num_matchdays - 2):
        problem += y[i][k] + y[i][k + 1] + y[i][k + 2] <= 2

# Constraint 5: Minimum distance of _ matchdays between games of the same teams
match_distance = selection
for i in range(num_teams):
    for j in range(num_teams):
        if i != j:
            for k in range(half_matchdays - match_distance, half_matchdays + match_distance):
                for d in range(1, match_distance + 1):
                    if k + d < num_matchdays:
                        problem += x[i][j][k] + x[i][j][k + d] <= 1
                        problem += x[j][i][k] + x[j][i][k + d] <= 1

# Constraint 6: On MD1, MD2, MD5, MD6 and MD38 neither the 
# matches between Napoli, Inter, Milan, and Atalanta nor the local derbies of 
# Tuscany (EMPOLI-FIORENTINA) can be scheduled.
for k in [0, 1, 4, 5, num_matchdays - 1]:
    for i in [0,3, 4,6, 5, 8, 9, 10,13,11]:  # Atalanta, Empoli, Fiorentina, Inter, Milan, Napoli
        for j in [0, 3,4,6, 5, 8, 9,10,13, 11]:
            if i != j:
                problem += x[i][j][k] + x[j][i][k] == 0

# Constraint 7: There must be an absolute alternation of home and away matches between
# the following combinations of Clubs: EMPOLI - FIORENTINA, INTER - MILAN
#JUVENTUS - TORINO,LAZIO - ROMA

# Empoli (4) - Fiorentina (5)
for k in range(num_matchdays):
    problem += y[4][k] + y[5][k] == 1

# Inter (8) - Milan (9)
for k in range(num_matchdays):
    problem += y[8][k] + y[9][k] == 1

#Roma (3) - Lazio (6)
for k in range(num_matchdays):
    problem += y[3][k] + y[6][k] == 1

#Juventus (10) - Torino (13)
for k in range(num_matchdays):
    problem += y[10][k] + y[13][k] == 1

# Constraint 8: All local derbies must be played on different matchdays
# Milan (9) - Inter (8), Fiorentina (5) - Empoli (4), Roma (3) - Lazio (6), 
# Juventus (10) - Torino (13)
for k in range(num_matchdays):
    problem += (
        x[8][9][k] + x[9][8][k] + 
        x[5][4][k] + x[4][5][k]+
        x[3][6][k] + x[6][3][k] +
        x[10][13][k] + x[13][10][k] 
    ) <= 1

# Objective value
Z = 0
problem += Z

# Solve the problem
problem.solve()

# Print the results

# print(f"{'Matchday':<10} {'Home Team':<20} {'Away Team':<20}")
# print("=" * 50)
# for k in range(num_matchdays):
#     print(f"Matchday {k + 1}:")
#     for i in range(num_teams):
#         for j in range(num_teams):
#             if i != j and pulp.value(x[i][j][k]) == 1:
#                 print(f"{'':<10} {teams[i]:<20} {teams[j]:<20}")
#     print("=" * 50)

# Print the results correctly
print(f"{'Matchday':<10} {'Home Team':<20} {'Away Team':<20}")
print("=" * 50)
for k in range(num_matchdays):
    match_set = set()  # To keep track of printed matches
    print(f"Matchday {k + 1}:")
    for i in range(num_teams):
        for j in range(num_teams):
            if i != j and pulp.value(x[i][j][k]) == 1 and (i, j) not in match_set:
                print(f"{'':<10} {teams[i]:<20} {teams[j]:<20}")
                match_set.add((i, j))  # Mark this match as printed
    print("=" * 50)

print(f"Time taken: {time.time() - time_now:.2f} seconds")


