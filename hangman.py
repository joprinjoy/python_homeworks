import random
words= ['one','two','three','four']
show_word_dict = {} 
list_word =[] #word converted to list
man_hanged = "+-----+\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n   -----\n --------"
man_hang_half = "+-----+\n |    |\n O    |\n/|\\   |\n      |\n      |\n   -----\n --------"
man_hang_start = "+-----+\n |    |\n O    |\n      |\n      |\n      |\n   -----\n --------"

def start():
    print("Welcome To Hangman\n")
    print(man_hanged)
    print("\n Enter START to start or QUIT to quit the game:")
    ignition = input(">")
    ignition = ignition.lower()
    if ignition == "start":
        game_word = select_word()
        game_room(game_word)

    else:
        quit()

   
def print_hangman(man):
    print(man)  

def game_room(game_word):
    print("guess the word")
    res=guess(game_word)
    if res == True:
        print('Congratulations ! You saved a life') 
    else:
        print("You killed Him")
        print("Do you want to try again?")
        retry =input('>')
        if yes in retry:
            start()
        else:
            quit()

    
    
def select_word():
    print("lets start")
    file = open('words.txt')
    file =file.read()
    file = file.split()
    wd = random.choice(file)
    word_mask(wd)
    return(wd)
    

def word_mask(wd):
    p=1
    for i in wd:
        show_word_dict.update({p:"-"})
        p+=1

def guess(word):
    print(word) #test
    char_count = len(word)   
    chance = 10
    input_word = ""
    for j in range (0,chance):
        player_input = str(input(">"))
        if player_input:
            if player_input in word and player_input not in input_word:
                
                print("Hurray thats correct!!")
                input_word = input_word+player_input
                show_word = show_the_progress(word,player_input)
                print(show_word)
                print_hangman(man_hang_start)
            else:
                show_word = show_the_progress(word,player_input)
                print(show_word)
                print("Oh noo..try again")
                show_hangman(j,char_count)  

            # if len(input_word) == char_count:
            if word == show_word:
                print(f"input word:{len(input_word)} char count:{char_count}")
                return True   
          
    if len(input_word) != char_count: 
        return False       




def show_the_progress(word,player_input):
    list_word = list(word)
    list_word_len = len(list_word)  
    for position in range(1,list_word_len+1):
        if  list_word[position-1]  == player_input:
            show_word_dict.update({position:player_input})
    show_word_list =list(show_word_dict.values())
    show_word_to_send = ''.join(show_word_list)
    return (show_word_to_send)



def show_hangman(iteration,char_count):
    if iteration >(char_count/2) and iteration < char_count :
        print_hangman(man_hang_half)
    elif iteration > char_count-1:
        print_hangman(man_hanged)
    else:
        print_hangman(man_hang_start)
    
if __name__=="__main__":
    start()
