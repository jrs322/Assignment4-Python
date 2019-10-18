import unittest
from stack import Stack

class StackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_base_stack_empty(self):
        test_stack = Stack()
        self.assertEqual(0, test_stack.size())

    def test_push_increases_size(self):
        test_stack = Stack()
        test_stack.push(StackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    def test_peek_size_remains(self):
        test_stack = Stack()
        test_stack.push(StackTestCase.ITEM_1)
        self.assertEqual(StackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = Stack()
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_pop_empty_stack(self):
        test_stack = Stack()
        self.assertEqual(None, test_stack.pop())

    def test_pop_single_item(self):
        test_stack = Stack()
        test_stack.push(StackTestCase.ITEM_1)
        self.assertEqual(StackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    def test_last_in_first_out(self):
        test_stack = Stack()
        test_stack.push(StackTestCase.ITEM_1)
        test_stack.push(StackTestCase.ITEM_2)
        test_stack.push(StackTestCase.ITEM_3)
        self.assertEqual(3, test_stack.size())

        self.assertEqual(StackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(StackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(StackTestCase.ITEM_1, test_stack.pop())


if __name__ == '__main__':
    unittest.main()
