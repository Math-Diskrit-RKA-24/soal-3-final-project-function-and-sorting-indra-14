PlayerList = []

Player = dict(name="",
              score=0,
              damage=0,
              health=100,
              defensePower=0,
              defense=False)

def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name, damage=0, defensePower=0):
    return {
        'name': name,
        'score': 0,
        'damage': damage,
        'health': 100,
        'defensePower': defensePower,
        'defense': False
    }

def addPlayer(player):
    PlayerList.append(player)

def removePlayer(name):
    global PlayerList
    PlayerList[:] = [player for player in PlayerList if player['name'] != name]
    if all(player['name'] != name for player in PlayerList):
        print("There is no player with that name!")

def setPlayer(player, key, value):
    if key in player:
        player[key] = value

def attackPlayer(attacker, target):
    damage_taken = max(0, attacker['damage'] - target['defensePower']) if target['defense'] else attacker['damage']
    new_health = max(0, target['health'] - damage_taken)
    new_score = attacker['score'] + (0.8 if target['defense'] else 1)
    
    setPlayer(attacker, 'score', new_score)
    setPlayer(target, 'health', new_health)
    setPlayer(target, 'defense', False)

def displayMatchResult():
    global PlayerList
    sorted_players = sorted(PlayerList, key=lambda x: (x['score'], x['health']), reverse=True)
    
    for idx, player in enumerate(sorted_players, start=1):
        print(f"Rank {idx}: {player['name']} | Score: {player['score']} | Health: {player['health']}")