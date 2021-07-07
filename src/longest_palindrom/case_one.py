import unittest


def get_longest_palindrom(pharse: str):

    global result

    # using two pointer
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(pharse) and pharse[left] == pharse[right]:
            left -= 1
            right += 1
        return pharse[(left + 1):right]

    if len(pharse) < 2 or pharse == pharse[::-1]:
        return pharse

    for i in range(len(pharse) - 1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)

    return result




class testClass(unittest.TestCase):
    pass
