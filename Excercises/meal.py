def main():
    time= input("what time is it? ")
    new_time= convert(time)

    if (new_time >= 7.00) and (new_time <= 8.00):
        print("Breakfast time")
    elif (new_time >= 12.00) and (new_time <= 13.00):
        print("Lunch time")
    elif (new_time >= 18.00) and (new_time <= 19.00):
        print("Dinner time")



def convert(time):
    hour, minute= time.split(":")
    hour=int(hour)
    minute= (float(minute))/60
    new_time= hour+minute
    return new_time


if __name__ == "__main__":
    main()
