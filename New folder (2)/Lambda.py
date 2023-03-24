# Code to demonstrate how we can use a lambda function  
add = lambda num: num + 4  
print( add(6) )  

def add( num ):  
   return num + 4  
print( add(6) )  

# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
print(odd_list)  

#Code to calculate the square of each number of a list using the map() function  
  
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]  
squared_list = list(map( lambda num: num ** 2 , numbers_list ))  
print( squared_list )  


#Code to calculate square of each number of list using list comprehension  
squares = [lambda num = num: num ** 2 for num in range(0, 11)]  
   
for square in squares:  
    print( square(), end = " ")  

    # Code to use lambda function with if-else  
Minimum = lambda x, y : x if (x < y) else y  
print(Minimum( 35, 74 ))  

# Code to print the third-largest number of the given list using the lambda function  
  
my_List = [ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]  
  
# sorting every sublist of the above list  
sort_List = lambda num : ( sorted(n) for n in num )  
  
# Getting the third largest number of the sublist  
third_Largest = lambda num, func : [ l[ len(l) - 2] for l in func(num)]  
result = third_Largest( my_List, sort_List)  
  
print( result )  