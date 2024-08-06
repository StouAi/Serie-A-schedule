from collections import defaultdict

# List of matchdays
matchdays = [
    [
        ("Atalanta", "Venezia"), ("Empoli", "Hellas Verona"), ("Lazio", "Venezia"),
        ("AC Milan", "Bologna"), ("Napoli", "Lecce"), ("Udinese", "Fiorentina"),
        ("Torino", "Cagliari"), ("Como", "Juventus"), ("Monza", "Roma"), ("Parma", "Internazionale")
    ],
    [
        ("Atalanta", "Cagliari"), ("Bologna", "Fiorentina"), ("Empoli", "Monza"),
        ("Lazio", "Udinese"), ("Internazionale", "Como"), ("Juventus", "Venezia"),
        ("Napoli", "Hellas Verona"), ("Venezia", "AC Milan"), ("Lecce", "Roma"), ("Parma", "Torino")
    ],
    [
        ("Bologna", "Lazio"), ("Cagliari", "Hellas Verona"), ("Roma", "Empoli"),
        ("Fiorentina", "Parma"), ("Internazionale", "Atalanta"), ("Juventus", "Napoli"),
        ("Udinese", "AC Milan"), ("Lecce", "Monza"), ("Como", "Torino"), ("Venezia", "Venezia")
    ],
    [
        ("Atalanta", "Napoli"), ("Cagliari", "Internazionale"), ("Roma", "Fiorentina"),
        ("Empoli", "Lazio"), ("Hellas Verona", "Bologna"), ("AC Milan", "Lecce"),
        ("Torino", "Udinese"), ("Venezia", "Monza"), ("Venezia", "Como"), ("Parma", "Juventus")
    ],
    [
        ("Fiorentina", "Cagliari"), ("Lazio", "Venezia"), ("Hellas Verona", "Roma"),
        ("Internazionale", "Udinese"), ("Napoli", "Bologna"), ("Torino", "Venezia"),
        ("Lecce", "Juventus"), ("Como", "Empoli"), ("Monza", "AC Milan"), ("Parma", "Atalanta")
    ],
    [
        ("Atalanta", "Monza"), ("Bologna", "Torino"), ("Roma", "Cagliari"),
        ("Empoli", "Parma"), ("AC Milan", "Hellas Verona"), ("Juventus", "Udinese"),
        ("Napoli", "Venezia"), ("Venezia", "Internazionale"), ("Lecce", "Lazio"), ("Como", "Fiorentina")
    ],
    [
        ("Bologna", "Juventus"), ("Cagliari", "Venezia"), ("Fiorentina", "Napoli"),
        ("Lazio", "AC Milan"), ("Hellas Verona", "Atalanta"), ("Internazionale", "Roma"),
        ("Udinese", "Monza"), ("Torino", "Empoli"), ("Venezia", "Lecce"), ("Parma", "Como")
    ],
    [
        ("Atalanta", "Lazio"), ("Cagliari", "Venezia"), ("Roma", "Juventus"),
        ("Empoli", "Bologna"), ("Hellas Verona", "Lecce"), ("AC Milan", "Fiorentina"),
        ("Torino", "Internazionale"), ("Venezia", "Napoli"), ("Como", "Monza"), ("Parma", "Udinese")
    ],
    [
        ("Atalanta", "Bologna"), ("Fiorentina", "Empoli"), ("Lazio", "Torino"),
        ("AC Milan", "Parma"), ("Juventus", "Hellas Verona"), ("Napoli", "Cagliari"),
        ("Udinese", "Lecce"), ("Como", "Venezia"), ("Venezia", "Roma"), ("Monza", "Internazionale")
    ],
    [
        ("Bologna", "Como"), ("Cagliari", "Lecce"), ("Roma", "Udinese"),
        ("Empoli", "Atalanta"), ("Hellas Verona", "Lazio"), ("Internazionale", "Juventus"),
        ("Napoli", "AC Milan"), ("Torino", "Venezia"), ("Venezia", "Parma"), ("Monza", "Fiorentina")
    ],
    [
        ("Bologna", "Monza"), ("Cagliari", "Juventus"), ("Fiorentina", "Venezia"),
        ("Lazio", "Internazionale"), ("AC Milan", "Roma"), ("Udinese", "Atalanta"),
        ("Torino", "Napoli"), ("Venezia", "Empoli"), ("Como", "Hellas Verona"), ("Parma", "Lecce")
    ],
    [
        ("Atalanta", "AC Milan"), ("Empoli", "Venezia"), ("Lazio", "Roma"),
        ("Hellas Verona", "Torino"), ("Internazionale", "Napoli"), ("Juventus", "Fiorentina"),
        ("Udinese", "Venezia"), ("Lecce", "Bologna"), ("Como", "Cagliari"), ("Monza", "Parma")
    ],
    [
        ("Bologna", "Udinese"), ("Cagliari", "Parma"), ("Roma", "Torino"),
        ("Fiorentina", "Hellas Verona"), ("AC Milan", "Internazionale"), ("Juventus", "Empoli"),
        ("Napoli", "Lazio"), ("Venezia", "Atalanta"), ("Lecce", "Como"), ("Venezia", "Monza")
    ],
    [
        ("Atalanta", "Juventus"), ("Cagliari", "Bologna"), ("Roma", "Como"),
        ("Empoli", "Lecce"), ("Internazionale", "Fiorentina"), ("Napoli", "Udinese"),
        ("Torino", "AC Milan"), ("Venezia", "Hellas Verona"), ("Venezia", "Parma"), ("Monza", "Lazio")
    ],
    [
        ("Atalanta", "Torino"), ("Bologna", "Venezia"), ("Empoli", "Napoli"),
        ("Lazio", "Cagliari"), ("Hellas Verona", "Internazionale"), ("AC Milan", "Venezia"),
        ("Juventus", "Monza"), ("Udinese", "Como"), ("Lecce", "Fiorentina"), ("Parma", "Roma")
    ],
    [
        ("Cagliari", "Udinese"), ("Roma", "Venezia"), ("Fiorentina", "Torino"),
        ("Internazionale", "Empoli"), ("Juventus", "Lazio"), ("Napoli", "Parma"),
        ("Lecce", "Atalanta"), ("Como", "AC Milan"), ("Venezia", "Bologna"), ("Monza", "Hellas Verona")
    ],
    [
        ("Bologna", "Internazionale"), ("Cagliari", "Empoli"), ("Roma", "Atalanta"),
        ("Fiorentina", "Lazio"), ("Hellas Verona", "Parma"), ("AC Milan", "Juventus"),
        ("Torino", "Monza"), ("Venezia", "Lecce"), ("Como", "Napoli"), ("Venezia", "Udinese")
    ],
    [
        ("Atalanta", "Fiorentina"), ("Empoli", "AC Milan"), ("Lazio", "Como"),
        ("Hellas Verona", "Udinese"), ("Internazionale", "Venezia"), ("Napoli", "Roma"),
        ("Torino", "Lecce"), ("Venezia", "Juventus"), ("Monza", "Cagliari"), ("Parma", "Bologna")
    ],
    [
        ("Atalanta", "Como"), ("Bologna", "Roma"), ("Fiorentina", "Venezia"),
        ("Lazio", "Parma"), ("AC Milan", "Cagliari"), ("Juventus", "Torino"),
        ("Udinese", "Empoli"), ("Lecce", "Internazionale"), ("Venezia", "Hellas Verona"), ("Monza", "Napoli")
    ],
    [
        ("Bologna", "Hellas Verona"), ("Cagliari", "AC Milan"), ("Roma", "Parma"),
        ("Empoli", "Torino"), ("Internazionale", "Monza"), ("Juventus", "Atalanta"),
        ("Udinese", "Venezia"), ("Venezia", "Fiorentina"), ("Lecce", "Napoli"), ("Como", "Lazio")
    ],
    [
        ("Roma", "Lazio"), ("Fiorentina", "Udinese"), ("Hellas Verona", "Juventus"),
        ("Internazionale", "Venezia"), ("Napoli", "Atalanta"), ("Torino", "Bologna"),
        ("Como", "Lecce"), ("Venezia", "Cagliari"), ("Monza", "Empoli"), ("Parma", "AC Milan")
    ],
    [
        ("Cagliari", "Monza"), ("Fiorentina", "Roma"), ("Lazio", "Hellas Verona"),
        ("AC Milan", "Atalanta"), ("Juventus", "Bologna"), ("Napoli", "Como"),
        ("Udinese", "Internazionale"), ("Venezia", "Torino"), ("Lecce", "Empoli"), ("Parma", "Venezia")
    ],
    [
        ("Atalanta", "Roma"), ("Bologna", "Lecce"), ("Cagliari", "Venezia"),
        ("Empoli", "Fiorentina"), ("Lazio", "Napoli"), ("Hellas Verona", "Venezia"),
        ("Internazionale", "Parma"), ("Juventus", "Como"), ("Monza", "Torino"), ("AC Milan", "Udinese")
    ],
    [
        ("Atalanta", "Venezia"), ("Bologna", "Empoli"), ("Cagliari", "Lazio"),
        ("Roma", "AC Milan"), ("Fiorentina", "Como"), ("Internazionale", "Hellas Verona"),
        ("Juventus", "Parma"), ("Napoli", "Monza"), ("Torino", "Venezia"), ("Lecce", "Udinese")
    ],
    [
        ("Bologna", "Fiorentina"), ("Cagliari", "Roma"), ("Empoli", "Internazionale"),
        ("Lazio", "Venezia"), ("Hellas Verona", "Napoli"), ("AC Milan", "Monza"),
        ("Juventus", "Lecce"), ("Venezia", "Atalanta"), ("Como", "Parma"), ("Torino", "Udinese")
    ],
    [
        ("Atalanta", "Empoli"), ("Fiorentina", "Juventus"), ("Lazio", "Monza"),
        ("AC Milan", "Como"), ("Internazionale", "Cagliari"), ("Napoli", "Parma"),
        ("Udinese", "Venezia"), ("Venezia", "Bologna"), ("Lecce", "Roma"), ("Torino", "Hellas Verona")
    ],
    [
        ("Bologna", "Atalanta"), ("Cagliari", "Napoli"), ("Empoli", "AC Milan"),
        ("Roma", "Internazionale"), ("Fiorentina", "Monza"), ("Juventus", "Lazio"),
        ("Venezia", "Udinese"), ("Venezia", "Lecce"), ("Como", "Hellas Verona"), ("Parma", "Torino")
    ],
    [
        ("Atalanta", "Fiorentina"), ("Bologna", "Roma"), ("Cagliari", "Juventus"),
        ("Empoli", "Lazio"), ("Hellas Verona", "Napoli"), ("AC Milan", "Torino"),
        ("Internazionale", "Como"), ("Venezia", "Monza"), ("Lecce", "Venezia"), ("Parma", "Udinese")
    ],
    [
        ("Atalanta", "Cagliari"), ("Fiorentina", "Napoli"), ("Lazio", "Hellas Verona"),
        ("AC Milan", "Juventus"), ("Roma", "Venezia"), ("Internazionale", "Torino"),
        ("Udinese", "Bologna"), ("Venezia", "Empoli"), ("Como", "Lecce"), ("Monza", "Parma")
    ],
    [
        ("Bologna", "AC Milan"), ("Cagliari", "Lecce"), ("Empoli", "Atalanta"),
        ("Fiorentina", "Lazio"), ("Hellas Verona", "Internazionale"), ("Juventus", "Venezia"),
        ("Napoli", "Monza"), ("Udinese", "Venezia"), ("Como", "Roma"), ("Parma", "Torino")
    ],
    [
        ("Atalanta", "Venezia"), ("Bologna", "Torino"), ("Cagliari", "Empoli"),
        ("Fiorentina", "Roma"), ("Lazio", "Napoli"), ("Hellas Verona", "Lecce"),
        ("AC Milan", "Venezia"), ("Internazionale", "Juventus"), ("Como", "Monza"), ("Parma", "Udinese")
    ]
]




# Initialize dictionaries to count home and away matches
home_matches = defaultdict(lambda: defaultdict(int))
away_matches = defaultdict(lambda: defaultdict(int))

# Process the matches
for matchday in matchdays:
    for home, away in matchday:
        home_matches[home][away] += 1
        away_matches[away][home] += 1

# Check the match counts
all_good = True
teams = set(home_matches.keys()).union(set(away_matches.keys()))
for team in teams:
    for opponent in teams:
        if team != opponent:
            if home_matches[team][opponent] != 1 or away_matches[team][opponent] != 1:
                all_good = False
                print(f"Discrepancy found: {team} vs {opponent} - Home: {home_matches[team][opponent]}, Away: {away_matches[team][opponent]}")

if all_good:
    print("Every team plays against every other team exactly twice, once at home and once away.")
else:
    print("There are discrepancies in the schedule.")
