import re
import unittest

def is_right_syntax(amountText):
    price_expr_syntax = re.compile("[0-9,]")
    if price_expr_syntax.match(amountText):
        return True
    else:
        return False

def is_zero(amountText):
    if amountText[0] == 0:
        if len(amountText) == 1:
            return True
        else:
            return False
    else:
        return True
def is_not_comma(amountText):
    if amountText.isdigit():
        return True
    else:
        return False
        
def is_right_commas_syntax(amountText):
    comma_syntax = re.compile(r'(^((-)?([1-9]([0-9]{0,2})?(,\d{3})*|0)(\.\d+)?)$)')
    if comma_syntax.match(amountText):
        return True
    else:
        return False

def solution(amountText):
    
    if not is_right_syntax(amountText):
        print(amountText, 1)
        return False
    if not is_zero(amountText):
        print(amountText, 2)
        return False
    if is_not_comma(amountText):
        print(amountText, 3)
        return True
    else:
        if is_right_commas_syntax(amountText):
            print(amountText, 4)
            return True
        else:
            print(amountText, 5)
            return False
    

class TestCaasdf(unittest.TestCase):

    def test_one(self):
        self.assertEqual(solution("10000"), True)

    def test_two(self):
        self.assertEqual(solution("25,000"), True)
    
    def test_thr(self):
        self.assertEqual(solution("39,00"), False)