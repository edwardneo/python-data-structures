from tree import Tree

class BinaryTree(Tree):
    """A binary tree data structure"""

    def __correct_branches(self, branches):
        for branch in branches:
            assert isinstance(branch, BinaryTree), 'Branch is not a BinaryTree'
        assert len(branches) <= 2, 'More than two branches'
    
    def __repr__(self):
        return f'BinaryTree({repr(self.label)}, {[repr(branch) for branch in self.branches]})'