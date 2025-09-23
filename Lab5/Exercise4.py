def possibleWords(wordList, charList):
    # Chuyển charList thành set 
    available_chars = set(charList)

    result = []
    for word in wordList:
        # Kiểm tra nếu tất cả ký tự trong word đều có trong available_chars
        if set(word).issubset(available_chars):
            result.append(word)
    return result

def possible_words(word_list, char_list):
    result = []
    for word in word_list:
        if all(ch in char_list for ch in word):
            result.append(word)
    return result

def possibleWords(wordList, charList):
    # 1. Đếm số ký tự có sẵn trong charList
    available = {}
    for ch in charList:
        available[ch] = available.get(ch, 0) + 1

    result = []

    for word in wordList:
        # 2. Đếm số ký tự cần cho từ hiện tại
        needed = {}
        for ch in word:
            needed[ch] = needed.get(ch, 0) + 1

        # 3. Kiểm tra: mỗi ký tự trong word có đủ trong available không
        is_valid = True
        for ch in needed:
            if needed[ch] > available.get(ch, 0):  # thiếu ký tự
                is_valid = False
                break

        # 4. Nếu đủ ký tự thì thêm vào kết quả
        if is_valid:
            result.append(word)

    return result



print(possibleWords(['fat','tap','day','fun','man','ant','bag','aim'],['m','t','e','d','f','a','p','y','i']))