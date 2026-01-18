from num import smallest_largest

def test_case1():
    assert smallest_largest(3, 7, 5) == "A : 3\nB : 7\nC : 5\nSmallest : 3\nLargest : 7"

def test_case2():
    assert smallest_largest(10, 2, 15) == "A : 10\nB : 2\nC : 15\nSmallest : 2\nLargest : 15"

def test_case3():
    assert smallest_largest(-1, -5, 0) == "A : -1\nB : -5\nC : 0\nSmallest : -5\nLargest : 0"
