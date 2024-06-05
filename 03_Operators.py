# Arithmetic operator

a = 20
b = 3
print (a + b)
print (a - b)
print (a * b)
print (a / b) # Gives the quotient
print (a % b) # Gives the remainder

print (3 ** 2) # 3 Power 2

#! Comparison operator:- return boolean values

print(2 == 23)
print (4 // 3) # Floor operator:- gives nearest integer
print(2 != 3)
print(10 > 2)
print(10 < 2)
print(10 <= 10)
print(10 >= 1)
print(10 >= 10)
print(10 >= 12)

#! Logical operator:- True = 1 and False = 0

print (True and True) # True
print (False and True) # False
print (True and False) # False
print (False and False) # False

print (True or True) # True
print (True or False) # True
print (False or True) # True
print (False or False) # False

#! Membership operator :- It will show that particular data is available in object or not.

a = "PWSkills"
print ("P" in a) # True
print ("Data" in a) # False

b = ["data", "Science", "Ajay"]
print ("data" in b) # True
print ("data1" in b) # False

#! Identity operator :- Compare the memory location of two object

x = 2
y = 3

print (x is y) # False
print (y is x) # False

p = "PW SKills"
q = p

print (p is q) # True
print (q is p) # True

#! bitwise operator :- operations at binary or 0 and 1 level

print (bin(10)) #? It will give binary representation of any number
print (10 & 10)

print(bin(18))
print(bin(3))
print (18 & 3)

#! Negation :- Give next integer with negative sign

print (~100)

#! Bitwise xor :- return 1 when exactly one operand is 1

print (5 ^ 3)

#! Shift operator
#? Left shift operator (<<):- put zeros on the right

print (35 << 3)

#? Right shift operator (>>):- Remove zeros from right

print (280 >> 3)

#! Order of percedence :- execution will start from left
#? Always parenthesis

print (2 + 3 - 5)
print ((4 + 5) - 4)