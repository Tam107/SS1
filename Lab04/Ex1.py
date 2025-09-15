def dotProduct(a,b) -> int:
    """
    Calculate the dot product of two vectors a and b.

    :param a: List of integers representing the first vector.
    :param b: List of integers representing the second vector.
    :return: The dot product of vectors a and b.
    zip(a, b) sẽ ghép cặp từng phần tử từ a và b.
    Ví dụ: zip([1,2,3], [4,5,6]) → [(1,4), (2,5), (3,6)]
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")

    return sum(x * y for x, y in zip(a, b))


def dotProduct_loop(a, b) -> int:
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

def dotProduct_listcomp(a, b) -> int:
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")
    return sum([a[i] * b[i] for i in range(len(a))])



print(dotProduct([1,2,3,4,5],[10,20,30,40,50]))

