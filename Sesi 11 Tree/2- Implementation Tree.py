# membangun Tree
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


# tree disini di definisiin pake tuple
# (1, 3, None) merupakan data left, root, right
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


# fungsi untuk me-metakan tree yang ada dalam variabel tree_tuple
def parse_tuuple(data):
    # isintance mengecek apakah data merupakan suatu kelas dari class built-in tuple
    # len(data) untuk mengecek level dari 0-1-2-3
    if isinstance(data, tuple) and len(data) == 3:
        # ini sebagai root
        node = TreeNode(data[1])
        node.left = parse_tuuple(data[0])
        node.right = parse_tuuple(data[2])
    # kondisi ketika datanya kosong
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def display_key(node, space="\t", level=0):
    # ngecek apa datanya kosong
    if node is None:
        print(space * level + "*")
        return

    # kalo pointer adalah leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    display_key(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_key(node.left, space, level + 1)


if __name__ == "__main__":
    tree2 = parse_tuuple(tree_tuple)

    display_key(tree2)
