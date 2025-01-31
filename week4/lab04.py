# Import the random library to use for the dice later
import random

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points


# Game
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# Define the number of stars awarded to the Player
num_stars = 0

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0

while i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted is a number between 1-6
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    # Break out of while loop if input was valid
    else:
        break

# Input was valid - broke out of while loop
combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

# Roll for weapon
input("Roll the dice for your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)

# Max out the combat strength at 6
combat_strength = min(6, (combat_strength + weaponRoll))
print("The hero\'s weapon is " + str(weapons[weaponRoll - 1]))

# Weapon Roll Analysis
input("Analyze the Weapon roll (Press enter)")
if weaponRoll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weaponRoll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if weapons[weaponRoll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(diceOptions)
print("Player rolled " + str(m_health_points) + " health points for the monster")

input("Analyze the roll (Press enter)")
# Compare Player vs Monster's strength
print("--- You are matched in strength: " + str(combat_strength == m_combat_strength))

# Check the Player's overall strength and health
print("--- You have a strong player: " + str((combat_strength + health_points) >= 15))

# Loop while the monster and the player are alive. Call fight sequence functions
print("You meet the monster. FIGHT!!")
while m_health_points > 0 and health_points > 0:

    input("You strike first (Press Enter)")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    if m_health_points == 0:
        num_stars = 3
    else:
        input("The monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

stars = "*" * num_stars
print("Hero gets <" + stars + "> stars")

# Q1. python dictionary for monster powers (handled like hero's weapon)
monster_powers = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}

# Q2. roll for random monster power
input("Roll the dice for the monster's power (Press enter)")
m_power_roll = random.choice(monster_powers)

# Q3. add monster power's value to monster's combat strength, cannot be more than 6
m_combat_strength += monster_powers[m_power_roll]
m_combat_strength = min(6, (m_combat_strength + 2))
print ("The monster's power is " + str(monster_powers.keys()[m_power_roll - 1]) + " and its combat strength is " + str(m_combat_strength))

# Q4. define new array called belt
belt = []

# Q5. print that Player has found a loot bag, prompt user for Enter key, roll for loot, remove from loot pool using pop(), add to belt array
input("You have found a loot bag. Press enter to open")
lootRoll = random.choice(range(1, len(loot_options) + 1))
loot = loot_options.pop(lootRoll - 1)
belt.append(loot)
print ("You have found a " + str(loot))

# Q6. collect second loot item (copy code, function will be covered in week5)
loot2Roll = random.choice(range(1, len(loot_options) + 1))
loot2 = loot_options.pop(loot2Roll - 1)
belt.append(loot2)
print ("You have found a " + str(loot2))

# Q7. print that belt is sorted A-Z, use sort() on belt array, print sorted belt
print ("Organizing belt, A-Z...")
belt.sort()
print ("Belt sorted: " + belt)

# Q8. print that the player can use a loot item, pop() out of belt and into variable, if loot is good, add +2HP up to max 6, if bad, drop -2HP down to min 0
print ("You see a monster, you can use a loot item!")
heldLootItem = belt.pop(0)
for i in range(0, len(good_loot_options) + 1):
    if heldLootItem == good_loot_options[i]:
        health_points = min(6, (health_points + 2))
    elif heldLootItem == bad_loot_options[i]:
        health_points = max(0, (health_points - 2))
    else:
        print ("It's not that helpful, you're better off just chucking it away")
        heldLootItem.pop()
    print ("You have used the " + heldLootItem + " and your health is now " + str(health_points) + "!")

# move the Questions (Q1-Q8) into the correct places in the code, i.e. loot before you fight the monster