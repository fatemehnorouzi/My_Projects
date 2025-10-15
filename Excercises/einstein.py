mass= int(input("Enter the mass amount: "))

def calc(m):
    C= 300000000
    E= m * (C**2)
    return E


print (f"The equivalent number of Joules is: {calc(mass)}.")
