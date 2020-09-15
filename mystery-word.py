import random




# def difficulty():
    # dif = input("Choose difficulty: Easy, Normal, or Hard.")
    # if difficulty == "easy" & "Easy":
        
    # elif difficulty == "normal" & "Normal":

    # elif difficulty == "hard" & "Hard":
    
    # else:
    #     return difficulty
    


def get_words(file):
    with open (file, "r") as f:
        file_contents = f.read()

    word_list = file_contents.lower().split()
    # print(word)
    return random.choice(word_list)



def start_game():
    turns = 8
    guesses = False
    g_letters = []
    
    word = get_words(file)
    # print("The words has", len(word), "letters.")
    print(len(word) * "_ ")

    while guesses == False and  turns > 0:
        # print(len(word) * "_ ")
        print('You have ', str(turns) + ' tries.')
        guess = input('Choose a letter: ').lower()
        if len(guess) == 1:
            if guess in word:
                print("Great guess!")
                g_letters.append(guess)
            elif guess in g_letters:
                print('You guessed that letter already.')
            else:
                guess not in word
                print('Sorry try again')
                g_letters.append(guess)
                turns -= 1
            
            # if len(guess) == 0:
            #     print('Game Over!')
            #     pass
        
        status = ''
        if guesses == False:
            for letter in word:
                if letter in g_letters:
                    status += letter
                else:
                    status += ' - '
            print(status)








if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        start_game()
    else:
        print(f"{file} does not exist!")
        exit(1)



#         import random

# f = open('words.txt')
# word_list = f.read().split()

# def get_word():
#     word = random.choice(word_list)
#     return word.lower()


# def game(file):
#     get_word()
#     print(get_word)


# if __name__ == "__main__":
#     word = (get_word())
#     game(word)
