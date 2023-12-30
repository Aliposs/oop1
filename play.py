#####################################################################

# Take_age = int(input("Enter you Age :"))
# while ( Take_age < 0):
#    Take_age = print(int(input("Enter positive number : ")))
# print(f'your age is : {Take_age}')

######################################################################

######################################################################

# def multpli_elements_of_list(lis_t):
   
#     lis__t = []
#     for element in lis_t:
#         element = element * 2
      
#         lis__t.append(element)

#     return lis__t


# lis_t = list(input("Enter your list : "))
# calling = multpli_elements_of_list(lis_t)
# print(calling)

########################################################################

########################################################################

# def check_number( num ):
#     if num %2 == 0:
#         print(" this number is even number!")
#     else:
#         print(" this number is odd!")


# print(check_number(9))        

#######################################################################
        
#######################################################################

# class Animal :
    
#     def __init__(self , name , age , food_type  , kind_animal ):
#         self.name = name
#         self.age = age
#         self.food_type = food_type
#         self.kind = kind_animal
#     def get_name(self):
#         ''' get_name is a function that return name of an animal '''
#         return print( "# My name is ", self.name )
    
#     def get_kind_animal(self):
#         ''' get_kind is a function that return kind of this animal '''
#         return print( "# I'm " , self.kind)
    
#     def get_Age(self):
#         ''' get_Age is a function that return age of this animal '''
#         return print(  "# I have ", self.age , " years ")
    
#     def get_Food_type(self):
#         '''get_food_type is a function that return type of food that this animal eat it '''
#         return print( "# I eat ", self.food_type)
# ##################################################################################################################################    
# class Child (Animal) :
#     def __init__( self , child_name , child_age , name , age , food_type , kind_animal ):
#         self.baby_name = child_name
#         self.baby_age = child_age

#         Animal.__init__ ( self , name , age , food_type , kind_animal )

#     def get_baby_name(self):
#         return ("My name is " , self.baby_name ,"I'm son's " , self.baby_name)
    
#     def get_child_age(self):
#         return (f"I have {self.baby_age} months")
    
#     def Finshied (self):
#         return " Finishied "
   
# op = Child( " Sihooo " , 12 , " Simbaaa " , 16  , " meals " , " categore of lions " )

# print(op.baby_age , "\n")
# print(op.baby_name , "\n")
# print(op.get_Age())
# print(op.get_name())

#########################################################################

#########################################################################

# class Ayman :
#     def __init__( self , id ):
#         self.defination = id
#         return print(self.defination)
#     def __str__(self):
#         return " / " , str(self.defination) , " \ "

# obb = Ayman(12)

##################################################################
################################################################## 
from copyreg import dispatch_table


# class Person_1 :
#     def __init__(self , name_person_1):
#         self.name_person_1 = name_person_1
#         print(self.name_person_1)

# class Person_2 :  
#     def __init__(self , name_person_2  ):
#         self.name_person_2  = name_person_2  
#         print(self.name_person_2)

# class Hell(Person_1 , Person_2):
#     def __init__ (self , name_person_2 , name_person_1):

#        super().__init__( name_person_1)
#        super().__init__( name_person_2  )

# opp = Hell("Aymen" , "Ahmed")

#############################################################
#############################################################
# class Person_1 :
    
#     def __init__(self , name_1 , idnum_1):
#         self._name_1 = name_1
#         self._idnum_1 = idnum_1

       

# class Person_2:

#     def __init__(self , name_2 , idnum_2):
#         self._name_2 = name_2
#         self._idnum_2 = idnum_2

       
   
# class Print_3(Person_2 , Person_1 ):
    
#     def __init__(self , name_1 ,  idnum_1 , name_2 ,idnum_2  ):

#         Person_1.__init__(self , name_1 , idnum_1)
#         Person_2.__init__(self , name_2 , idnum_2)

#     def display(self):
#         print("Hello World 1")
#         print(self._name_1)
#         print(self._idnum_1)
#         print("Hello World 2")
#         print(self._name_2)
#         print(self._idnum_2)
#         print("Good Bye Everyone ")

# obb = Print_3( "Ali " , 20220046 , "Mahmoud" , 20220087 )
# obb.display()

##########################################################
##########################################################

# def critical_area(reduis):
#     area = 3.14 * (reduis) **2
#     print(f'Area of Circil That Has {reduis} Of Reduis Equals: {area}cm ')

#     return critical_area

# critical_area(12)

#########################################################
#########################################################

# class A:
#     def __init__(self, val1):
#         self.val = val1
#     def method_a(self):
#         return 10+self.val

# class B:
#     def __init__(self, val2 ):

#        self.val = val2
#     def method_b(self, obj):
#         return obj.method_a() + self.val

# obj1 = A(20)
# # print(obj1.method_a())
# obj2 = B(30)
# print(obj2.method_b(obj1))
######################################################
# class Employee:
#     _counter = 100
#     def __init__(self, name):
#         self.name = name
#         Employee._counter += 1
#     @staticmethod
#     def get_counter():
#         return Employee._counter
    
# emp1 = Employee("ali")
# emp2 = Employee("ali")
# emp3 = Employee("ali")
# emp4 = Employee("ali")
# emp5 = Employee("ali")

# print(Employee.get_counter() - 100)
#####################################################

# def Calculate_factorial(num =  int(input("Enter Number: "))):
#     factorial = 1
    
#     for n in range(1, num + 1):
#         factorial = factorial * n
#     return print(factorial)

# Calculate_factorial()

#######################################################

# class Perant:
#      name = "defulat"
#      _age = 0
#      __address = "defulat"

#      def __init__(self, name, age, address):
#         self.name = name
#         self._age = age
#         self.__address = address
    
#      def _display(self):
#         print("My name is:", self.name)
#         print("My age is:", self._age)
#         print("I live in ", self.__address)

# onn = Perant("Ali", 19, "Biala")

# print(onn.name)

# class P1:
#     def show(self):
#         print("P1")
# class P2(P1):
#     def show(self):
#         P1.show(self)
#         print("P2")

# obj1 = P2()
# obj1.show()
#################################################################

# import asyncore
# from multipledispatch import dispatch


# @dispatch(int, int)
# def product(first, scound):
#     result = first*scound
#     print(result)
    
# @dispatch(int, int, int)
# def product(first, scound, third):
#     result = first*scound*third
#     print(result)
    
# @dispatch(float, int)

# def product(first, scound):
#     result = first*scound
#     print(result)
    
    
# product(1, 2)
# product(2, 3, 5)
# product(2.3, 3)
###################################################################
# an example about how to handle the overloading

def add(datatype, *args):

	if datatype == 'int':
		answer = 0

	if datatype == 'str':
		answer = ''

	for x in args:

		answer = answer + x

	print(answer)


add('int', 5, 6)

add('str', 'Hi ', 'Geeks')
###########################################################