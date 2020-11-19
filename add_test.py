from typing import List


def add(numbers: List[int]) -> int:
    result = 0
    for number in numbers:
        result += number
    return result


def test_add():
    assert(add([1, 4, 5]) == 10)
    assert(add([0, 0]) == 0)
    assert(add([100]) == 100)
    assert(add([-10, -10, 10]) == -10)


def is_big_number(a: int) -> int:
    if a >= 100:
        return True
    return False


def test_is_big_number():
    assert(is_big_number(1000))
    assert(is_big_number(100))
    assert(not is_big_number(99))
    assert(not is_big_number(0))
    assert(not is_big_number(-10000))
