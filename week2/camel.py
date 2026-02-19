def main():
    name = input("camelCase: ")
    print("snake_case:", camel_case(name))

def camel_case(word):
    snake_case = ""

    for letter in word:
        if letter.isupper():
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    
    return snake_case

main()