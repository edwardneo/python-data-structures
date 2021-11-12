from deque import Deque

class Queue():
    """A queue (LIFO)"""

    def prepend(*args):
        raise AttributeError("'Queue' object has no attribute 'prepend'")

    def pop(*args):
        raise AttributeError("'Queue' object has no attribute 'pop'")
    
    def __str__(self):
        string = ''
        if self.lst:
            string += f'[{self.lst[0]}]'

        for item in self.lst[1:]:
            string += ' ' + item

        return string
    
    def __repr__(self):
        return f'Queue({self.lst})'