import sys
from heapq import heappush, heappop

class InvalidInput(Exception):
    def __init__(self):
        self.message = "Can't encode/decode input: it is None or Empty"

class Node(object):
    def __init__(self, char=None, frequency=None, child_left=None, child_right=None):
        self.char = char
        self.frequency = frequency
        self.left = child_left
        self.right = child_right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def get_frequency(self):
        return self.frequency

    def get_char(self):
        return self.char

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_char(self, char):
        self.char = char

    def set_left_child(self, child):
        self.left = child

    def set_right_child(self, child):
        self.right = child

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


#================= UTILITY METHODS =================

def build_huffman_tree_recursively(heap, node_left, node_right):
    if node_left is None or node_right is None:
        return
    else:
        frequency_sum = node_left.get_frequency() + node_right.get_frequency()
        new_node = Node(None, frequency_sum, node_left, node_right)
        heappush(heap, new_node)
        if len(heap) >= 2: build_huffman_tree_recursively(heap, heappop(heap), heappop(heap))


def generate_huffman_map(node, huffmanCode, huffman_map):
    if node is None:
        return
    else:
        if node.has_left_child(): 
            new_code = huffmanCode[0:len(huffmanCode)] + str(0)
            generate_huffman_map(node.get_left_child(), new_code, huffman_map)
        if node.has_right_child(): 
            new_code = huffmanCode[0:len(huffmanCode)] + str(1)
            generate_huffman_map(node.get_right_child(), new_code, huffman_map)
        if node.get_char() != None:
            huffman_map[node.get_char()] = huffmanCode
            return


#================= MAIN METHODS ==================================================

def huffman_encoding(data):

    if data is None or data.strip() is "": 
        raise InvalidInput

    heap = []
    map_char_frequency = {}

    # Build map where key is char and value is its frequency
    for char in data: # O(n)
        value = map_char_frequency.get(char) # O(1)
        map_char_frequency[char] = (value + 1) if value != None else 1 # O(1)

    # create a Node for each key-value and insert it into the min-heap
    for char, frequency in map_char_frequency.items(): # O(n)
        heappush(heap, Node(char, frequency)) # O(?)

    # build Huffman Tree
    build_huffman_tree_recursively(heap, heappop(heap), heappop(heap))

    # Traverse tree and build map with huffman_code for each char
    huffman_map = {}
    generate_huffman_map(heap[0], "", huffman_map)

    # Generate encoded data
    encodedData = ""
    for char in data:
        encodedData += huffman_map.get(char)

    return encodedData, heap[0]





def huffman_decoding(data, tree):
    if data is None or data.strip() is "":
        raise InvalidInput
    
    decoded = ""
    node = tree
    for bit in data:
        if bit == '0':
            if node.has_left_child():
                node = node.get_left_child()
                if node.get_char() != None:
                    decoded += node.get_char()
                    node = tree
        elif bit == '1':
            if node.has_right_child():
                node = node.get_right_child()
                if node.get_char() != None:
                    decoded += node.get_char()
                    node = tree

    return decoded



#=== DEFINE AND RUN TESTS ==============================================================

def test(input):
    print("==== NEW TEST ====")
    print ("The size of the data is: {}\n".format(sys.getsizeof(input)))
    print ("The content of the data is: {}\n".format(input))
    
    try:
        encoded_data, tree = huffman_encoding(input)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded = huffman_decoding(encoded_data, tree)

        if decoded == input: print("SUCCESS! Input is: {} - decoded is: {}".format(input, decoded))
        else: print("FAIL!")

    except InvalidInput as ex:
        print(ex.message)



input_1 = "AAAAAAABBBCCCCCCCDDEEEEEE"
input_2 = "One ring to rule them ALL!"
input_3 = ""
input_4 = None

test(input_1)
test(input_2)
test(input_3)
test(input_4)