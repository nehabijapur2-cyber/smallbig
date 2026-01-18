def smallest_largest(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    result = f"A : {a}\nB : {b}\nC : {c}\nSmallest : {smallest}\nLargest : {largest}"
    return result

if __name__ == "__main__":
    print(smallest_largest(3, 7, 5))
