from Codewars.Find_the_unknown_digit.solution import solve_runes
import unittest

class MyTestCase(unittest.TestCase):
    def expectEqual(self, first, second, msg=None):
        with self.subTest():
            self.assertEqual(first, second, msg)

class TestMA(MyTestCase):
    def test_ma(self):
        self.expectEqual(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ")
        self.expectEqual(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ")
        self.expectEqual(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ")
        self.expectEqual(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ")
        self.expectEqual(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ")
        self.expectEqual(solve_runes("??*1=??"), 2, "Answer for expression '?*11=??' ")


if __name__ == '__main__':
    unittest.main()



