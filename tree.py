import json


class BinaryTree:

    def __init__(self, *, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = 0
        self._set_depth(self.depth)

    def _set_depth(self, depth):
        if self.left is not None:
            self.left._set_depth(depth+1)
        if self.right is not None:
            self.right._set_depth(depth+1)
        self.depth = depth

    def create_repr(self):
        output = {}
        next_item = {'left': None, 'right': None}
        if self.left is not None:
            next_item['left'] = self.left.create_repr()
        if self.right is not None:
            next_item['right'] = self.right.create_repr()
        output.update({self.data: next_item})
        return output

    def reverse(self):
        self.right, self.left = self.left, self.right
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()

    def print_tree(self):
        print(json.dumps(self.create_repr(), indent=4, sort_keys=True))


print('Creating binary tree')
tree = BinaryTree(
    data='level 1 data',
    left=BinaryTree(
        data='level 2 data left', right=BinaryTree(data='level 3 data')
    ),
    right=BinaryTree(data='level 2 data right'),
)
tree.print_tree()
print('Reversing...')
tree.reverse()
tree.print_tree()
