grocery_list = {}

while True:
    try:
        item = input().upper().strip()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        print()

        for product in sorted(grocery_list):
            print(f"{grocery_list[product]} {product}")
        break