import random

def create_permutation(n):

    permutation = []
    for i in range(n):
        index = random.randint(0,i)
        permutation.insert(index, i)

    return permutation

def scramble_word(word):
    scrambled_word = ""
    permutation = create_permutation(len(word))

    for i in permutation:
        scrambled_word = scrambled_word + word[permutation[i]]

    return scrambled_word

def guessing_game(word):
    scrambled_word = scramble_word(word)

    print("Unscramble the word: " + scrambled_word)

    for i in range(3):
        guessNo = str(i+1)
        guess = input("Try #" + guessNo +":")
        if guess == word:
            print("Yay, you did it!")
            break
        else: print ("Wrong!")


print(create_permutation(7))
print(scramble_word("pokemon"))
guessing_game("hello")
