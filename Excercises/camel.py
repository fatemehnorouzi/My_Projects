camel= input("camelCase: ")
for c in camel:
    if c.isupper():
        print("_"+ c.lower(), end="")

    else:
        print(c, end="")
print()
