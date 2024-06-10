# random to select random word 
import random  
#importing sleep to improve the use erxperience
from time import sleep
show_word_dict = {} 
list_word =[] #word converted to list
#image construct for different stages of hanging
man_hanged = "+-----+\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n   =====\n ========"
man_hang_half = "+-----+\n |    |\n O    |\n/|\\   |\n      |\n      |\n   =====\n ========"
man_hang_start = "+-----+\n |    |\n O    |\n      |\n      |\n      |\n   =====\n ========"

"""function calls function to set the game word and function for main game.
its asks gamer to choose to start o quit the game. once game word is recieved, game starts"""
def start():
    print("Welcome To Hangman\n")
    print(man_hanged)
    print("\n Enter START to start or QUIT to quit the game:")
    ignition = input(">")
    ignition = ignition.lower()

    if ignition == "start":
        print("lets start")
        #game room is callled
        game_room()
    else:
        quit()

   
def print_hangman(man):
    print(man)  

#body of the game. here we call the guess and game ends here
def game_room():
    game_word = select_word()
    #testing purpose
    # print(f"word:{game_word}") 

    print("The challenge is to find the masked word . number of - indicates the number of caracters in word.")
    #execution will pause for 1 sec
    sleep(1)
    print("You got 10 attempts to figure out the word")
    sleep(1)
    print("Every false entries will let the man suffer to die")
    sleep(1)
    print("\n")
    print("Guess the word")
    sleep(1)
    #calling guess function which perform as game engine . guess will return the result of the game
    result =guess(game_word)
    if result == True:
        print('Congratulations ! You saved a life') 
        # giving an option to gamer ,if want to retry 
        retry()
    else:
        print("You killed Him")
        print("\nCorrect word \t",game_word)
        retry()

#select word is function select and return  the word to game_word
def select_word():
    #words.txt is a file located in /usr/share/dict/words
    file = open('words.txt')
    file =file.read()
    file = file.split()
    #setting an empty list to store filtered list of words from file. then it only contains words with charcters more than 3
    filtered_words = []
    for word in file:
        if len(word) > 3:
            filtered_words.append(word)

    #using random.choise() to pick random words from list
    word_from_file = random.choice(filtered_words)

    #setting rule to allow only words with number of characters more than 3
    if len(word_from_file) < 3 :
        select_word()
    else:
        #removing 's from words as many words in the file having it
        if '\'' in word_from_file:
            word_from_file = word_from_file[-2]

        #handling the input allowing any case   
        word_from_file = word_from_file.lower()

        #masking the word
        word_mask(word_from_file)
        return(word_from_file)
    
#masking the word nand hinting the numbe rof characters to gamer
#dictionary usage can be eliminated
def word_mask(word_from_file):
    p=1
    for i in word_from_file:
        show_word_dict.update({p:"-"})
        p+=1

##engine of the game takes input from gamer and check whether it is correct or not and return result
def guess(game_word):
    #showing an empty word to hint the gamer with  number of characters in word
    masked_word = show_the_progress(game_word,1)
    print("\n" ,masked_word,"\n")
    sleep(1)
    print_hangman(man_hang_start) 
    char_count = len(game_word) 
    #setting up the number of chances user got to solve the word   
    chance = 10
    #empty string to save the inputs from user to use later
    input_word = ""
    print(" if you wish to change the word , Enter NEXT  or start game by inputing first character")
    for j in range (0,chance):
        chances_remaining = chance - j
        print(f"chances Remaining: {chances_remaining}")
        
        player_input = (input(">"))
        player_input = player_input.lower()
        #if input have a value inside 
        if player_input:
            if player_input == 'next':
                retry()
            #checking whether the input is in game word and not entered already
            if player_input in game_word and player_input not in input_word:  
                #joining the inputs
                input_word = input_word+player_input

                #if guess was correct the character will appear in the right position
                show_word = show_the_progress(game_word,player_input)
                print_hangman(man_hang_start)
                print(show_word)
                print("Hurray thats correct!!")
                
            else:
                show_word = show_the_progress(game_word,player_input)
                #setting the right picture
                show_hangman(j,char_count) 
                print(show_word) 
                print("Oh noo..try again")
            #always checking whether the game word and show word is same or not   
            if game_word == show_word:
                return True   
    #seting the failure of game with the number of entries in input word     
    if len(input_word) != char_count: 
        return False       

#to show the progress in the terminal after every guess
def show_the_progress(game_word,player_input):
    list_word = list(game_word)
    list_word_len = len(list_word)  
    for position in range(1,list_word_len+1):
        if  list_word[position-1]  == player_input:
            show_word_dict.update({position:player_input})
    show_word_list =list(show_word_dict.values())
    show_word_to_send = ''.join(show_word_list)
    return (show_word_to_send)

#render the image of hangman as per the result of enties
def show_hangman(iteration,char_count):
    if iteration >(char_count/2) and iteration < char_count :
        print_hangman(man_hang_half)
    elif iteration > char_count-1:
        print_hangman(man_hanged)
    else:
        print_hangman(man_hang_start)
#retry fuction let the gamer start again    
def retry():

    print("Do you want to try again? Y/N")
    user_input =input('>')
    user_input = user_input.lower()
    if 'y' in user_input:
        game_room()
    elif 'n' in user_input:
        quit()
    else:
        retry()

if __name__=="__main__":
    start()
