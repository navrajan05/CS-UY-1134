def isVowel(chara):
    if chara in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False


def isConsonant(chara):
    if chara.isalpha() and not chara.isVowel():
        return True
    else:
        return False


def vc_count(word, low, high):
    if low == high: vowels, consonants = 0, 0
    else: vowels, consonants = vc_count(word, low + 1, high)

    if word[low].isVowel(): vowels += 1
    if word[low].isConsonant(): consonants += 1

    return vowels, consonants
