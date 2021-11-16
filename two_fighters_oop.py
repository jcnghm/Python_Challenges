# Create a function that returns the name of the winner in a fight between two fighters.

# Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

# Each fighter will be a Fighter object/instance.

# Both health and damage_per_attack will be integers larger than 0. You can mutate the Fighter objects.

# Input = Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"
# Output = "Lew"

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        

def declare_winner(fighter1, fighter2, first_attacker):
    
    fighter_one = fighter1.health
    fighter_two = fighter2.health
    
    while fighter_one and fighter_two > 0:
        
        if first_attacker == fighter1.name:
            fighter_two -= fighter1.damage_per_attack
            if fighter_two <= 0:
                break
            fighter_one -= fighter2.damage_per_attack
            if fighter_one <= 0:
                break


        if first_attacker == fighter2.name:
            fighter_one -= fighter2.damage_per_attack
            if fighter_one <= 0:
                break
            fighter_two -= fighter1.damage_per_attack
            if fighter_two <= 0:
                break

    
    if fighter_one <= 0:
        return fighter2.name
    elif fighter_two <= 0:
        return fighter1.name

declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")