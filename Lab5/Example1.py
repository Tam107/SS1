def wordCount(sentence: str) -> tuple:
    words = sentence.split()
    word_count = len(words)

    # Đếm ký tự không tính space
    char_count = sum(len(w) for w in words)

    return word_count, char_count
print(wordCount("I love Python"))      # (3, 11)