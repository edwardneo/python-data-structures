class Queue():
    """A queue (LIFO)"""

    def __init__(self, lst=[]):
        self.lst = lst
    
    def push(self, item):
        self.lst.append(item)
    
    def pop(self):
        if self.lst:
            temp = self.lst[0]
            self.lst = self.lst[1:]
            return temp
        return None
    
    def __str__(self):
        string = ''
        if self.lst:
            string += f'[{self.lst[0]}]'

        for item in self.lst[1:]:
            string += ' ' + item

        return string
    
    def __repr__(self):
        return f'Queue({self.lst})'