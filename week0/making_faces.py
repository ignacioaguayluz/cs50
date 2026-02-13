def main():
    text = input('Enter text: ')
    
    converted = convert(text)
    print(converted)


def convert(text):

    text = text.replace(":)", "😃")
    text = text.replace(":(", "☹️")
    return text

main()