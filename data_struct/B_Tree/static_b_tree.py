"""
    b tree
    ~~~~~~~
    static b_tree
    add by
        feikong
        0906
"""


class StaticBTree(object):
    def __init__(self, value=None, left_node=None, right_node=None):
        self.left_node = left_node
        self.right_node = right_node
        self.value = value


def create(*args):
    a = input('enter a b_tree value:')
    if a is '#':
        b_tree = None
    else:
        b_tree = StaticBTree(value=a)
        b_tree.left_node = create(b_tree.left_node)
        b_tree.right_node = create(b_tree.right_node)
    return b_tree


def pre_traverse(root):
    """
    根 -> 左 -> 右
    :param root: 根节点
    :return:
    """
    if not root:
        return
    value = root.value
    print(value)
    pre_traverse(root.left_node)
    pre_traverse(root.right_node)


def middle_traverse(root):
    """
    左 -> 根 -> 右
    :param root: 根节点
    :return:
    """
    if not root:
        return
    middle_traverse(root.left_node)
    value = root.value
    print(value)
    middle_traverse(root.right_node)


def post_traverse(root):
    """
    左 -> 右 -> 根
    :param root: 根节点
    :return:
    """
    if not root:
        return
    middle_traverse(root.left_node)
    pre_traverse(root.right_node)
    value = root.value
    print(value)


if __name__ == '__main__':
    b_tree = create(None)

    pre_traverse(b_tree)
    print("============")
    middle_traverse(b_tree)
    print("============")
    post_traverse(b_tree)
