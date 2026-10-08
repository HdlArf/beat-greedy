from challenge.strategy import choose_sets

UNIVERSE = set(range(1, 13))
SETS = {
    "A": ({1, 2, 3, 4}, 4),
    "B": ({4, 5, 6, 7}, 4),
    "C": ({7, 8, 9}, 3),
    "D": ({9, 10, 11, 12}, 4),
    "E": ({1, 5, 8, 10}, 4),
    "F": ({2, 6, 9, 11}, 4),
    "G": ({3, 7, 12}, 3),
}

def greedy():
    uncovered, chosen, total = set(UNIVERSE), [], 0
    while uncovered:
        best = max(
            (n for n in SETS if n not in chosen),
            key=lambda n: (len(SETS[n][0] & uncovered) / SETS[n][1],
                           len(SETS[n][0] & uncovered))
        )
        chosen.append(best)
        total += SETS[best][1]
        uncovered -= SETS[best][0]
    return chosen, total

def evaluate(chosen):
    covered, total = set(), 0
    for n in chosen:
        if n not in SETS:
            return False, float("inf")
        covered |= SETS[n][0]
        total += SETS[n][1]
    return covered == UNIVERSE, total

baseline, base_score = greedy()
yours = choose_sets(UNIVERSE, SETS)
valid, score = evaluate(yours)

print("\n" + "="*42)
print("HΛDΞL MICRO LAB #01 — BEAT GREEDY")
print("="*42)
print(f"GREEDY : {baseline} | score = {base_score}")
if valid:
    print(f"YOU    : {yours} | score = {score}")
    print("RESULT :", "YOU BEAT THE MACHINE." if score < base_score
          else "TIE. TRY AGAIN." if score == base_score
          else "GREEDY WINS. TRY AGAIN.")
else:
    print(f"YOU    : {yours}")
    print("RESULT : INVALID — FULL COVERAGE REQUIRED.")
print("="*42)
