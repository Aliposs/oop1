                                                     
                                                     ## create an example define multilevel and mulitple ##
#                                        ______________________________________________________________________________                        #
                                                  
###############################################
# multilevel Inheritance
###############################################

class Animal:
    def __init__ (self, food, type, name):
        self.food = food
        self.type = type
        self.name = name

class cat1(Animal):
    def __init__(self, age_1,name_1 ,name, food, type):
        self.age_1 = age_1
        self.name_1 = name_1
        Animal.__init__(self, type, food, type, name)


class cat2(cat1):
    def __init__ (self, name, type, food, name_1, age_1, name_2, age_2):
        self.name_2 = name_2
        self.age_2 = age_2
        cat1.__init__( self, name_1, age_1, name, food, type)
        Animal.__init__(self, name, food, type)
    
    def display(self):
        print(self.food)
        print(self.name)
        print(self.age_1)
        print(self.name_1)
        print(self.age_2)
        print(self.name_2)

##############################################################
obbj1 = cat2("simba", "eating of meals", "meals", "koki", 9 , "bosi", 8 )
obbj1.display()
##############################################################




############################################################
# Multiple Inheritance
############################################################

class person_1:
    def __init__(self, name_1, age_1):
        self.name_1 = name_1
        self.age_1 = age_1


class person_2:
   def __init__(self, name_2, age_2):
       self.name_2 = name_2
       self.age_2 = age_2



class person_3:
   def __init__(self, name_3, age_3):
       self.name_3 = name_3
       self.age_3 = age_3



class family(person_1, person_2, person_3):
    def __init__(self, name_1, age_1, name_2, age_2, name_3, age_3):

        person_1.__init__(self,name_1, age_1)
        person_2.__init__(self, name_2, age_2)
        person_3.__init__(self, name_3, age_3)

    def display(self):
        print(self.name_1)
        print(self.age_1)
        print(self.name_2)
        print(self.age_2)
        print(self.name_3)
        print(self.age_3)

########################################################
obj1 = family("Ali", 19, "Ahmed", 12, "Mahmoud", 19)
obj1.display()
########################################################