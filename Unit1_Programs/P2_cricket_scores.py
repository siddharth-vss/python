# Practice Q2. Dictionary of cricket players' names and scores
# Accept player names & scores, then retrieve score by player name

# Create an empty dictionary
players = {}

# Accept player names and scores
n = int(input("Enter number of players: "))
for i in range(n):
    name = input("Enter player name: ")
    score = int(input("Enter score: "))
    players[name] = score

# Display dictionary
print("\nPlayers and Scores:")
print(players)

# Retrieve runs by entering player's name
search_name = input("\nEnter player name to find score: ")
if search_name in players:
    print(search_name, "scored", players[search_name], "runs.")
else:
    print("Player not found.")

# -------Output-------
# Enter number of players: 3
# Enter player name: Virat
# Enter score: 82
# Enter player name: Rohit
# Enter score: 56
# Enter player name: Dhoni
# Enter score: 44
#
# Players and Scores:
# {'Virat': 82, 'Rohit': 56, 'Dhoni': 44}
#
# Enter player name to find score: Rohit
# Rohit scored 56 runs.
