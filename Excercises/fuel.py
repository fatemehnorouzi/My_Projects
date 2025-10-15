while True:
    try:
        fraction= input("Fraction: ")
        x, y= fraction.split("/")
        x=int(x)
        y=int(y)

        if y == 0 or x<0 or y<0 or x>y:
            continue
        z= (x/y)*100
        if z >= 99 and z <= 100:
            print("F")
        elif z>= 0 and z<= 1:
            print("E")
        else:
            print(f"{round(z)}%")
        break
    except(ValueError, ZeroDivisionError):
        pass