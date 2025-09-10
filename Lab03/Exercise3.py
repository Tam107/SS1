def pythagoreanTriplets(num):
    triplets = []
    for a in range(1, num + 1):
        for b in range(a, num + 1):
            c2 = a * a + b * b
            c = int(c2 ** 0.5)
            if c <= num and c * c == c2:
                triplets.append((a, b, c))
    result = "\n".join(str(t) for t in triplets)
    print(result)



print(pythagoreanTriplets(10))