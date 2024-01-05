''' Mathematical Operators '''

# Addition

a = 10
b = 5
result = a + b
print(result)

# Substraction

a = 20
b = 8
result = a - b
print(result)

# Multiplication

a = 3
b = 4
result = a * b
print(result)

# Division  (Result will be always in float(decimal number))

a = 24
b = 3
result = a / b
print(result)

# Modulus (It will give the remainder)

a = 17
b = 4
result = a % b
print(result)

# Exponentials

a = 5
b = 2
result = a ** b
print(result)

''' Comparison operator ''' #? It will return boolean

# Equal to (==) :- It will show that the two values are equal or not

a = 10
b = 5
result = a == b
print(result)

# Not equal to (!=)

a = 3
b = 3
result = a != b
print(result)

# Greater than (>)

a = 12
b = 8
result = a > b
print(result)

# Less than (<)

a = 5
b = 8
result = a < b
print(result)

# Greater than or equal to (>=)

a = 12
b = 12
result = a >= b
print(result)

# Less than or equal to (<=)

a = 10
b = 15
result = a <= b
print(result)

''' Logic Opeartor '''

# Logical AND (and)

x = True
y = False
result = x and y
print(result)

# Logical OR (or)

x = True
y = False
result = x or y
print(result)

# Logical NOT (not)

x = True
result = not x
print(result)

'''Assignment Operator'''

# Assignment (=)

a = 20

# Additional assignment (+=)

a += 5
print(a)

# Multiplication assignment (*=)

a *= 4
print(a)

# Division assignment (/=)

a /= 3
print(a)

'''Membership Operator''' #? It will return boolean.

# 'in' operator

text = "Data Science course is available in PWSkills"
result = "Data Science" in text
print(result)

# 'not in' operator

text = "Data Science course is available in PWSkills"
result = "Data Science" not in text
print(result)

'''Identity Operator''' #? It will return boolean.

# 'is' operator

x = "PW Skills"
y = x
result = x is y
print(result)

# 'is not' operator

x = "PW Skills"
y = x
result = x is not y
print(result)

'''Precedence of operator'''

"""
1. Parentheses ()
2. Exponentiation **
3. Multiplication / Division / Modulus 
4. Addition / Substraction
5. Bitwise shift >> / <<
6. Comparison operators
7. Logical operator

"""

'''parentheses()'''

result = (2 + 3) * 4
print(result)

total = (10 + 5) + (8 / 2)
print(total)

'''Exponentiation'''

result = 2 ** 3
print(result)

'''Bitwise Shift operator'''

# Left shift

result = 8 << 2   # Shift 8 two bits to the left 
print(result)

# Right Shift

value = 32
shifted = value >> 2   # Shift 32 two bits to the right
print(shifted)
