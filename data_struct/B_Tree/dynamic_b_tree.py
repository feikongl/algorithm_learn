"""
    b tree
    ~~~~~~~
    dynamic b_tree
    add by
        feikong
        0908
"""
from data_struct.B_Tree.static_b_tree import pre_traverse, middle_traverse


class BTree(object):
    def __init__(self, value=None, left_node=None, right_node=None):
        self.left_node = left_node
        self.right_node = right_node
        self.value = value


def create(b_tree, value):
    if b_tree.value is None:
        b_tree.value = value
        return b_tree
    root = b_tree
    while root.value:
        # 插入值大于根节点
        if value > root.value:
            # 右侧无节点
            if root.right_node is None:
                root.right_node = BTree(value)
                return root
            root = root.right_node
        else:
            if root.left_node is None:
                root.left_node = BTree(value)
                return
            root = root.left_node


if __name__ == '__main__':
    a = [2, 3, 1, 4, 5]
    b_tree = BTree()
    for i in a:
        create(b_tree, i)
    pre_traverse(b_tree)
    print("==============")
    middle_traverse(b_tree)
