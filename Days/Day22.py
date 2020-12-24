import time

def recursive_combat(deck1, deck2):
    previous_games = set()
    player1 = deck1.copy()
    player2 = deck2.copy()
    winner = None
    while not winner:
        if (tuple(player1), tuple(player2)) in previous_games:
            winner = 1
        else:
            previous_games.add((tuple(player1), tuple(player2)))
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            if card1 <= len(player1) and card2 <= len(player2):
                result = recursive_combat(player1[:card1], player2[:card2])[0]
                if result == 1:
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)
            else:
                if card1 > card2:
                    player1.append(card1)
                    player1.append(card2)
                else:
                    player2.append(card2)
                    player2.append(card1)
            if len(player1) == 0:
                winner = 2
            elif len(player2) == 0:
                winner = 1
    return winner, player1, player2

def main():
    start = time.time()

    # Execution time: 3.17s
    with open("Day22Input2.txt") as line:
        lines = line.read().strip().split("\n\n")
    player1 = list(map(int, lines[0].split('\n')[1:]))
    player2 = list(map(int, lines[1].split('\n')[1:]))
    
    result = recursive_combat(player1, player2)
    if result[0] == 1:
        winner = result[1]
    else:
        winner = result[2]

    score = 0
    for i, j in enumerate(winner):
        score += (50 - i) * int(j)
    print(score)

    end = time.time()
    print(f"Executiont time: {end - start}")

main()