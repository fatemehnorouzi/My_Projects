Expression= input("Expression: ")
x, y, z= Expression.split(" ")

x= float(x)
z= float(z)

if y== "+":
    number= x + z
elif y== "-":
    number= x - z
elif y== "*":
    number= x * z
elif y== "/":
    number= x / z

print(f"{number:.1f}")