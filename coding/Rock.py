import random

responses = [4, 5, 8]

class Action_lawsuit:
    def Cpu_action(self):
        print('Hello, This is a rock-paper-scissors simulation. You must choose ')
        cpu = random.choice(responses)
        return cpu

class Player_action(Action_lawsuit):
    def Decision(self):
        Choice1 = input('Please choose either: Rock, Paper, or scissors. ')
        choice2 = len(Choice1)
        return choice2

class Game(Player_action):
    def Hand(self, cpu, choice2):
        if choice2 == 4:
            if cpu == 4:
                print('Its a tie. No score added or removed.')
            if cpu == 5:
                print('You lose. You have lost one point.')
            if cpu == 8:
                print('You win. You have earned a point.')
        if choice2 == 5:
            if cpu == 4:
                print('You win. You have earned a point.')
            if cpu == 5:
                print ('Its a tie. No score added or removed.')
            if cpu == 8:
                print('You lose. You have lost one point.')
        if choice2 == 8:
            if cpu == 4:
                print('You lose. You have lost a point.')
            if cpu == 5:
                print('You win. You have earned a point.')
            if cpu == 8:
                print('Its a tie. No score will be added or removed.')

