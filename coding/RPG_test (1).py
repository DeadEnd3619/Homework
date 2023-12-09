import random

print("Hello. you have died. This is very unfortunate, but I have a solution. I can revive you so that you come to our world. You will arrive with nothing and you're expected to save my world. Come, nameless warrior, and face this dangerous world and become a god.")

Map_zone = "forest"

Player_name = input('What is your name adventurer? ')
Player_health = 100
Player_damage = 3
Player_luck = 100
Player_crit = 100
Player_money = 0
Player_strength = 0
Player_int = 0
Player_charisma = 0
Player_perception = 0
Player_positionx = 0
Player_positiony = 0

class Player_action:
    def __init__(self, input):
        self.input = input
    def Input(self):
        self.input = input('What do you plan to do? ')
        if self.input == 'w':
            Player_positiony += 1
            print(f'{Player_positionx},{Player_positiony}')
        if self.input == 'a':
            Player_positionx -= 1
            print(f'{Player_positionx},{Player_positiony}')
        if self.input == 's':
            Player_positiony -= 1
            print(f'{Player_positionx},{Player_positiony}')
        if self.input == 'd':
            Player_positionx += 1
            print(f'{Player_positionx},{Player_positiony}')
        else:
            print('invalid input')
class Enemy:
    def __init__(self, health, damage, rare_item, exp, enemy):
        self.health = health
        self.damage = damage
        self.rare_item = rare_item
        self.exp = exp
        self.enemy = enemy

    def Area(self):
        area = Map_zone
        if area == "???":
            self.damage + 10000
        else:
            self.damage + 0

    def npc_attack(self):
        print(f'{self.enemy_type} has decided to attack.')
        if Player_health <= self.damage:
            print('You have been slain in combat.')
        if Player_health > self.damage:
            print(f'You have taken {self.damage} from {self.enemy}')
class Slime(Enemy):
    enemy_type = "slime"

# Create an instance of Player_action and pass the input
player_action = Player_action(input())

# Call the Input method to get user input and update player position
player_action.Input()