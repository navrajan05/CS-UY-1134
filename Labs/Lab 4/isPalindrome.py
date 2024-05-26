def is_palindrome(str):
    left = 0
    right = len(str) - 1

    palindromic = True

    while left < right:
        if str[left] != str[right]:
            palindromic = False

        left += 1
        right -= 1

    return palindromic


print(is_palindrome("raccar"))
print(is_palindrome("racecar"))
print(is_palindrome("race2car"))