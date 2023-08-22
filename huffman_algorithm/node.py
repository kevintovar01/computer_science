class Node:

    def __init__(self, probability,data=None) -> None:
        self.data = data
        self.probability = probability
        self.left_son = None
        self.right_son = None
        self.parent = None

    def insert(self, data):
        if data < self.data:
            if self.left_son == None:
                self.left_son = Node(data)
                self.left_son.parent = self
            else:
                self.left_son.insert(data)
        else:
            if self.rigth_son == None:
                self.rigth_son = Node(data)
                self.rigth_son.parent = self
            else:
                self.rigth_son.insert(data)
    

    def source(self, data):
        if data == self.data:
            return self.data
        elif data < self.data:
            if self.left_son == None:
                return
            else:
                return self.left_son.source(data)
        else:
            if self.rigth_son == None:
                return
            else:
                return self.rigth_son.source(data)
            

       
    #preorder jusf for huffman algorithm
    def preorder(self, root):
        
        print(root.data)

        if root.data == None:
            self.preorder(root.left_son)

        if root.data == None:
            self.preorder(root.right_son)

    #delete node
    def delete(self):
        pass