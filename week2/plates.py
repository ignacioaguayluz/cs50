def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    
    if not s[:2].isalpha():
        return False
    
    number_started = False
    
    for char in s[2:]:
        if not char.isalnum():
            return False
        
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        else:
            if number_started:
                return False
    
    return True
main()