"""python Arithmetic Operators(+, -, *, /, %, //, **) //-Floor division(not give desible value), **-Exponentiation ex-2 ki power10(2**10) , %-Modulus(8%3=2)"""

#print(8%3)  # Modulus operator
#print(13//3)  # Floor division operator
#print(2**10)  # Exponentiation operator

"""python Comparison Operators(==, !=, >, <, >=, <=) != #-Not equal to, ==-Equal to, >-Greater than, <-Less than, >=-Greater than or equal to, <=-Less than or equal to
"""
#print(3!=10)

"""#python Logical Operators(and, or, not) #and-If both operands are true then it returns true, or-If any one of the operands is true then it returns true, not-If the operand is false then it returns true"""

# print(3<2 or 2<3)  # Logical OR operator
# print(3<2 or 3>7)  # Logical OR operator with both conditions false
# print(not(3>4 or 3<4))  # Logical NOT operator

"""Assignment Operators(=, +=, -=, *=, /=, %=, //=, **=) #= is used to assign a value to a variable, += is used to add and assign, -= is used to subtract and assign, *= is used to multiply and assign, /= is used to divide and assign, %= is used to modulus and assign, //= is used to floor division and assign, **= is used to exponentiation and assign
a=6 is a assignment operator that assigns the value 6 to the variable a on the left side of the operator."""
# a = 6
# a += 2  # Add and assign
# # a -= 3  # Subtract and assign
# # a *= 4  # Multiply and assign
# print(a)  # Output: 8

"""identity Operators(is, is not) #is-If both operands refer to the same object then it returns true, is not-If both operands do not refer to the same object then it returns true"""
# a = 1234
# b = "1234"
# print(a is not b)  # Identity operator (is)

"""Bitwise Operators(&, |, ^, ~, <<, >>) #&-Bitwise AND, |-Bitwise OR, ^-Bitwise XOR, ~-Bitwise NOT, <<-Left shift operator, >>-Right shift operator"""

# Bitwise AND operator(&), 1&1=1, 0&0=0, 1&0=0, 0&1=0
# a=10
# b=8
# print(a & b)  # Bitwise AND operator, 
# print(bin(15))  # Binary representation of 15

# or operator(|) 1|0 = 1, 0|1 = 1, 1|1 = 1, 0|0 = 0
# a = 10
# b = 8
# print(a | b)  # Bitwise OR operator

#xor operator(^), 1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1
# a = 10
# b = 8
# print(a ^ b)  # Bitwise XOR operator

#right shift operator(>>), 1 >> 1 = 0, 0 >> 0 = 0, 1 >> 0 = 1, 0 >> 1 = 0
# print(10 >> 2)  # Right shift operator, 10 in binary is 1010, right shifting by 2 gives 0010 which is 2 in decimal

#left shift operator(<<), 1 << 1 = 10, 0 << 0 = 0, 1 << 0 = 1, 0 << 1 = 0
#print(10 << 2)  # Left shift operator, 10 in binary is 1010, left shifting by 1 gives 10100 which is 20 in decimal

"""Membership Operators(in, not in) #in-If the value is found in the sequence then it returns true, not in-If the value is not found in the sequence then it returns true"""
a = "Hello World"
# print("P" in a)  # Membership operator (in)
# print("e" in a)  # Membership operator (in)
# print("H" not in a)  # Membership operator (not in)

