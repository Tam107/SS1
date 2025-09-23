"""
Most frequent character in a string
In a string, the most frequent character is the character that the highest frequency in a string, except the space character.
Write a Python3 function named mostFrequentChar(sentence) that take a sentence as the input and returns the most frequent character in the sentence. If there are many characters that have the same highest frequency, the function will return the left most character.
For example:
mostFrequentChar('i love python') will return character 'o'
mostFrequentChar('apple is good') will return character 'p'
We assume that the input sentence contains only lowercase characters and all inputs data are correct. Please refer to the example table about the input and output of the function.
"""
from collections import Counter


# first way
def mostFrequentChar(str):
    count = {}
    for char in str:
        if char != ' ':
            count[char] = count.get(char,0) + 1
    if not count:
        return ' '
    max_count = max(count.values())
    for ch in str:
        if ch != ' ' and count[ch] == max_count:
            return ch

# second way

def mostFrequentChar2(sentence):
    filtered = sentence.replace(' ', '')
    counter = Counter(filtered)

    max_freq = max(counter.values())

    for ch in filtered:
        if counter[ch] == max_freq:
            return ch



print(mostFrequentChar('i love python'))
