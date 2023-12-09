import random


class Coin:

   def __init__(self):
      self.response =""
   

   
   def __str__(self):
      return "You got a "+self.response+ ' when you flipped.'
   
   def coin(self):
      responses = [
       "Heads",
       "Tails"
      ]
      response = random.choice(responses)
      self.response = response
   


   # def petty_print(name):
   #    print('you got a ' + name + ' when you flipped')


useless_var = Coin()
useless_var.coin()
print(useless_var)