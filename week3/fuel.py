while True:
    try:
        fraction = input("Fraction: ").split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        if x <= y:
            percent = (x / y) * 100
            break
    except (ValueError, ZeroDivisionError, IndexError):
        pass

result = round(percent)

if result <= 1:
    print("E")
elif result >= 99:
    print("F")

else:
    print(f'{result}%')