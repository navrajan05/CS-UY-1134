def can_construct(word, letters):
    # using a list for convenience
    letter_list = []

    for char in letters:
        letter_list.append(char)

    found = False

    for currentChar in word:
        found = False
        for i in range(len(letter_list)):

            if letter_list[i] == currentChar:
                found = True
                letter_list.pop(i)
                break

        if not found: break

    return found


print(can_construct("apples", "aplespl"))
