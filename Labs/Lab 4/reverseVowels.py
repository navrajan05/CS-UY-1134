def reverseVowels(str):

    lst = list(str)
    vowels = ['a','e','i','o','u']

    left = 0
    right = len(str) - 1



    while True:
        while lst[left] not in vowels and left < len(lst) - 1:
            left += 1
        while lst[right] not in vowels and right > 0:
            right -= 1
        if left > right:
            break

        lst[left], lst[right] = lst[right], lst[left]

        left += 1
        right -= 1

    return "".join(lst)
text = "lorem ipsum dolor sit amet"
print(reverseVowels(text))
print(text)