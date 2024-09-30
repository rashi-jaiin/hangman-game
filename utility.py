def draw_blanks(word):
    
    for letter in word:
        print(letter, end=' ')
    print()


def fill_blanks(word, blank_word, inp):
    for index in range(0,len(word)):
        if inp == word[index]:
            blank_word = blank_word[:index] + inp + blank_word[index+1:]

    return blank_word


def game_over(string):
    print(string)
    print("Game Over")


