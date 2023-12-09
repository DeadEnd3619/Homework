# # print('AHHHHHHHHHHH')
# import random
# '''Python is a high level language , general purpose and very popular programming language. The latest python is version 3. Python is used in machine leaening, web-design and many other industries. The biggest strength of python is it's vast libraries. This has many application. Comments are very important for
# Rule 1. Comments should not be the same as the code
# Rule 2. good comments don't excuse bad code
# Rule 3. If you are unable to write a clear comment, it's the code thats wrong
# Rule 4. Comments should clear confusion, not make it
# Rule 5. explain unidiomatic code
# Rule 6. Provide links to copied code
# Rule 7. Include links for refrences as they become relivent.
# Rule 8. Add comments when fixing bugs
# Rule 9. Use comments to mark incomplete implementations.'''
# #Weird, thats kinda cool
# """This stuff is very powerful, i hope it doesn't come to life"""
# f_name,l_name,age = "Conner", "Kirkley", 35
# initial_value =start = i= 0
# print(age)
# print(initial_value)
# '''sequence type: tuple, range, list
# mapping types: dict
# Set types: set, frozenset
# boolean Types: bool
# none type: nonetype
# '''
# a,b,c = 221,-9,15
# if a<b: 
#     print('that is correct')
#     b=500
#     Print('all done')
# x = 3
# y = str(x)
# print(x * 5)
# z = "The_Prong"
# finding = z.find("Prs")
# print(x,y,z)
# print("my age was once " + str(x))
# '''Indentation: Indentation refers to the spaces at the beginning of the code line. In other languages, indentation is only for readability, in Python it's very important.'''
# test = "This is a test string"
# print(test[5])
# print(test[5:15])
# print (test.upper())#uppercase letters
# space = ' This has a lot of spaces in and around it '
# txt = "i tPinA Ihis woNks"
# x = txt.capitalize()
# print (x)
# txx = 'Coding can be difficult, hard even'
# y = txx.find('difficult')
# print (y)
# print (txx+txt)
# name= 'take 5.'
# cost= 45
# ammount= 20
# statements = "I had way to much {} I had {}. Now i have {}, i should see a doctor. Why did i buy so much and then eat almost half?"
# print(statements.format(name,cost,ammount))
# '''conditionals for pythons'''
# import math
# first_name = 'Bernard'
# Age = 18
# Patience = -25
# Verbal_abuse = 1,000,000,000,000
# Kenny_just_Died = False
# Fake_age

# if Kenny_Just_Died:
#     print('Kenny WHYYYYYYYY')
# if age > 20:
#     print('Conner kirkley')
#     age += 1
# elif age == 19:
#     print("Party in the usa")

# else:
#     print("crotch spawns")
#     age = 19
# j = 6
# print(j**3)
# print(math.sqrt(age))
# print(math.pow(2,6))
# #  one equal sign is a Value
# #  two equal signs is checking value
# # three equal signs checks value without formating numbers and strings n' such
# Grade = 79
# Grade = 69
# Firstname = 'Conner'
# Lastname = "kirkley"






# if Grade > 89:
#     print('A')
# elif Grade > 79:
#     print('B')
# elif Grade > 69:
#     print('C')
# elif Grade > 59:
#     print('D')
# # else:
# #     print('F')
# '''lists in python
#     '''
# food = ['tacos', "burritos", "pizza", "soulfood"]
# # print(food)
# # print(len(food))
# # print(food[2])
# # print(sorted(food)) #does not alter list other then order
# # print(food)
# # food.reverse()
# # print(food)
# # food.append('carmelcorn') #adds to the end of the list
# # print(food)
# # print(food.index('tacos'))
# # del food[4]
# # print(food)

# # #dictionaries - key value

# favgames = {"Josh": 'Star wars battle front 2', 'Chris': 'Jump Force', 'Shawn': 'Apex legends', 'Lawrence': 'Stalris'}
# print(favgames)
# print(favgames.keys())
# print(favgames.values())
# print(len(favgames))

# user = 'Combogod#6047'
# password = 'Noword'

# login_username = input('')
# login_password = input('')
# if user == login_username and password == login_password:
#     print('Succes')
# else:
#     print('no')
#To the loops: for loops used for 


# for thing in food:
#     print(thing)

# for i in range(11,63895,77):
#     print(i)
# else:
#     print('numbers go burrr')
# friends =['CJ','Shawn','Lawrence','Nick','Neltin']

# for x in friends:
#     for y in food:
#         print(x + ': ' + y)
    
# conteacts = []
# index= 2
# while index <= 10:
#     print(index)
#     index +=2
# answer = False
# while answer == False:
#     question = input('what is a weird guys favorite food?')
#     if(question.upper() == 'PURPLE'):
#         answer = True

#functions

