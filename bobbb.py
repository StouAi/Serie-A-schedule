from collections import defaultdict

# List of matchdays
matchdays = [
    [
        ("Atalanta", "Venezia"), ("Bologna", "Cagliari"), ("Fiorentina", "Empoli"),
        ("Genoa", "AC Milan"), ("Hellas Verona", "Lazio"), ("Lecce", "Como"),
        ("Napoli", "Internazionale"), ("Roma", "Parma"), ("Torino", "Monza"), ("Udinese", "Juventus")
    ],
    [
        ("Empoli", "Bologna"), ("Fiorentina", "Como"), ("Genoa", "Juventus"),
        ("Hellas Verona", "Roma"), ("Lazio", "AC Milan"), ("Lecce", "Internazionale"),
        ("Monza", "Udinese"), ("Parma", "Napoli"), ("Torino", "Atalanta"), ("Venezia", "Cagliari")
    ],
    [
        ("Bologna", "Internazionale"), ("Empoli", "Hellas Verona"), ("Genoa", "Como"),
        ("Lazio", "Torino"), ("Lecce", "Cagliari"), ("AC Milan", "Fiorentina"),
        ("Monza", "Juventus"), ("Parma", "Atalanta"), ("Roma", "Udinese"), ("Venezia", "Napoli")
    ],
    [
        ("Bologna", "Fiorentina"), ("Empoli", "Napoli"), ("Genoa", "Atalanta"),
        ("Internazionale", "Cagliari"), ("Juventus", "Lazio"), ("Lecce", "Monza"),
        ("Parma", "AC Milan"), ("Roma", "Como"), ("Torino", "Hellas Verona"), ("Udinese", "Venezia")
    ],
    [
        ("Atalanta", "Roma"), ("Empoli", "Internazionale"), ("Fiorentina", "Genoa"),
        ("Hellas Verona", "Udinese"), ("Lazio", "Bologna"), ("Lecce", "Napoli"),
        ("AC Milan", "Juventus"), ("Monza", "Como"), ("Parma", "Cagliari"), ("Venezia", "Torino")
    ],
    [
        ("Bologna", "Lecce"), ("Cagliari", "Udinese"), ("Empoli", "Como"),
        ("Genoa", "Torino"), ("Hellas Verona", "Parma"), ("Juventus", "Atalanta"),
        ("Monza", "Internazionale"), ("Napoli", "Fiorentina"), ("Roma", "Lazio"), ("Venezia", "AC Milan")
    ],
    [
        ("Atalanta", "Hellas Verona"), ("Bologna", "Torino"), ("Como", "Cagliari"),
        ("Empoli", "Lazio"), ("Genoa", "Lecce"), ("Juventus", "Fiorentina"),
        ("AC Milan", "Internazionale"), ("Monza", "Roma"), ("Udinese", "Napoli"), ("Venezia", "Parma")
    ],
    [
        ("Atalanta", "Lazio"), ("Bologna", "Monza"), ("Empoli", "Juventus"),
        ("Genoa", "Hellas Verona"), ("Lecce", "AC Milan"), ("Napoli", "Cagliari"),
        ("Parma", "Fiorentina"), ("Torino", "Como"), ("Udinese", "Internazionale"), ("Venezia", "Roma")
    ],
    [
        ("Atalanta", "Como"), ("Bologna", "Udinese"), ("Cagliari", "Fiorentina"),
        ("Empoli", "Parma"), ("Genoa", "Napoli"), ("Hellas Verona", "Lecce"),
        ("Monza", "Lazio"), ("Roma", "AC Milan"), ("Torino", "Juventus"), ("Venezia", "Internazionale")
    ],
    [
        ("Atalanta", "Monza"), ("Bologna", "AC Milan"), ("Empoli", "Cagliari"),
        ("Genoa", "Parma"), ("Hellas Verona", "Fiorentina"), ("Internazionale", "Como"),
        ("Juventus", "Napoli"), ("Lazio", "Venezia"), ("Roma", "Lecce"), ("Udinese", "Torino")
    ],
    [
        ("Atalanta", "Napoli"), ("Bologna", "Como"), ("Cagliari", "AC Milan"),
        ("Hellas Verona", "Internazionale"), ("Lazio", "Fiorentina"), ("Lecce", "Juventus"),
        ("Monza", "Parma"), ("Torino", "Roma"), ("Udinese", "Empoli"), ("Venezia", "Genoa")
    ],
    [
        ("Atalanta", "Fiorentina"), ("Bologna", "Hellas Verona"), ("Como", "Juventus"),
        ("Empoli", "Torino"), ("Lecce", "Venezia"), ("AC Milan", "Udinese"),
        ("Monza", "Cagliari"), ("Napoli", "Lazio"), ("Parma", "Internazionale"), ("Roma", "Genoa")
    ],
    [
        ("Cagliari", "Hellas Verona"), ("Fiorentina", "Monza"), ("Internazionale", "Atalanta"),
        ("Juventus", "Venezia"), ("Lazio", "Genoa"), ("AC Milan", "Empoli"),
        ("Napoli", "Torino"), ("Parma", "Como"), ("Roma", "Bologna"), ("Udinese", "Lecce")
    ],
    [
        ("Bologna", "Atalanta"), ("Cagliari", "Juventus"), ("Como", "Lazio"),
        ("Empoli", "Monza"), ("Hellas Verona", "AC Milan"), ("Parma", "Lecce"),
        ("Roma", "Napoli"), ("Torino", "Internazionale"), ("Udinese", "Genoa"), ("Venezia", "Fiorentina")
    ],
    [
        ("Atalanta", "Cagliari"), ("Bologna", "Venezia"), ("Como", "AC Milan"),
        ("Fiorentina", "Roma"), ("Genoa", "Internazionale"), ("Juventus", "Hellas Verona"),
        ("Lazio", "Udinese"), ("Lecce", "Empoli"), ("Monza", "Napoli"), ("Parma", "Torino")
    ],
    [
        ("Empoli", "Roma"), ("Genoa", "Cagliari"), ("Hellas Verona", "Monza"),
        ("Internazionale", "Lazio"), ("Lecce", "Atalanta"), ("AC Milan", "Torino"),
        ("Napoli", "Bologna"), ("Parma", "Juventus"), ("Udinese", "Fiorentina"), ("Venezia", "Como")
    ],
    [
        ("Bologna", "Genoa"), ("Cagliari", "Lazio"), ("Empoli", "Atalanta"),
        ("Internazionale", "Fiorentina"), ("Lecce", "Torino"), ("AC Milan", "Monza"),
        ("Napoli", "Como"), ("Parma", "Udinese"), ("Roma", "Juventus"), ("Venezia", "Hellas Verona")
    ],
    [
        ("Empoli", "Venezia"), ("Genoa", "Monza"), ("Hellas Verona", "Como"),
        ("Internazionale", "Juventus"), ("Lecce", "Lazio"), ("AC Milan", "Napoli"),
        ("Parma", "Bologna"), ("Roma", "Cagliari"), ("Torino", "Fiorentina"), ("Udinese", "Atalanta")
    ],
    [
        ("Bologna", "Juventus"), ("Cagliari", "Torino"), ("Como", "Udinese"),
        ("Empoli", "Genoa"), ("Hellas Verona", "Napoli"), ("Lazio", "Parma"),
        ("Lecce", "Fiorentina"), ("AC Milan", "Atalanta"), ("Monza", "Venezia"), ("Roma", "Internazionale")
    ],
    [
        ("Atalanta", "Empoli"), ("Fiorentina", "Hellas Verona"), ("Internazionale", "Genoa"),
        ("Juventus", "Monza"), ("Lazio", "Cagliari"), ("Lecce", "Bologna"),
        ("Napoli", "AC Milan"), ("Parma", "Roma"), ("Torino", "Venezia"), ("Udinese", "Como")
    ],
    [
        ("Atalanta", "AC Milan"), ("Cagliari", "Parma"), ("Empoli", "Lecce"),
        ("Hellas Verona", "Genoa"), ("Juventus", "Como"), ("Lazio", "Internazionale"),
        ("Napoli", "Monza"), ("Roma", "Fiorentina"), ("Torino", "Udinese"), ("Venezia", "Bologna")
    ],
    [
        ("Atalanta", "Juventus"), ("Bologna", "Empoli"), ("Cagliari", "Internazionale"),
        ("Como", "Venezia"), ("Fiorentina", "Udinese"), ("Lazio", "Lecce"),
        ("Monza", "Genoa"), ("Napoli", "Roma"), ("Parma", "Hellas Verona"), ("Torino", "AC Milan")
    ],
    [
        ("Atalanta", "Udinese"), ("Bologna", "Napoli"), ("Cagliari", "Venezia"),
        ("Como", "Lecce"), ("Fiorentina", "Juventus"), ("Internazionale", "Empoli"),
        ("AC Milan", "Lazio"), ("Parma", "Monza"), ("Roma", "Hellas Verona"), ("Torino", "Genoa")
    ],
    [
        ("Cagliari", "Roma"), ("Fiorentina", "Venezia"), ("Genoa", "Udinese"),
        ("Hellas Verona", "Empoli"), ("Internazionale", "Parma"), ("Juventus", "Bologna"),
        ("Lazio", "Napoli"), ("AC Milan", "Como"), ("Monza", "Atalanta"), ("Torino", "Lecce")
    ],
    [
        ("Cagliari", "Atalanta"), ("Fiorentina", "Napoli"), ("Juventus", "Internazionale"),
        ("Lazio", "Como"), ("Lecce", "Hellas Verona"), ("AC Milan", "Genoa"),
        ("Parma", "Venezia"), ("Roma", "Monza"), ("Torino", "Empoli"), ("Udinese", "Bologna")
    ],
    [
        ("Cagliari", "Napoli"), ("Como", "Atalanta"), ("Fiorentina", "AC Milan"),
        ("Genoa", "Bologna"), ("Hellas Verona", "Juventus"), ("Internazionale", "Monza"),
        ("Parma", "Empoli"), ("Roma", "Torino"), ("Udinese", "Lazio"), ("Venezia", "Lecce")
    ],
    [
        ("Atalanta", "Torino"), ("Bologna", "Lazio"), ("Como", "Monza"),
        ("Empoli", "AC Milan"), ("Fiorentina", "Cagliari"), ("Internazionale", "Hellas Verona"),
        ("Lecce", "Roma"), ("Napoli", "Udinese"), ("Parma", "Genoa"), ("Venezia", "Juventus")
    ],
    [
        ("Cagliari", "Bologna"), ("Como", "Napoli"), ("Empoli", "Fiorentina"),
        ("Hellas Verona", "Atalanta"), ("Internazionale", "AC Milan"), ("Juventus", "Roma"),
        ("Lecce", "Genoa"), ("Monza", "Torino"), ("Udinese", "Parma"), ("Venezia", "Lazio")
    ],
    [
        ("Cagliari", "Lecce"), ("Como", "Hellas Verona"), ("Fiorentina", "Atalanta"),
        ("Genoa", "Venezia"), ("Internazionale", "Bologna"), ("Lazio", "Empoli"),
        ("AC Milan", "Roma"), ("Napoli", "Juventus"), ("Torino", "Parma"), ("Udinese", "Monza")
    ],
    [
        ("Como", "Torino"), ("Fiorentina", "Parma"), ("Genoa", "Lazio"),
        ("Internazionale", "Roma"), ("Juventus", "Lecce"), ("AC Milan", "Hellas Verona"),
        ("Monza", "Bologna"), ("Napoli", "Atalanta"), ("Udinese", "Cagliari"), ("Venezia", "Empoli")
    ],
    [
        ("Atalanta", "Lecce"), ("Bologna", "Parma"), ("Como", "Internazionale"),
        ("Fiorentina", "Torino"), ("Genoa", "Roma"), ("Hellas Verona", "Cagliari"),
        ("Juventus", "AC Milan"), ("Lazio", "Monza"), ("Napoli", "Empoli"), ("Venezia", "Udinese")
    ],
    [
        ("Atalanta", "Parma"), ("Cagliari", "Como"), ("Fiorentina", "Lazio"),
        ("Hellas Verona", "Bologna"), ("Internazionale", "Torino"), ("Juventus", "Genoa"),
        ("AC Milan", "Venezia"), ("Monza", "Empoli"), ("Napoli", "Lecce"), ("Udinese", "Roma")
    ],
    [
        ("Cagliari", "Genoa"), ("Como", "Empoli"), ("Fiorentina", "Lecce"),
        ("Hellas Verona", "Venezia"), ("Internazionale", "Napoli"), ("Juventus", "Udinese"),
        ("Monza", "AC Milan"), ("Parma", "Lazio"), ("Roma", "Atalanta"), ("Torino", "Bologna")
    ],
    [
        ("Como", "Parma"), ("Fiorentina", "Bologna"), ("Internazionale", "Lecce"),
        ("Juventus", "Empoli"), ("Lazio", "Atalanta"), ("Monza", "Hellas Verona"),
        ("Napoli", "Genoa"), ("Roma", "Venezia"), ("Torino", "Cagliari"), ("Udinese", "AC Milan")
    ],
    [
        ("Atalanta", "Internazionale"), ("Bologna", "Roma"), ("Cagliari", "Monza"),
        ("Como", "Fiorentina"), ("Genoa", "Empoli"), ("Juventus", "Parma"),
        ("AC Milan", "Lecce"), ("Napoli", "Venezia"), ("Torino", "Lazio"), ("Udinese", "Hellas Verona")
    ],
    [
        ("Atalanta", "Bologna"), ("Como", "Genoa"), ("Internazionale", "Venezia"),
        ("Juventus", "Cagliari"), ("Lazio", "Hellas Verona"), ("Lecce", "Udinese"),
        ("AC Milan", "Parma"), ("Monza", "Fiorentina"), ("Roma", "Empoli"), ("Torino", "Napoli")
    ],
    [
        ("Atalanta", "Genoa"), ("Como", "Bologna"), ("Empoli", "Udinese"),
        ("Fiorentina", "Internazionale"), ("Juventus", "Torino"), ("Lazio", "Roma"),
        ("Lecce", "Parma"), ("AC Milan", "Cagliari"), ("Napoli", "Hellas Verona"), ("Venezia", "Monza")
    ],
    [
        ("Cagliari", "Empoli"), ("Como", "Roma"), ("Genoa", "Fiorentina"),
        ("Hellas Verona", "Torino"), ("Internazionale", "Udinese"), ("Lazio", "Juventus"),
        ("AC Milan", "Bologna"), ("Monza", "Lecce"), ("Napoli", "Parma"), ("Venezia", "Atalanta")
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
