#!/usr/bin/env python
# coding: utf-8

# ## Introduction
# 
# This notebook is intended for the beginners. It covers the basics and fundamentals of Pyhton which are essential for making an understanding of language.
# 
# This is first in the series, I will come up with a similar notebook for advanced level as well.
# 
# After looking at number of sites and tutorials, i found https://thepythonguru.com/ really helpful for learning, in a way that it has clearly laidout topics for beginners as well as for the people at advanced level. 
# 
# I will not cover the theory in this notebook as the same is available at the above mentioned site as well, rather i will back it up with the example and code snippets that i have created for my learning. That way you will have access to the more code examples.
# 
# Also, i have code examples on the topics which you will not find in the site itslef but i have created by comparing it to Java.
# 
# The idea is that you create you general understanding of the language using the following links:
# 
# https://thepythonguru.com/getting-started-with-python/
# https://thepythonguru.com/installing-python3/
# https://thepythonguru.com/running-python-programs/
# https://thepythonguru.com/datatype-varibles/
# https://thepythonguru.com/python-numbers/
# https://thepythonguru.com/python-strings/
# https://thepythonguru.com/python-lists/
# https://thepythonguru.com/python-dictionaries/
# https://thepythonguru.com/python-tuples/
# https://thepythonguru.com/datatype-conversion/
# https://thepythonguru.com/python-numbers/
# https://thepythonguru.com/python-strings/
# 
# Once you have the general understanding then you can start using this notebook for the code examples. The code examples are in the same order as the topics covered at pythonguru, so to get the most out of it first understand the topic from there and then use this notebook for extensive examples. If you have reached this far, then you know what i am talking about :)
# 
# 
# TODO:
# 
# Advanced topics to be explored:
# Static vs non-static variables & methods
# Calling a method from the constructor, like the one in 'Oprator Overloading'
# Different Collections like Set
# 

# In[4]:


## 
# Using if else clauses
##

month = 'Jan'
year = '2019'
if((month=='Jan') or year=='2018'):
    print('1')
elif( year=='2019'):
    print('2')
else:
    print('default')


# In[5]:


## 
# Functions declaration and calling
##
def sum(start, end):
    if(start is None or end is None):
        print('start and end are mandatory')
    elif(start >= end):
        print('start must be smaller than end')
    else:
        total = 0
        for i in range(start, end+1):
            total = total + i
        return total
    
sum(1,5)
        


# In[54]:


##
# Use of global keywoard
## 

def testing():
    testing_local = 'local var'
    global testing_global #value to global can not be assigned while declaration.
    testing_global = 'global var'

testing()
#print(testing_local) -> This will throw an error stating testing_local is not defined, try uncommenting and explore
print(testing_global)
    


# In[ ]:


##
# Arguments with default value
## 

def testing_default_1(var1, var2=None):
    
    #testing_default_1(1,1) -> Uncomment this code and see the magic!!
    return str(var1) + " , " + str(var2) 
  
    
print(testing_default_1(1,2), "\n")
print(testing_default_1(1), "\n")


# In[35]:


##
# Method overloading 
##
def overload(var1):
    return var1

def overload(var2, var3):
    return var2 + var3

#overload(1) -> Executing this line will result in error as method overloading is not supported in Pyhton
#always the latest defination is considered for execution. 

#Following call will work just fine
overload(1,2)


# In[34]:



##############################################
# However you can still have the same method doing different things based on the number of arguments. It is done
#using the varargs
##############################################

def varArgsExampleMethod(*args):
    if(args is not None):
        returnContainer = []
        length = len(args)
        if(length > 0):
            global sameType
            sameType = False
            currentType = None
            for i in args:
                if(currentType is None):
                    currentType = type(i)
                elif(type(i) == currentType):
                    sameType = True
                    continue
                else:
                    sameType = False
                    break
            print(sameType)
            returnContainer.append(sameType) 
            
        if(length == 0):
            print('Please provide atleast one argument')
            returnContainer.append(0)
        elif(length == 1):
            print('one argument')
            returnContainer.append(1)
        elif(length == 2):
            print('two argument')
            returnContainer.append(2)
        elif(length == 3):
            print('three argument')
            returnContainer.append(3)
        else:
            print('More than three arguments')
            returnContainer.append(4)
    ##
    # In python a method can return multiple objects, unlike Java where only one object can be returned.
    # One way of doing it is to create a wrapper object & return it
    # Another way is by seperating the multiple objects by comma.
    # Both ways shown below
    ##
    
    return returnContainer
    #return sameType, 0

varArgsExampleMethod(2,1)
            
    


# In[43]:


##
# Range Method
# There are 3 variants of range method, one which takes just the end number, second which takes the start and end & third whcih also takes the step size
##
print('--------------1st variant: Start--------------')
for i in range(10):
    print(i)
print('--------------1st variant: End--------------')

print('--------------2nd variant: Start--------------')
for i in range(2,5):
    print(i)
print('--------------2nd variant: End--------------')


print('--------------3rd variant: Start--------------')
for i in range(0,10,2):

    print(i)
