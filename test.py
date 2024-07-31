import pymprog as pm
import random
import re

# Teams that are in the Serie A league (using 2023-2024 teams)
teams = [
    "ATA",  # Atalanta
    "BOL",  # Bologna
    "CAG",  # Cagliari
    "EMP",  # Empoli
    "FIO",  # Fiorentina
    "VER",  # H. Verona
    "INT",  # Inter Milan
    "JUV",  # Juventus
    "LAZ",  # Lazio
    "LEC",  # Lecce
    "MIL",  # AC Milan
    "MON",  # Monza
    "NAP",  # Napoli
    "ROM",  # Roma
    "SAL",  # Salernitana
    "GEN",  # Genoa
    "SAS",  # Sassuolo
    "FRO",  # Spezia
    "TOR",  # Torino
    "UDI"   # Udinese
]

# HOME = 0, AWAY = 1
# Creating many patterns for the round-robin tournament
def create_patterns(num_patterns, pattern_length):
    patterns = []
    for _ in range(num_patterns):
        pattern = [random.randint(0, 1) for _ in range(pattern_length)]
        patterns.append(pattern)
    return patterns



def count_breaks(pattern):
    breaks = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[i - 1]:
            breaks += 1
    return breaks

def filter_and_fix_patterns(patterns):
    filtered_patterns = []
    for pattern in patterns:
        fixed_pattern = pattern.copy()
        for i in range(len(fixed_pattern) - 2):
            if fixed_pattern[i] == fixed_pattern[i + 1] == fixed_pattern[i + 2]:
                fixed_pattern[i + 1] = 1 - fixed_pattern[i + 1]  # Flip the value
        
        if count_breaks(fixed_pattern) < 5:
            filtered_patterns.append(fixed_pattern)
    return filtered_patterns

def find_pair_patterns(patterns):
    pair_patterns = []
    for i in range(len(patterns) - 1):
        for j in range(i + 1, len(patterns)):
            if all(patterns[i][k] != patterns[j][k] for k in range(len(patterns[i]))):
                pair_patterns.append((i, j))
                break
    return pair_patterns

def minimizeBreaks(filtered_patterns,pattern_pairs):
    num_patterns = len(filtered_patterns)
    
    # Initialize the model
    model = pm.model('Minimize Breaks')
    
    x = model

num_teams = len(teams)
pattern_length = 2*(num_teams - 1)
patterns = create_patterns(10000, pattern_length)
filtered_patterns = filter_and_fix_patterns(patterns)
pattern_pairs = find_pair_patterns(filtered_patterns)
b = minimizeBreaks(filtered_patterns,pattern_pairs)
print("Number of patterns after filtering:", len(filtered_patterns))
print("Number of pair patterns:", len(pattern_pairs))
print("First 5 pair patterns:", pattern_pairs)
print(filtered_patterns[:10])
