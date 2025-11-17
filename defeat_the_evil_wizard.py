import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power, heal_power=15, spcl_ability_names=None, status_effects=None):
        self.name = name
        self.health = health
        self.heal_power = heal_power
        self.attack_power = attack_power
        self.max_health = health  
        
        # If no list is provided, create a new empty one
        if spcl_ability_names is None:
            self.spcl_ability_names = []
        else:
            self.spcl_ability_names = spcl_ability_names
            
        # Do the same for status_effects
        if status_effects is None:
            self.status_effects = []
        else:
            self.status_effects = status_effects

    def attack(self, opponent):
        min_damage = int(self.attack_power * 0.8)
        max_damage = int(self.attack_power * 1.2)
            
        if min_damage < 1:
            min_damage = 1

        damage = random.randint(min_damage, max_damage)
        
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            
    def special_ability(self, opponent, option):
        pass  # To be overridden by subclasses
    
    def heal(self):
        heal_amount = self.heal_power
        if self.health == self.max_health:
            print(f"{self.name} is already at full health!")
        else:
            self.health += heal_amount
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, heal_power=20, spcl_ability_names=["Power Strike", "Shield Block"])
        
    def power_strike(self, opponent):
        print(f"{self.name} uses Power Strike!")
        damage = int(self.attack_power * 1.5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
    def shield_block(self):
        print(f"{self.name} uses Shield Block! They will block the next attack.")
        self.status_effects.append("block")
        
    def special_ability(self, opponent, option):
        if option == "1":
            self.power_strike(opponent)
        elif option == "2":
            self.shield_block()
        else:
            print("Invalid special ability choice.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, spcl_ability_names=["Fireball", "Teleport"])
        
    def fireball(self, opponent):
        print(f"{self.name} casts Fireball!")
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
    def teleport(self):
        print(f"{self.name} uses Teleport! They avoid the next attack.")
        self.status_effects.append("evade")
        
    def special_ability(self, opponent, option):
        if option == "1":
            self.fireball(opponent)
        elif option == "2":
            self.teleport()
        else:
            print("Invalid special ability choice.")
        
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20, heal_power=20, spcl_ability_names=["Quick Shot", "Evade"])
         
    def quick_shot(self, opponent):
        print(f"{self.name} uses Quick Shot!")
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
    def evade(self):
        print(f"{self.name} uses Evade! They will evade the next attack.")
        self.status_effects.append("evade")
        
    def special_ability(self, opponent, option):
        if option == "1":
            self.quick_shot(opponent)
        elif option == "2":
            self.evade()
        else:
            print("Invalid special ability choice.")
        
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=15, heal_power=25, spcl_ability_names=["Holy Strike", "Divine Shield"])
        
    def holy_strike(self, opponent):
        print(f"{self.name} uses Holy Strike!")
        damage = int(self.attack_power * 1.5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
    def divine_shield(self):
        print(f"{self.name} uses Divine Shield! They will block the next attack.")
        self.status_effects.append("block")
        
    def special_ability(self, opponent, option):
        if option == "1":
            self.holy_strike(opponent)
        elif option == "2":
            self.divine_shield()
        else:
            print("Invalid special ability choice.")
        
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15,)
        
    def attack(self, opponent):
        print(f"{self.name} is attempting to attack {opponent.name}...")
        if self.check_evade(opponent):
            return
        if self.check_block(opponent):
            return
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated by the evil wizard {self.name}!")
            
    def check_evade(self, opponent):
        if "evade" in opponent.status_effects:
            print(f"{opponent.name} evades the attack!")
            opponent.status_effects.remove("evade")
            return True
        return False        
    
    def check_block(self, opponent):
        if "block" in opponent.status_effects:
            print(f"{opponent.name} blocks the attack!")
            opponent.status_effects.remove("block")
            return True
        return False

    def regenerate(self):
        if self.health == self.max_health:
            print(f"{self.name} is at full health!")
        elif self.health < self.max_health:
            if self.health + 5 > self.max_health:
                self.health = self.max_health
                print(f"{self.name} regenerates to max health! Current health: {self.health}")
            else:
                self.health += 5
                print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        else:
            print(f"{self.name} cannot regenerate health beyond max health.")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            option = (input(f"--- {player.name}'s special abilities are ---\n1. {player.spcl_ability_names[0]}\n2. {player.spcl_ability_names[1]}\nChoose special ability: "))
            player.special_ability(wizard, option)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()