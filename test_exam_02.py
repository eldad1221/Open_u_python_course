import unittest
from exam_02 import max_matrix, is_identity, big_small


MATRIX_01 = [
    [1, 2, 3, 4, 5, 6, 7],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1]
]


class MyTestCase(unittest.TestCase):
    def test_2_3(self):
        self.assertEqual(True, is_identity(mat=MATRIX_01, x=2, size=3))

    def test_max_matrix(self):
        self.assertEqual(5, max_matrix(mat=MATRIX_01))

    def test_big_small(self):
        self.assertEqual(True, big_small("ZaBWzbAw"))
        self.assertEqual(True, big_small("AAaa"))
        self.assertEqual(False, big_small("bAaa"))
        self.assertEqual(False, big_small("Aaa"))


if __name__ == '__main__':
    unittest.main()
