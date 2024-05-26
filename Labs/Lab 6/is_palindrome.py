def is_palindrome(str,low,high):
    if low >= high:
        return True
    else:
        return str[low] == str[high] and is_palindrome(str, low + 1, high - 1)

myStr = "1racecar2"

print(is_palindrome(myStr,0,len(myStr)-1))
print(is_palindrome(myStr,1,len(myStr)-2))