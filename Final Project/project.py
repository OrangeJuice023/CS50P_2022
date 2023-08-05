import random

# Function to display the game introduction
def introduction():
    print("Welcome to the My Hero Academia RPG!")
    print("You are a young hero on a quest to protect the world from powerful villains.")
    print("Use your Quirk and courage to prevail!\n")

# Function to choose the player's hero name
def choose_hero_name():
    return input("Enter your Hero name: ")

# Function to fetch a random villain from the My Hero Academia universe (mock data)
def choose_villain():
    villains = ["Tomura Shigaraki", "Kurogiri", "Dabi", "Himiko Toga", "Stain"]
    return random.choice(villains)

# Function to simulate a battle between hero and villain
def battle(hero_name, villain_name, hero_level):
    hero_health = 100
    villain_health = random.randint(50, 100)
    hero_xp = 0

    print(f"A dangerous villain, {villain_name}, appears! Prepare for battle, {hero_name}!\n")

    while hero_health > 0 and villain_health > 0:
        print("1. Use Quirk")
        print("2. Evade and Counter")
        print("3. Use Healing Item")
        choice = int(input("Choose your action (1/2/3): "))

        if choice == 1:
            # Perform a Quirk attack with random damage based on hero's level
            hero_attack = random.randint(10, 20) + hero_level
            print(f"{hero_name} uses their Quirk against {villain_name} with {hero_attack} damage.")
            villain_health -= hero_attack
        elif choice == 2:
            # Introduce critical evasion: 20% chance to dodge and counter
            critical_evasion_chance = random.random()
            if critical_evasion_chance <= 0.2:
                hero_attack = random.randint(5, 15)
                print(f"{hero_name} evades the attack and counters with {hero_attack} damage.")
                villain_health -= hero_attack
            else:
                # Perform a regular villain attack based on hero's level
                villain_attack = random.randint(10, 20) + hero_level
                print(f"{villain_name} attacks {hero_name} with {villain_attack} damage.")
                hero_health -= villain_attack
        elif choice == 3:
            # Use a Healing Item to restore hero's health
            healing_item = random.randint(15, 25)
            hero_health = min(100, hero_health + healing_item)
            print(f"{hero_name} uses a Healing Item and restores {healing_item} health.")
        else:
            print("Invalid choice. You missed the turn.")

        if villain_health > 0:
            # Villain attacks hero with random damage
            villain_attack = random.randint(10, 20) + hero_level
            print(f"{villain_name} attacks {hero_name} with {villain_attack} damage.")
            hero_health -= villain_attack

            print(f"{hero_name}'s health: {hero_health}")
            print(f"{villain_name}'s health: {villain_health}\n")

    if hero_health > 0:
        # Hero wins the battle and earns XP
        xp_earned = random.randint(20, 40)
        hero_xp += xp_earned
        print(f"Congratulations, {hero_name}! You defeated {villain_name} and earned {xp_earned} XP!")
        return True, hero_xp
    else:
        print(f"{hero_name}, you were defeated by {villain_name}. Try again!")
        return False, hero_xp

# Function to explore a location in the My Hero Academia universe (mock data)
def explore(hero_name):
    locations = ["U.A. High School", "Kamino Ward", "Hosu City", "Musutafu City", "Kiyashi Ward"]
    location = random.choice(locations)
    print(f"{hero_name}, you are exploring {location}.")

# Function to check hero's level based on XP
def check_level(hero_xp):
    return hero_xp // 100 + 1

# Function to handle the final boss battle (mock data)
def final_boss_battle(hero_name, hero_level):
    boss_name = "All For One"
    boss_health = 150 + hero_level * 2

    print(f"The final battle begins! Defeat {boss_name} to save the world!\n")

    while boss_health > 0:
        print("1. Use Ultimate Quirk")
        print("2. Team-Up Attack")
        print("3. Use Healing Item")
        choice = int(input("Choose your action (1/2/3): "))

        if choice == 1:
            # Perform an Ultimate Quirk attack with random damage based on hero's level
            hero_attack = random.randint(20, 30) + hero_level
            print(f"{hero_name} uses their Ultimate Quirk against {boss_name} with {hero_attack} damage.")
            boss_health -= hero_attack
        elif choice == 2:
            # Perform a powerful Team-Up Attack with allies against the boss
            team_up_attack = random.randint(15, 25) + hero_level
            print(f"{hero_name} and their allies launch a Team-Up Attack with {team_up_attack} damage.")
            boss_health -= team_up_attack
        elif choice == 3:
            # Use a Healing Item to restore hero's health
            healing_item = random.randint(20, 30)
            hero_health = min(100, hero_health + healing_item)
            print(f"{hero_name} uses a Healing Item and restores {healing_item} health.")
        else:
            print("Invalid choice. You missed the turn.")

        if boss_health > 0:
            # Boss attacks hero with random damage
            boss_attack = random.randint(15, 30) + hero_level
            print(f"{boss_name} attacks {hero_name} with {boss_attack} damage.")
            hero_health -= boss_attack

            print(f"{hero_name}'s health: {hero_health}")
            print(f"{boss_name}'s health: {boss_health}\n")

        if hero_health <= 0:
            print(f"{hero_name}, you were defeated by {boss_name}. The world falls into darkness.")
            return False

    print(f"Congratulations, {hero_name}! You defeated {boss_name} and saved the world!")
    return True

# Main function to run the game
def main():
    introduction()
    name = choose_hero_name()
    hero_xp = 0

    while True:
        explore(name)
        villain = choose_villain()
        result, earned_xp = battle(name, villain, check_level(hero_xp))

        if result:
            hero_xp += earned_xp
            print(f"{name}, you leveled up to level {check_level(hero_xp)}!\n")

        if check_level(hero_xp) >= 10:
            final_boss_result = final_boss_battle(name, check_level(hero_xp))
            if not final_boss_result:
                break

        choice = input("Do you want to continue your hero journey? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
