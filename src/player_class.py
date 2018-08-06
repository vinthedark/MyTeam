import json

def select_team():
    with open('../properties/players.json') as d:
        players_list = json.load(d)
    non_selected = [player for player in players_list if player]
    for non in non_selected:
        print non

if __name__ == "__main__":
    select_team()
