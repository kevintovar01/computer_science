from algorithm_huffman import Huffman

if __name__ == '__main__':


    tree_huffman = Huffman()

    tree_huffman.get_probalities(input("insert a word: "))
    tree_huffman.aignar_nodo()
    tree = tree_huffman.suma_nodos()

    print("preorder: ")
    tree.preorder(tree)
    tree_huffman.rama = tree

    bits = tree_huffman.count_bits(tree)

    encode = tree_huffman.encode_word()

    word = tree_huffman.decode_word(encode, tree)
    print("bits of each letter: ", tree_huffman.bits)
    print("encode word in binary: ", encode)
    print("result of decode word: ", word)