print('--------------3rd variant: End--------------')


# In[8]:


#While loop
#Python does not support do-while but just the while loop

counter = 5
print("--------------While loop start--------------")
while(counter > 0):
    print(counter)
    counter-=1
print("--------------While loop End--------------")


#Python does not support do while but we can work around with that like below:
print("--------------Do-While loop start--------------")
i = 1  
  
while True:  
    print(i)  
    i = i + 1  
    if(i > 5):  
        break  
        
print("--------------Do-While loop end--------------")


# In[16]:


#Generating random numbers  in Python
#random module in python generates random numbers

import random

counter = 5
while(counter > 0):
    #random.random() prints the random number r, such that 0 <= r < 1
    print(random.random())
    counter-=1
        
counter = 10
while(counter > 0):
    #random.random() prints the random number r, such that 0 <= r < 1
    print(random.randint(1,10))
    counter-=1


# In[68]:


##
# Classes & objects
##
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ChangeParameters:
    obj = Person('Praveen Gaur', 32)
    print(obj.name)
    print(obj.age) 
    #changing the values
    obj.name = 'New Name'
    obj.age = 'New Age'
    print(obj.name)
    print(obj.age) 


# In[82]:


#But this is not a good idea to expose the parameters to the external code so that the values can be changed from outside, we should declare the variables as private
# Rewriting the above code in more safe way
#Classes & objects
class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def defineObject(obj):
        print(obj.__name)
        print(obj.__age)
    
    def redefineValues(self, name, age):
        self.__name = name
        self.__age = age
        
class ChangeParameters:
    obj = Person('Praveen Gaur', 32)
    obj.defineObject()
    
    #changing the values is not allowed, following code will not change the values
    obj.__name = 'new value'
    obj.__age = 'new value'
    obj.defineObject()
    
    #but the values can only be changed when accessed from inside the class
    obj.redefineValues('new name', 'new age')
    obj.defineObject()


# In[89]:


#Methods can be called in 2 ways, by using the class name or by using the object itself
#1: Calling a method using the class name, in this type you do not have to define a extra argument in the method definition
class Definition:
    def callingMethod(argument):
        print(argument)

object = Definition()
Definition.callingMethod(1)#Calling the methos using the class name
    

        
#2: Calling a method using the object variable, in this type you have to define an extra argument in the method definition
class Definition:
    def callingMethod(self):
        print(self.name)
    def __init__(self, arg):
        self.name = arg
        
object_1 = Definition('Praveen')
object_2 = Definition('Deepak')
object_1.callingMethod()#Calling the methos using the class name
object_2.callingMethod()#Calling the methos using the class name


# # Oprator Overloading
# Oprator overloading is a powerful feature using which you can overridge the default behavior of opeartors. For instance if you want your class(Circle) to define the way how 2 circles can be added or to check if two circles are equal or not.
# 
# Following operators can be overloaded with the provided method name:
# 
# + 	  __add__(self, other) 	 Addition
# * 	  __mul__(self, other) 	 Multiplication
# - 	  __sub__(self, other) 	 Subtraction
# % 	  __mod__(self, other) 	 Remainder
# / 	  __truediv__(self, other) 	 Division
# < 	  __lt__(self, other) 	 Less than
# <= 	  __le__(self, other) 	 Less than or equal to
# == 	  __eq__(self, other) 	 Equal to
# != 	  __ne__(self, other) 	 Not equal to
# > 	  __gt__(self, other) 	Greater than
# >= 	  __ge__(self, other) 	 Greater than or equal to
# [index] 	  __getitem__(self, index) 	 Index operator
# in 	  __contains__(self, value) 	Check membership
# len 	__len__(self) 	 The number of elements
# str 	__str__(self) 	 The string representation

# In[126]:



import math
class Circle:
    
    def __init__(self,argument):
        self.__radius = argument
       # self.__area = area()
    
    def area(self):
        area = math.pi * self.__radius ** 2
        self.__area = area
        return area
    def __add__(self, anotherCircle):
        return ((self.__area + anotherCircle.__area))
    def __eq__(self, anotherCircle):
        if(self.__area is not None and anotherCircle.__area is not None):
            return (self.__area == anotherCircle.__area)
        
circle_1 = Circle(2)
print("circle_1 area is : " + str(circle_1.area()))
circle_2 = Circle(4)
print("circle_2 area is : " + str(circle_2.area()))
print("Combined area of two circles is : " + str(circle_1 + circle_2))
print("Are 2 circles equal: " + str(circle_1 == circle_2))


# ## Inheritance & Polymorphism
# 
# Just like any other object oriented programming language, Pyhton also supports inheritance but if you are coming from Java, then there is a big surprise, it supports multiple inheritance i.e. one subclass inheriting two different parent classes.
# 
# 

# In[130]:


##
# Inheritance - showing extending a class
##

class Vehicle:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
    
    def getColor(self):
        return self.__color
    
    def getName(self):
        return self.__name
    
