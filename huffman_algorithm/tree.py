from node import Node

class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert (self, data):
        if data == None:
            raise
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.insert(data)


    def preorder(self, root=None):

        if root == None:
            root = self.root

        print(root.data)

        if root.left_son != None:
            self.preorder(root.left_son)

        if root.rigth_son != None:
            self.preorder(root.rigth_son)  