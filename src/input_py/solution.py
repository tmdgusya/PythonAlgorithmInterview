import unittest
from collections import deque

import unittest
from collections import deque

def solution(input):
    result = ""
    command_list: list = input.split("\n")
    show, day = command_list[0].split()

    result = command_list[0]

    show = int(show)
    day = int(day)

    is_show = [0 for i in range(day)]

    cur_day = 0
    is_negative = False
    for i in range(len(command_list)-1):
        command = command_list[i+1]
        
        if command == "SHOW":
            if cur_day >= len(is_show) or is_show[cur_day] >= show or is_negative:
                result += "\n0"
            else:
                is_show[cur_day] += 1
                result += "\n1"
        elif command == "NEXT":
            result += "\n-"
            next
        elif command == "EXIT":
            result += "\nBYE"
        elif command == "NEGATIVE":
            is_negative = True
            result += "\n0"
        else:
            result += "\nERROR"
        cur_day += 1
    return result
    


class TestSolution(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution("1 3\nSHOW\nNEXT\nEXIT"), "1 3\n1\n-\nBYE")

    def test_two(self):
        self.assertEqual(
            solution("2 3\nSHOW\nNEGATIVE\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nEXIT", 
            ), "2 3\n1\n0\n0\n-\n0\n0\n-\n0\n-\n1\n1\n-\n1\n0\nBYE")