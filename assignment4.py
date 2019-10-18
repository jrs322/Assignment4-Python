from stack import Stack

class UniqueStack(Stack):
    """
    UniqueStack has the same methods and functionality as Stack, but will only store one
    copy of a particular item at a time.
    If push is called with an item that is already in the UniqueStack, a ValueError should be raised
    with an appropriate error message.
    If push is called where item equals None, a TypeError should be raised like in the base class.
    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. New versions of __init__(), push(), and pop() should be sufficient.
    Hint: One option to implement this is to maintain an internal set() alongside the internal list.
    """
    # Add mehods here. Remove this comment and the next line before doing so.
    def __init__(self):
        super().__init__()
        self.internal_values = []
    def push(self, item):
        list = self.internal_values
        if item == None:
            raise TypeError
        for i in list:
            if i == item and i != None:
                raise ValueError
        super().push(item)
        list.append(item)

    def pop(self):
        list = self.internal_values
        temp = super().pop()
        for i in list:
            if i == temp and i != None:
                list.remove(temp)
        return temp

class LimitedStack(Stack):
    """
    A LimitedStack has the same methods and functionality as Stack, but will only hold up to a certain
    number of items.
    The __init__ method for LimitedStack should take a single, positive integer as an argument. This will
    be the maximum number of items that the LimitedStack can hold. If push is called with an item and that
    item would go beyond the LimitedStack's capacity, the item is not added to the LimitedStack and a
    LimitedStack.LimitedStackOverflowError should be raised.
    If push is called where item equals None, a TypeError should be raised like in the base class.
    If __init__ is called with a non-integer argument, a TypeError should be raised.
    If __init__ is called with an int <= 0, a ValueError should be raised.
    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. New versions of __init__() and push() should be sufficient.
    """

    class LimitedStackOverflowError(Exception):
        def __init__(self):
            super().__init__()

    def __init__(self, size):
        super().__init__()
        self.maximum_size = size;

    def push(self, item):
        current_size = self.size()
        if current_size == self.maximum_size:
            raise self.LimitedStackOverflowError
        else:
            super().push(item)

class RotatingStack(LimitedStack):
    """
    A RotatingStack has the same methods and functionality as LimitedStack, but will not raise an
    exception when an item is added that would go beyond the maximum capacity. Instead, the item
    will be added to the stack and then the oldest item from the RotatingStack will be dropped.
    The __init__ method for RotatingStack should take a single, positive integer as an argument. This will
    be the maximum number of items that the RotatingStack can hold. If push is called with an item and that
    item would go beyond the Rotating's capacity, the item will be added to the stack, but only after
    discarding the oldest item in the stack.
    If push is called where item equals None, a TypeError should be raised like in the base class.
    If __init__ is called with a non-integer argument, a TypeError should be raised.
    If __init__ is called with an int <= 0, a ValueError should be raised.
    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. As long as LimitedStack has properly handled the __init__ method functionality,
    only a new version of push() should be needed.
    """
    def __init__(self, size):
        super().__init__(size)

    def push(self, item):
        current_size = self.size()
        if current_size == self.maximum_size:
            del self._stack_items[-1]
            super().push(item)
        else:
            super().push(item)
