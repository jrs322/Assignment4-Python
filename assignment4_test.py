from assignment4 import UniqueStack
from assignment4 import LimitedStack
from assignment4 import RotatingStack
from assignment4 import LimitedStack
import unittest


class STC(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_unique_behavior(self):
        test_stack = UniqueStack()
        test_stack.push(STC.ITEM_1)
        with self.assertRaises(ValueError):
            test_stack.push(STC.ITEM_1)
        self.assertEqual(STC.ITEM_1, test_stack.pop())

    def test_limited_behavior(self):
        test_stack = LimitedStack(2)
        test_stack.push(STC.ITEM_3)
        test_stack.push(STC.ITEM_3)
        with self.assertRaises(test_stack.LimitedStackOverflowError):
            test_stack.push(STC.ITEM_1)

    def test_rotating_behavior(self):
        test_stack = RotatingStack(2)
        test_stack.push(STC.ITEM_1)
        test_stack.push(STC.ITEM_1)
        test_stack.push(STC.ITEM_2)
        self.assertEqual(STC.ITEM_2, test_stack.peek())

if __name__ == '__main__':
    unittest.main()
    print("Jobs Done")