'''a function is a block of code which only runs when it is called    you can pass data known as parameters into a function. A function can return data as a result but is not mandatory'''

# def pretty_print(name,direction):
#     print('-----***' + name + '***-----')

# pretty_print('deigo','north')



# name = 'bernard'
# age = 25
# email = 'bernard@benhard.com'

# if name == 'bernard':
#     print(email, name)
#     # favorite_color = 'blue'

# for i in range(0,len(name)):
#     favorite_color = 'purple'

# Global works in all things while local works and only exists in a function.
'''object oriented programing'''

# def myfunction():
#     global favorite_place
#     favorite_place = 'my house'
#     return favorite_place

# print(myfunction())
# print(favorite_place)



'''
Python Arithmetic Operators
Operator    Name            Example 
+           Addition        x + y   
-           Subtraction     x - y   
*           Multiplication  x * y   
/           Division        x / y   
%           Modulus         x % y   
**          Exponentiation  x ** y  
//          Floor division  x // y

Python Assignment Operators:
Operator    Example     Same As 
=           x = 5       x = 5   
+=          x += 3      x = x + 3   
-=          x -= 3      x = x - 3   
*=          x *= 3      x = x * 3   
/=          x /= 3      x = x / 3   
%=          x %= 3      x = x % 3   
//=         x //= 3     x = x // 3  
**=         x **= 3     x = x ** 3  
&=          x &= 3      x = x & 3   
|=          x |= 3      x = x | 3   
^=          x ^= 3      x = x ^ 3   
>>=         x >>= 3     x = x >> 3  
<<=         x <<= 3     x = x << 3


Operator    Description Try it
()          Parentheses 
**          Exponentiation  
+x  -x  ~x  Unary plus, unary minus, and bitwise NOT    
*  /  //  % Multiplication, division, floor division, and modulus   
+  -        Addition and subtraction    
<<  >>      Bitwise left and right shifts   
&           Bitwise AND 
^           Bitwise XOR 
|           Bitwise OR  
not         Logical NOT 
and         AND 
or          OR
'''

#Object oriented operataions
#Class definition: A blueprint for creating objects (a particular data structure) providing initial values for state (member varibales or attributes), and implementations of behaviors (member functions or methods)



# class Person:
#     #__init__ is a python CONSTRUCTOR for classes that is used to INITIALIZE attributes of objects as soon as the object is formed
#     # self is a default parameter/argument that represents the INSTANTIATED object of the class.
#     def __init__(self, first, middle, last, age):
#       self.first = first
#       self.last = last
#       self.middle = middle
#       self.age = age
#     def __str__(self):
#        return self.first + " " + self.middle + " " + self.last + " " + str(self.age)
    
#     def initials(self):
#        return self.first[0]+self.middle[0]+self.last[0]
    
#     def changeage(self, amount):
#        self.age += amount

# aperson = Person('bender','bending','rodriguez',4)
# print(aperson)
# aperson.changeage(2)
# print(aperson)
# print(aperson.initials())


# class Shape:
#    def __init__(self, xcor, ycor):
#       self.x = xcor
#       self.y = ycor

#    def __str__(self):
#       return 'x:' + str(self.x) + ' y: ' + str(self.y)
   
#    def move(self, x1, y1):
#       self.x += x1
#       self.y += y1
# night = Shape(5,7)
# print(night)
# night.move(2,2)
# print(night)

# Definitins of inheritance: The procedure in which one class inherits the attributes and methods of another class. The class whose properties and methods are inherited is know is know as the parent class or super class and the class that inherits the properties from the parent class is the child class or derived class.

# class Rectangle(Shape):
#    def __init__(self, xcor, ycor, width, height):
#       Shape.__init__(self, xcor, ycor)
#       self.width = width
#       self.height = height

#    def __str__(self):
#       recStr = Shape.__str__(self)
#       recStr += ' width= ' + str(self.width) + ' height= ' + str(self.height)
#       return recStr




# rec = Rectangle(5,10,8,9)
# print(rec)

# class Coin:

#    def __init__(self):
#       self.response =""
   

   
#    def __str__(self):
#       return "You got a "+self.response+ ' when you flipped.'
   
#    def flip(self):
#       responses = [
#        "Heads",
#        "Tails"
#       ]
#       response = random.choice(responses)
#       self.response = response
   


#    # def petty_print(name):
#    #    print('you got a ' + name + ' when you flipped')


# useless_var = Coin()
# useless_var.flip()
# print(useless_var)

# Routing in flask

'''What is a route? 
A route is a URL you can use to determine what the user receives when they visit your web application on their browser. For example, http://127.0.0.1:5000/ is the main route might be used to display an index page. The URL http://127.0.0.1:5000/ about may be about may be another route used for an about page that gives the visitor some information about your web application.. similarly, you can create a route that allows users to sign into your application at http://127.0.0.1:5000/login'''

















