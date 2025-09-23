def topKWords(sentence, k):
    result_dict = {}
    for word in sentence.split():
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    # Sắp xếp:
    #   - Ưu tiên frequency giảm dần (-value)
    #   - Nếu bằng nhau thì theo alphabet tăng dần (key)
    sorted_items = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))

    # Lấy top k
    return sorted_items[:k]


print(topKWords('i love python i love coding', 2))
print(topKWords('the day is sunny the the the sunny is is', 3))