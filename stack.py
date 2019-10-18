class Stack:
    """
    See Stack data structure description here: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """
    def __init__(self):
        self._stack_items = []

    def push(self, item):
        """
        Add item to the stack.
        Raises a TypeError if item equals None.
        """
        if item == None:
            raise TypeError("Stack will not store an object of NoneType.")
        self._stack_items.append(item)

    def pop(self):
        """
        If the stack contains at least one item, remove the last
        item that was added to the stack and return it.
        Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items.pop()
        else:
            return None

    def peek(self):
        """
        If the stack contains at least one item, return the value of last
        item that was added to the stack. Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items[-1]
        else:
            return None

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self._stack_items)
