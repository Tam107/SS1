def isPalindrome(s: str):
    check = s.reverse()
    if check == s:
        return True
    return False


def isPalindrome(s: str):
    if s == s[::-1]: return 'YES'
    return 'NO'


def is_palindrome_reversed(s):
    reversed_s = ''.join(reversed(s))
    return reversed_s == s