class Car(Vehicle):
    def __init__(self, name, color, numberOfWheels, engineSize, numberOfDoors):
        super().__init__(name, color)#calling the parent constructor
        self.__numberOfWheels = numberOfWheels
        self.__engineSize = engineSize
        self.__numberOfDoors = numberOfDoors
    
    def getNumberOfWheels(self):
        return self.__numberOfWheels
    
    def getEngineSize(self):
        return self.__engineSize
    
    def getNumberOfDoors(self):
        return self.__numberOfDoors
    
    def defineCar(self):
        print("This is a car, specifications: ")
        print("name: " + self.getName())
        print("color: " + self.getColor())
        print("numberOfWheels: " + self.getNumberOfWheels())
        print("engineSize: " + self.getEngineSize())
        print("numberOfDoors: " + self.getNumberOfDoors())
        
car = Car('Skoda', 'black', '4','2600', '4')
car.defineCar()


# In[146]:


##
# Inheritance - showing how multiple inheritance works
# MRO - Method Resolution Order
# MRO represents the order in which classes will be searched in oredr to execute an overridden method.
# MRO defines the presidence path, class appearing first will be picked for execution
##

class Parent_1:
    def define():
        print('In class parent_1')
        
class Parent_2:
    def define():
        print('In class parent_2')

# MRO depends upon the order in which the child class places the parent classes
# For Child_1, Parent_1 takes the presidence as it is declared before parent_2
# For Child_2, Parent_2 takes the presidence as it is declared before parent_1
class Child_1(Parent_1, Parent_2):
    def define(self):
        self.define()
        
class Child_2(Parent_2, Parent_1):
    def define(self):
        self.define()
        
        
print(Child_1.mro())
print(Child_2.mro())


# In[168]:


##
# Inheritance - testing the multiple inheritance
# MRO comes in to play
##

class Parent_1:
    def define(self):
        print('MRO is: ', Child_1.mro())
        print('In class parent_1')
        
class Parent_2:
    def define(self):
        print('MRO is: ', Child_2.mro())
        print('In class parent_2')

# MRO depends upon the order in which the child class places the parent classes
# For Child_1, Parent_1 takes the presidence as it is declared before parent_2
# For Child_2, Parent_2 takes the presidence as it is declared before parent_1
class Child_1(Parent_1, Parent_2):
    def define_child(self):
        self.define()
        
class Child_2(Parent_2, Parent_1):
    def define_child(self):
        self.define()
        

child_1 = Child_1()
child_1.define_child()

child_2 = Child_2()
child_2.define_child()

parent_1 = Parent_1()


# In[170]:


##
# isinstance method checks the if the given object is of given Type or not - it honors the inheritance
# have a look at the following examples
##
print(isinstance(child_1, Child_1))
print(isinstance(child_1, Child_2))
print(isinstance(child_1, Parent_1))
print(isinstance(child_1, Parent_2))
print(isinstance(child_1, Parent_2))
print(isinstance(parent_1, Child_1))


# # Exception Handling
# 
# In this section, we will understand how to catch exceptions & perform required actions
# Also, will see how to define custom Exception types.
# 
# More details at https://thepythonguru.com/python-exception-handling/
# 
# Documentation: https://docs.python.org/3/library/exceptions.html
# 

# In[9]:


class DivideHelper:
    def divide(numerator, denominator):
        result = None
        try:
            result = numerator/denominator
        except ZeroDivisionError as zError:
            print('Divide by zero is not allowed: ',zError)
        except FloatingPointError as fError:
            print('Floating point error')
        else:
            print('End of try/catch block')
        finally:
            print('Inside finally')
            return result

#DivideHelper.divide(2,4)
DivideHelper.divide(2,0)


# # Declaring the custom exception type
# Pyhton supports the custom exception type, for that you need to extend one of the system exception classes. BaseException class is the top exception class, you can extend this class to create custom exception also, if the custom exception is little focused then you can extend one of the other classes as well like: FloatingPointError, EOFError and others.
# 
# More details at https://thepythonguru.com/python-exception-handling/
# 
# Documentation: https://docs.python.org/3/library/exceptions.html
# 

# In[ ]:


##
# Declaring custom exception class which inherits ZeroDivisionError, it checks for denominator for 0 & also checks if either numerator or denominator < 0
##


# In[11]:


class CustomNumberException(ArithmeticError):
    def __init__(self,numerator, denominator):
        super().__init__()
        print(numerator)
        if(numerator < 0 or denominator < 0):
            print('numerator & denominator have to be greater than zero')

class DivideHelper:
    def divide(numerator, denominator):
        
        result = None
        try:
            if(numerator < 0 or denominator < 0):
                print('inside if')
                raise CustomNumberException(numerator, denominator)
            result = numerator/denominator
        except ZeroDivisionError as zError:
            print('Divide by zero is not allowed: ',zError)
        except FloatingPointError as fError:
            print('Floating point error')
        else:
            print('End of try/catch block')
        finally:
            print('Inside finally')
            return result

#DivideHelper.divide(2,4)
DivideHelper.divide(2,-1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




