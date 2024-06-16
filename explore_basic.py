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

# largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a==b==c:
    print("All the entered numbers has equal values")

elif  a==b:
    print("first number and second number are equal")
elif a==c:
    print("first number and third number are equal")
elif c==b:
    print("third number and second number are equal")
elif a>b and a>c:
    print(f"{a} is largest number")
elif c>b and c>a:
    print(f"{c} is largest number")
elif b>a and b>c:
    print(f"{b} is largest number")
else:
    print("Enter the correct numbers")

# Using the max function
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def maximum(a,b,c):
    return max(a,b,c)

largest = maximum(a,b,c)
print("the largest number is ", largest)








