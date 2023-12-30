# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:16:27 2023

@author: FreeComp
"""
##############################################

# Difference between class atteibuties


class Person:
    
    #Class Attributes
    name = "Ali"
    age = 19
    
    def __init__(self, name, age):
        #Instace Attributes
        self.name = name
        self.age = age
    
    def display(self):
    
        print("My name: ", self.name)
        print("My age is: ", self.age)
    
obj1 = Person("Ahmed", 12)
obj1.display()
print(Person.name)
print(Person.age)

#############################################################

# Example Override
class Animal:
    
    def Food(self):
        print("I eat the grass")
        
        
class Dog(Animal):
    
    def Food(self):              # Here will print Food Method's child To overriding this peroblem ,we will use {super / className .MethodName(self)} 
    
        Animal.Food(self)
        print("I eat the meat")  
        
obj2 = Dog()
obj2.Food()

################################################################

# def product(a, b):
#     do = a*b
#     print(do)
    
# def product(a, b, c):
    # do = a*b*c
    # print(do)
    
# product(1, 2)
# product(2, 3, 5)
# product(1, 2)

############################################################

def add(datatype, *args):
    if datatype == 'int':
        answer = 0
        

    if datatype == 'str':
        answer = ''
        
    for x in args:
        
        answer = answer + x
    print(answer)
    
    
    
add('int', 7, 4)
add('str', "Al", "i")   
#############################################
#conda 
############################################## 

@dispatch(int, int)
def product(first, scound):
    result = first*scound
    print(result)
    
@dispatch(int, int, int)
def product(first, scound, third):
    result = first*scound*third
    print(result)
    
@dispatch(float, int)

def product(first, scound):
    result = first*scound
    print(result)
    
    
product(1, 2)
product(2, 3, 5)
product(2.3, 3)
