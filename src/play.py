import game as m

def inputPlayerData():
    try:
        num_players = int(input("Enter the number of players: "))
        for _ in range(num_players):
            name = input("Enter player name: ")
            damage = int(input(f"Enter damage for {name}: "))
            defensePower = int(input(f"Enter defense power for {name}: "))
            player = m.createNewPlayer(name, damage, defensePower)
            m.addPlayer(player)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        inputPlayerData()

def playRound(player_idx=0):
    alive_players = [p for p in m.PlayerList if p['health'] > 0]

    if len(alive_players) == 1:
        print(f"\nWinner: {alive_players[0]['name']}! Congratulations!")
        return

    if player_idx >= len(alive_players):
        print("\n--- End of Round ---")
        playRound()
        return

    player = alive_players[player_idx]
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
            target = next((p for p in alive_players if p['name'] == target_name), None)
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
    print("\n====--------- Let the battle begin! ------------==")
    playRound()

if __name__ == "__main__":
    main()