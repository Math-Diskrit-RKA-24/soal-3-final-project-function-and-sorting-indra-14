PlayerList = []

def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name: str, damage: int, defensePower: int):
    Player = dict(
        name='',
        score=0,
        damage=0,
        health=100,
        defensePower=0,
        defense=False
    )
    return Player

def addPlayer(player):
    global PlayerList
    PlayerList.append(player)

def removePlayer(name: str):
    global PlayerList
    for player in PlayerList:
        if player["name"] == name:
            PlayerList.remove(player)
            return
    print("There is no player with that name!")

def setPlayer(player: dict, key: str, value):
    if key in player:
        player[key] = value
    else:
        print(f"'{key}' is not in player attributes!")

def attackPlayer(attacker: dict, target: dict):
    if target["defense"]:
        damage_dealt = max(0, attacker["damage"] - target["defensePower"])
    else:
        damage_dealt = attacker["damage"]
    
    setPlayer(target, "health", max(0, target["health"] - damage_dealt))
    setPlayer(attacker, "score", attacker["score"] + damage_dealt)
    setPlayer(target, "defense", False)

def displayMatchResult():
    global PlayerList
    sorted_players = sorted(PlayerList, key=lambda x: (-x["score"], -x["health"]))
    
    print("Match Results:")
    for rank, player in enumerate(sorted_players, start=1):
        print(f"Rank: {rank}:  {player['name']} | Score: {player['score']} | Health: {player['health']}")