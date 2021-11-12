from deque import Deque

class Stack(Deque):
    """A stack (FIFO)"""

    def prepend(*args):
        raise AttributeError("'Stack' object has no attribute 'prepend'")
    
    def pop_left(*args):
        raise AttributeError("'Stack' object has no attribute 'pop_left'")
    
    def __str__(self):
        string = ''
        for item in self.lst[:-1]:
            string += item + ' '
            
        if self.lst:
            string += f'[{self.lst[-1]}]'

        return string
    
    def __repr__(self):
        return f'Stack({self.lst})'