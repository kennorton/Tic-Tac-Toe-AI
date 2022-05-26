""" Add a test for notable functions bellow """

import unittest
import functions as f


class FunctionTesting(unittest.TestCase):
    
    def test_take_move(self):
        old = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        new = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(f.take_move(old, 1, 1), new)

if __name__ == '__main__':
    unittest.main()
