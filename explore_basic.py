# basic operation in python
str1 = "Python is a case sensitive  language"
print(len(str1))
print(str1[9:])  # string slicing
print(str1.replace("a case sensitive","object oriennted"))

substring = "\"a\""
try:
    index = str1.index(substring)
    print(f"the index of {substring} is : {index} ")
except ValueError:
    print(f"{substring} not found")

substring1 = "a"
try:
    index = str1.index(substring1)
    print(f"the index of {substring} is: {index}")
except ValueError:
    print(f"{substring} not found")

print(str1.replace(" ","")) # remove whitespace
str2 = "    Python is a good   language to start your programming career     "
print(str2.strip()) # remove leading and trailing whitespace
print(" ".join(str2.split())) # remove extra whitespace from string

# variables
name = "nishu"
sid = 24379
dept = "civil"
print(f"Hey {name} here! \n My SID is {sid} \n My DEPARTMENT is {dept} ")

# bitwise operators
a = 40 # 0b101000
b = 43 # 0b101011
print(a & b) # a and b
print (a | b) # a or b
print(a ^ b) # XOR between two integers
print(a>>2 , b>>2) # right shift of a and  by 2
print(a<<2 , b<<2) # left shift of a and b by 2
print(bin(a)[2:])

# input statement
'''name = str(input ("Enter your full name here : "))
try:
    rank = int(input ("Enter your rank of JEE MAINS 2024: "))
    if rank < 40000:
        print("you got a seat at PEC!!" )
    else:
        print("Sorry, you can't grab a seat this year. But don't be sad , it is not the end of life. Give yourself one more chance.")
except ValueError:
    print(f"INVALID INPUT!! check {name}, again")'''

# bits
a = 23 #0b100111
b = 12 #0b1100
def no_counts(n):
    return bin(n).count('1')
print(no_counts(a))
print(no_counts(b))
def flip_bits(a,b): # bits needed to convert a to b
    c = a ^ b
    return bin(c).count('1')
print(flip_bits(2 , 5))

# list methods #mutable
list1 = ['cady', '12', 'medical', '98'] # all data types allowed
print(list1.append('mary')) # returns none but modifies the list
print(list1.remove("mary")) # returns none but modifies the list
#print(list1.clear())       # returns none but modifies the list
print(list1.pop())
print(list1.insert(1,"john"))
print(list1.insert(2, "mary"))
print(len(list1))
print(list1)

# tuple methods #immutable
t = (1, 2, {"name" : "cady"} , [4,5,6], (4,5,6),2) # different data types allowed
print(len(t))
print(t[2])
print(t.index(2,2))  # (value,start,stop)
for i in t:
    print(i)
# add items in tuple
t1 = ({"surname" : "mario"}, )  # byconcatenation
add = t + t1
print(add)
t2 = t1 # by slicing
add1 = t[:3] + t2 + t[3:]
print(add1)
t3 = list(t) # by converting to list
t3.insert(6,2)
print(tuple(t3))
# dictionary methods (key,value pair) , mutable
dict = {"a" : 2, "b" : 3, "c" : 4}
print(dict.get("a"))
print(dict.items())
print(dict.values())
print(dict.keys())
print(dict.update({"a" : 3, "d" : 4}))
print(dict)

# # largest of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a==b==c:
#     print("All the entered numbers has equal values")
# elif  a==b:
#     print("first number and second number are equal")
# elif a==c:
#     print("first number and third number are equal")
# elif c==b:
#     print("third number and second number are equal")
# elif a>b and a>c:
#     print(f"{a} is largest number")
# elif c>b and c>a:
#     print(f"{c} is largest number")
# elif b>a and b>c:
#     print(f"{b} is largest number")
# else:
#     print("Enter the correct numbers")

# # Using the max function
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# def maximum(a,b,c):
#     return max(a,b,c)
# largest = maximum(a,b,c)
# print("the largest number is ", largest)

# fahrenheit to celcius
# c = float(input("Enter the temperature in celcius: "))
# def fahreheit_to_celcius(c):
#       f =(c/5)*9 +32
#       return f
# celcius = fahreheit_to_celcius(c)
# print(celcius, "fahrenheit" )

# factorial of a number
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (factorial(n-1)*n)
print(factorial(80))

# fibonacci series
def fibonacci(n):
  fib_seq = [0,1]
  while len(fib_seq) < n:
       fib_seq.append(fib_seq[-1]+ fib_seq[-2])
  return fib_seq[:n]

print(fibonacci(5))

list1 = [1,"john",6]
list2 = [1,"mary",6]
def is_equal (list1,list2):
    if list1 == list2:
        return "True"
    else:
        return "false"
    
print(is_equal(list1,list2))

# is_palindrome()
s = ("ho ho")
def is_palindrome(s):
    s.replace(" ", "").lower
    return  s == s[::-1]
print(f"{s} is a palindrome, {is_palindrome(s)}")

#  draw pattern
def pattern(n):
    for i in range(1,n+1):
        for j in range (i):
          print("*", end=" " )
        print()

    for i in range(n,0,-1):
        for j in range (i):
            print("*" , end = " ")
        print()

print(pattern(6))

def draw_pattern(rows, initial_stars):
    stars = initial_stars
    for i in range(rows):
        for j in range(2):  # Print each row twice
            print('*' * stars)
        stars *= 2  # Double the number of stars for the next pair of rows

# Example: Draw the pattern with 6 rows starting with 2 stars
draw_pattern(3, 2)



# vowels = ("a","e","i","o","u")
# def count_vowels(a):
#     count =0
#     for char in a.lower():
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowels(a))

a = (1,299,546,9)
count = 0
for num in a :
    count+=num
print(count)

# os module
import os
print(os.getcwd())
print(os.listdir())
os.mkdir("New")
print(os.getcwd())
file_exist = os.path.exists("calculator.py")
print(file_exist)
print(os.listdir())

os.chdir("New")
print(os.getcwd())



























