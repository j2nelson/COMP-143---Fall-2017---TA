#acronym

def main():
    phrase = input("Enter a phrase: ")
    phrase = phrase.title()
    phrase = phrase.split()

    for i in range(len(phrase)):
        print(phrase[i][0], end = "")
main()