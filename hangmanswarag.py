import random

word= ["s","w","a","r","a","g"]


# def dictionary_words():
#     print("Ready To Guess ??? (y/n)")
#     usr = input("> ")
#     if usr == "y":
#         file = open('dictionary.txt')
#         words = file.read()
#         words = words.split()
#         return random.choice(words)
#     else:
#         quit()



def check():
    checker=["-","-","-","-","-","-"]
    string=" ".join(checker)
    print("usr",string)

    usr_input = input("Enter the word" )


    for i in word :
        if usr_input == "s":
            checker[0] = "s"
            print(" ".join(checker))
            usr_input = input("Enter the word")
            print(" ".join(checker))

        if usr_input == "w":
            checker[1] = "w"
            print(" ".join(checker))

            usr_input = input("Enter the word")
            print(" ".join(checker))

        if usr_input == "a":
            checker[2] = "a"
            checker[4] = "a"
            print(" ".join(checker))

            usr_input = input("Enter the word")
            print(" ".join(checker))

        if usr_input == "r":
            checker[3] = "r"
            print(" ".join(checker))

            usr_input = input("Enter the word")
            print(" ".join(checker))

        if usr_input == "g":
            checker[-1] = "g"
            print(" ".join(checker))

            usr_input = input("Enter the word")


    print("You win !!!!")



if __name__ == '__main__':
    check()
    # print(dictionary_words())