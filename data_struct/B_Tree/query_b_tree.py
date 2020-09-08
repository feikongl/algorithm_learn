"""
    b tree
    ~~~~~~~
    query b_tree：
        high
        max root

    add by
        feikong
        0908
"""
from data_struct.B_Tree.dynamic_b_tree import create


class BTree(object):
    def __init__(self, value=None, left_node=None, right_node=None):
        self.left_node = left_node
        self.right_node = right_node
        self.value = value


def get_tree_height(b_tree):
    if b_tree is None:
        return 0
    l_height = get_tree_height(b_tree.left_node)
    r_height = get_tree_height(b_tree.right_node)

    height = max(l_height, r_height) + 1
    return height


def get_max_value(b_tree):
    if b_tree is None:
        return -1
    root = b_tree.value
    right = get_max_value(b_tree.right_node)
    result = max(root, right)
    return result


if __name__ == '__main__':
    a = [2, 3, 1, 4, 5]
    b_tree = BTree()
    for i in a:
        create(b_tree, i)

    print("height:", get_tree_height(b_tree))
    print("max:", get_max_value(b_tree))
