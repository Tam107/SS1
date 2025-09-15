def caesarEncoder(word, offset):
    """
    Encrypts an uppercase word using Caesar cipher with the given offset.
    """
    result = []
    for char in word:
        # Shift character and wrap around using modulo
        shifted = (ord(char) - ord('A') + offset) % 26 + ord('A')
        result.append(chr(shifted))
    return ''.join(result)


def caesarEncoder_listcomp(word, offset):
    check = [chr(((ord(word[1]) - ord('A') + offset) % 26) + ord('A'))]
    print("check number", check)

caesarEncoder_listcomp('hello', 3)

"""
offset = 3
print((25 + offset) % 26)  # 2  (Z -> C)
print((0 - 1) % 26)        # 25 (A - 1 -> Z)
"""