class Deque():
    """A deque"""

    def __init__(self, lst=[]):
        self.lst = lst
    
    def prepend(self, item):
        self.lst = [item] + self.lst
    
    def append(self, item):
        self.lst.append(item)
    
    def pop_left(self):
        if self.lst:
            temp = self.lst[0]
            self.lst = self.lst[1:]
            return temp
        return None
    
    def pop(self):
        if self.lst:
            return self.lst.pop()
        return None
    
    def __str__(self):
        string = ''
        if self.lst:
            string += f'[{self.lst[0]}]'

        for item in self.lst[1:-1]:
            string += ' ' + item
        
        if self.lst:
            string += f' [{self.lst[-1]}]'

        return string
    
    def __repr__(self):
        return f'Deque({self.lst})'