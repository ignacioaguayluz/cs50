def main():
    user = input("What time is it? ")
    meal_time = convert(user)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19:
        print("dinner time")
    


def convert(time):
    hours, minutes = time.strip().split(":")

    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()