#  python buit-in functions : https://www.programiz.com/python-programming/methods/built-in
# Convert to binary(Ob), octal(Oo), Hexadecimal(Ox)
# used built-in functions bin(), oct() and hex()
decimal = int(input("Enter a decimal number :"))
print("The decimal value of",decimal, "is :")
print(bin(decimal), "in binary")
print(oct(decimal), "in octal")
print(hex(decimal), "in hexadecimal")