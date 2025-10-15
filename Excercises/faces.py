def convert(str):
    str= str.replace(":)", "🙂")
    str= str.replace(":(", "🙁")
    return str


def main():
    Sentence= input("Enter your desired sentence: ")
    New_sentence= convert(Sentence)
    print(New_sentence)


main()