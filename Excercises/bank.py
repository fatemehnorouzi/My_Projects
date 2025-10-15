while True:
    greet= input("Greeting: ")
    if greet.startswith("Hello"):
        output= print("$0")
    elif greet.startswith("H"):
        output= print("$20")
    else:
        output= print("$100")
