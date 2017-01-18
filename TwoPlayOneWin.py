class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    """Function to find the winner"""

    fighter_list = [fighter1, fighter2]

    # Find which fighter object attacks first
    attacker1 = [i for i in fighter_list if first_attacker == i.name]
    attacker2 = [i for i in fighter_list if first_attacker != i.name]

    # Checks damage
    fightstatus_attacker1 = attacker2[0].health / attacker1[0].damage_per_attack
    fightstatus_attacker2 = attacker1[0].health / attacker2[0].damage_per_attack


    # Checks winner based on steps to death and attack
    if fightstatus_attacker1 > fightstatus_attacker2:
        return attacker2[0].name
    else:
        return attacker1[0].name


print(declare_winner(Fighter("Jerry", 30, 5), Fighter("Harald", 20, 5), "Harald"))
