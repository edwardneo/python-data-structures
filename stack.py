class Stack():
    """A stack (FIFO)"""

    def __init__(self, lst=[]):
        self.lst = lst
    
    def append(self, item):
        self.lst.append(item)
    
    def pop(self):
        if self.lst:
            return self.lst.pop()
        return None
    
    def __str__(self):
        string = ''
        for item in self.lst[:-1]:
            string += item + ' '
            
        if self.lst:
            string += f'[{self.lst[-1]}]'

        return string
    
    def __repr__(self):
        return f'Stack({self.lst})'