from Codewars.Middle_Permutation.solution import middle_permutation
import unittest

class MyTestCase(unittest.TestCase):
    def expectEqual(self, first, second, msg=None):
        with self.subTest():
            self.assertEqual(first, second, msg)

class TestMA(MyTestCase):
    def test_ma(self):
        self.expectEqual(middle_permutation("abc"),"bac")
        self.expectEqual(middle_permutation("abcd"),"bdca")
        self.expectEqual(middle_permutation("abcdx"),"cbxda")
        self.expectEqual(middle_permutation("abcdxg"),"cxgdba")
        self.expectEqual(middle_permutation("abcdxgz"),"dczxgba")


if __name__ == '__main__':
    unittest.main()