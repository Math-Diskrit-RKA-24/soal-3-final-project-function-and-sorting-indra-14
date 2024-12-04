import game as m
import random

heal_given = False
healed_player = None

def inputPlayerData():
    define_players = [
        {"name": "Adan", "damage": 20, "defensePower": 10},
        {"name": "negnaK", "damage": 15, "defensePower": 12},
        {"name": "sutuP", "damage": 25, "defensePower": 8},
        {"name": "?koY", "damage": 18, "defensePower": 15}
    ]
    for playerData in define_players:
        player = m.createNewPlayer(playerData['name'], playerData['damage'], playerData['defensePower'])
        m.addPlayer(player)
        print(f"\n{playerData['name']} joined the game!")

def random_heal_once(players):
    global heal_given, healed_player
    if not heal_given:
        healed_player = random.choice(players)
        healed_player['health'] += 50
        heal_given = True
        print(f"\n{healed_player['name']} received an instant heal of +50 health!")
        print(f"{healed_player['name']}'s health is now {healed_player['health']}.")

def playRound(player_idx=0):
    player_hidup = [p for p in m.PlayerList if p['health'] > 0]

    if len(player_hidup) == 1:
        print(f"\nWinner: {player_hidup[0]['name']}! Congratulations!")
        m.displayMatchResult()
        return

    if player_idx == 0:  # Panggil hanya sekali di awal
        random_heal_once(player_hidup)

    if player_idx >= len(player_hidup):
        print("\n--- End of Round ---")
        playRound()
        return

    player = player_hidup[player_idx]
    print(f"\n{player['name']}'s turn!")

    if player['health'] <= 30:
        heal_choice = input(f"{player['name']}, your health is low ({player['health']}). Heal 15 health but lose 10 damage? (yes/no): ").lower()
        if heal_choice == "yes":
            player['health'] += 15
            player['damage'] -= 10
            if player['damage'] <= 0:
                print(f"{player['name']}'s damage is too low! {player['name']} has killed themselves!")
                player['health'] = 0

    action = input("Choose action (attack/defense): ").lower()
    if action in ("defense", "d"):
        m.setPlayer(player, 'defense', True)
        print(f"{player['name']} is now in defensive mode.")
    elif action in ("attack", "a"):
        while True:
            target_name = input("Enter the name of the target player: ")
            target = next((p for p in player_hidup if p['name'] == target_name), None)
            if target:
                if target['name'] == player['name']:
                    print("You cannot attack yourself! Please choose another target.")
                    continue
                m.attackPlayer(player, target)
                print(f"{player['name']} attacked {target['name']}!")
                print(f"{target['name']} now has {target['health']} health.")
                break
            else:
                print("Invalid target! Please try again.")
    playRound(player_idx + 1)

def main():
    print("\n==----- Welcome to the Battle Royale Game! -----==")
    m.initPlayers()
    inputPlayerData()
    print("\n====--------- Let the battle begin! -----------===")
    playRound()

if __name__ == "__main__":
    main()
