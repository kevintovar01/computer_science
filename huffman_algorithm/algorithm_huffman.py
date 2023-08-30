from collections import Counter
from node import Node


class Huffman:
    def __init__(self) -> None:
        self.word = ""
        self.probabilitys = {}
        self.nodos = []
        self.bits = {} 
        self.bit = ""
        self.root = None

    def get_probalities(self, content):
        self.word = content  #example hello world
        total = len(content)
        counter = Counter(content) #count each letter --> Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

        for char, count in counter.items():
            self.probabilitys[char] = float(count)/total # example 'l':3, 3/11  


    def aignar_nodo(self):
        sorted_items = sorted(self.probabilitys.items(), key=lambda x: x[1])#sort ascending

        print(sorted_items)

        for data, valor in sorted_items: #for each value we are create a node
            self.nodos.append(Node(valor, data))

    def suma_nodos(self):
        
        while len(self.nodos) > 1:
            
            
            nodo1 = self.nodos.pop(0)  #delete node of the lists for create other new
            nodo2 = self.nodos.pop(0)


            new_node = Node(nodo1.probability+nodo2.probability)  #sum the probabilities

            nodo1.parent = new_node
            nodo2.parent = new_node
            new_node.left_son = nodo1
            new_node.right_son = nodo2

            self.nodos.append(new_node)

        
        tree = self.nodos
        return tree[0]

    #count the bits for each letter in the tree
    def count_bits(self, root=None, bit_string=""): 
        if root is None:
            root = self.root

        if root.left_son is None and root.right_son is None:
            self.bits[root.data] = bit_string
            return

        if root.left_son is not None:
            self.count_bits(root.left_son, bit_string + '0')

        if root.right_son is not None:
            self.count_bits(root.right_son, bit_string + '1')


    #encode our word
    def decode_word(self, encode_string, root=None):
        word = ""
        current_node = root

        for bit in encode_string:
            if bit == '0':
                current_node = current_node.left_son
            else:
                current_node = current_node.right_son
            
            if current_node.data is not None:
                word += current_node.data
                current_node = root 

        return word
    
    #just join all bits for each letter
    def encode_word(self):
        encode_string = ''.join(self.bits[char] for char in self.word)
        return encode_string
