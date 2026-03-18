#PART A:
# #Q1.
#(A) Maximum and minimum in a list
nums = [3, 7, 2, 9, 5]

max_val = nums[0]
min_val = nums[0]

for num in nums:
    if num > max_val:
        max_val=num
    if num < min_val:
        min_val=num

print("Max:",max_val)
print("Min:",min_val)

#(B) count frequency using dictionary
nums = [1, 2, 2, 3, 1, 4]
freq = {}

for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print(freq)

#-----------------------------------------------------------------------------------------------
#Q2.
#(A) Reverse a number
n = 123
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)

#(B) Check if palindrome
n = 121
original = n
rev = 0

while n > 0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10

if original==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#-----------------------------------------------------------------------------------
#Q3. 
# (A) Tuples into dictionary
tuples = [("a",1),("b",2),("c",3)]
d = {}

for item in tuples:
    key = item[0]
    value = item[1]
    d[key] = value
print(d)

#(B) Key with highest value
d = {"a": 10, "b": 25, "c": 15}

max_key = None
max_val = -1

for key in d:
    if d[key] > max_val:
        max_val = d[key]
        max_key = key
print(max_key)

#--------------------------------------------------------------------------------
#Q4.
def calc(*args):
    total = 0
    
    for num in args:
        total += num
    
    avg = total / len(args)
    return total, avg

print(calc(10, 20, 30))

#--------------------------------------------------------------------------------------------
#Q5.
def topper(**kwargs):
    max_marks = -1
    top_student = ""

    for name in kwargs:
        if kwargs[name] > max_marks:
            max_marks = kwargs[name]
            top_student = name

    return top_student

print(topper(Aditi=90, Rahul=85, Neha=95))

#------------------------------------------------------------------------------------------------
# PART B:

class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(tuple(result))

    def __sub__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])
        return Vector(tuple(result))

    def __mul__(self, scalar):
        result = []
        for i in self.values:
            result.append(i * scalar)
        return Vector(tuple(result))

    def __repr__(self):
        return str(self.values)
    
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)

#--------------------------------------------------------------------------------------------
#PART C:
#Q2:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

    def __str__(self):
        return f"{self.name} - {self.marks} - Grade {self.grade()}"