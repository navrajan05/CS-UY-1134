def count_lowercase(s, low, high):
    def is_lowercase_letter(n):
        return n.isalpha() and n.islower()

    if low > high:
        return 0
    else:
        if is_lowercase_letter(s[low]): return count_lowercase(s, low + 1, high) + 1
        else: return count_lowercase(s, low + 1, high)


def is_number_of_lowercase_even(s, low, high):
    def is_lowercase_letter(n):
        return n.isalpha() and n.islower()

    if low == high:
        return not is_lowercase_letter(s[low])
    else:
        # Using XOR because it's too early in the morning for more than one line of code
        return is_lowercase_letter(s[low]) ^ is_number_of_lowercase_even(s, low + 1, high)


'''

myString = "Are you suggesting coconuts migrate?"
print(count_lowercase(myString, 0, len(myString) - 1))
print(len(myString))

'''