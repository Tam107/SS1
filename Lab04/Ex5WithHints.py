from numpy import char


def is_vowel(char):
    return char.lower() in 'aeiou'


def findFirstVowel(word):
    for i, ch in enumerate(word):  # loop with index
        if is_vowel(ch):
            return i
    return -1


def findFirstVowel1(word: str) -> int:
    vowels = "aeiouAEIOU"
    for i, ch in enumerate(word):
        if ch in vowels:
            return i
    return -1


# page 2
def convertWordToPigLatin(word: str) -> str:
    idx = findFirstVowel(word)

    if idx == -1:  # no vowel
        return "yayyay"
    elif idx == 0:  # starts with a vowel
        return word + "yay"
    else:  # starts with consonant(s)
        return word[idx:] + word[:idx] + 'ay'


def convertSentenceToPigLatin(sentence):
    sentence = sentence.split()
    pig_words = [convertWordToPigLatin(w) for w in sentence]
    return " ".join(pig_words)


if __name__ == '__main__':
    print(findFirstVowel('duck'))
    print(findFirstVowel('egg'))
    print(findFirstVowel('myths'))
    print(convertWordToPigLatin('duck'))
    print(convertWordToPigLatin('smile'))
    print(convertSentenceToPigLatin('Hello I am a Python programmer'))
