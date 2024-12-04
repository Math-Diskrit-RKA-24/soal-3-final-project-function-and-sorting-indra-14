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
    pemain_update = [player for player in PlayerList if player['name'] != name]
    if len(pemain_update) == len(PlayerList):
        print("There is no player with that name!")
    PlayerList[:] = pemain_update

def setPlayer(player, key, value):
    if key in player:
        player[key] = value

def attackPlayer(attacker, target):
    if target['defense'] == True:
        targetHealth = target.get("health") - attacker.get("damage") + target.get("defensePower")
        attackScore = round(attacker.get("score") + 1 - 1 / target["defensePower"], 2)
    else:
        targetHealth = target.get("health") - attacker.get("damage")
        attackScore = attacker.get("score") + 1 

    setPlayer(attacker, 'score', attackScore)
    setPlayer(target, 'health', max(0, targetHealth))
    setPlayer(target, 'defense', False) 

def displayMatchResult():
    global PlayerList
    sorted_players = sorted(PlayerList, key=lambda x: (x['score'], x['health']), reverse=True)
    
    for idx, player in enumerate(sorted_players, start=1):
        print(f"Rank {idx}: {player['name']} | Score: {player['score']} | Health: {player['health']}")