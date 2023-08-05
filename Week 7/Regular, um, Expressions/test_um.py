from um import count

def main():
    test_case1()
    test_case2()
    test_case3()


def test_case1():
    assert count("thank you, Um, I love you.") == 1
    assert count("Um, kase naman, um") == 2

def test_case2():
    assert count("yummiya") == 0
    assert count("yummuh") == 0

def test_case3():
    assert count("Hello um okay ka lang ba?") == 1
    assert count("hello world") == 0

if __name__ == "__main__":
    main()
