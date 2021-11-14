class Tree():
    """A tree data structure"""

    empty = []
    def __init__(self, label, branches=empty):
        self.__correct_branches(branches)

        self.label = label
        self.branches = branches
    
    def is_leaf(self):
        return self.branches is Tree.empty
    
    def __correct_branches(self, branches):
        for branch in branches:
            assert isinstance(branch, Tree), 'Branch is not a Tree'
    
    def __str__(self):
        def tree_str(tree, indent=0):
            string_lst = ['  ' * indent + tree.label]
            for branch in tree.branches:
                string_lst.append(tree_str(branch, indent+1))
            return '\n'.join(string_lst)
        return tree_str(self)
    
    def __repr__(self):
        return f'Tree({repr(self.label)}, {[repr(branch) for branch in self.branches]})'
            