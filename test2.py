import pulp
import time

# Updated team names after removing the first four teams
teams = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
]

time_now = time.time()
num_teams = len(teams)
num_matchdays = 2 * (num_teams - 1)
# HOME = 1, AWAY = 0

# x = 1 when team i plays at home versus team j on matchday k
x = pulp.LpVariable.dicts("x", (range(num_teams), range(num_teams), range(num_matchdays)), 0, 1, pulp.LpBinary)

y = pulp.LpVariable.dicts("y", (range(num_teams), range(num_matchdays)), 0, 1, pulp.LpBinary)

# Create the problem
problem = pulp.LpProblem("Schedule", pulp.LpMaximize)

# Connect y to x
for i in range(num_teams):
    for k in range(num_matchdays):
        problem += y[i][k] == pulp.lpSum([x[i][j][k] for j in range(num_teams)])

# Constraint 1: each team plays exactly one game on each matchday
for i in range(num_teams):
    for k in range(num_matchdays):
        problem += pulp.lpSum([x[i][j][k] + x[j][i][k] for j in range(num_teams) if j!=i] ) == 1

# Constraint 2: Each team plays exactly one game against each other team twice (both home and away) over the entire season
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





# Solve the problem
problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}")
for k in range(num_matchdays):
    print(f"Matchday {k + 1}:")
    for i in range(num_teams):
        for j in range(num_teams):
            if i != j and pulp.value(x[i][j][k]) == 1:
                print(f"  {teams[i]} vs {teams[j]}")
    print("")

print(f"Time taken: {time.time() - time_now:.2f} seconds")
