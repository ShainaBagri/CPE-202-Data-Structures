class HuffmanNode:
    def __init__(self, char_ascii, freq):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq              # the frequency count associated with the node
        self.left = None              # Huffman tree (node) to the left
        self.right = None             # Huffman tree (node) to the right

    def __lt__(self, other):
        return comes_before(self, other) # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):
    """Returns True if node a comes before node b, False otherwise"""
    if a.freq == b.freq:
        return a.char_ascii < b.char_ascii
    return a.freq < b.freq

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    if comes_before(a, b):
        left = a
        right = b
    else:
        left = b
        right = a
    newnode = HuffmanNode(min(a.char_ascii, b.char_ascii), a.freq+b.freq)
    newnode.left = left
    newnode.right = right
    return newnode

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    file = open(filename)
    txt = file.read()
    freqlis = [0]*256
    for item in txt:
        freqlis[ord(item)] += 1
    file.close()
    return freqlis

def selection_sort(lis):
    lis_size = len(lis)
    i = 0
    while i<lis_size-1:
        maxInd = 0
        j = 1
        while j<lis_size-i:
            if comes_before(lis[maxInd], lis[j]):
                maxInd = j
            j += 1
            tmp = lis[lis_size-1-i]
            lis[lis_size - 1 - i] = lis[maxInd]
            lis[maxInd] = tmp
        i += 1

def create_huff_tree(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    #creates list of huffman nodes
    nodes = []
    for i in range(len(freq_list)):
        if freq_list[i] != 0:
            nodes.append(HuffmanNode(i, freq_list[i]))
    if len(nodes)==0:
       return None
    #sorts list of huffman nodes
    selection_sort(nodes)
    #removes 2 lowest nodes and combines
    while len(nodes)>1:
        newnode = combine(nodes[0], nodes[1])
        nodes = nodes[2:]
        sorted = False
        j = 0
        while j<len(nodes) and not sorted:
            if comes_before(newnode, nodes[j]):
                nodes = nodes[:j] + [newnode] + nodes[j:]
                sorted = True
            j += 1
        if j==len(nodes):
            nodes = nodes + [newnode]
    return nodes[0]

def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    if node.left is None and node.right is None:
        return None
    return create_code_h(node, "", [""]*256)

#helper function for create_code
def create_code_h(node, str, lis):
    if node is None:
        return lis
    if node.left is None and node.right is None:
        lis[node.char_ascii] = str
    else:
        create_code_h(node.left, str+"0", lis)
        create_code_h(node.right, str + "1", lis)
    return lis

def create_header(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    ans = ""
    first = True
    for i in range(len(freq_list)):
        if freq_list[i]!=0:
            if first:
                ans = str(i) + " " + str(freq_list[i])
                first = False
            else:
                ans = ans + " " + str(i) + " " + str(freq_list[i])
    return ans

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take note of special cases - empty file and file with only one unique character"""
    try:
        f = open(in_file, "r")
        if f.mode == 'r':
            text = f.read()
        f.close()
    except:
        raise FileNotFoundError
    f2 = open(out_file, "w")
    if text != '':
        huffcode = create_code(create_huff_tree(cnt_freq(in_file)))
        huffheader = create_header(cnt_freq(in_file))
        lis = list(text)
        encoded = ''
        if huffcode is None:
            f2.write(huffheader)
        else:
            for i in lis:
                encoded += huffcode[ord(i)]
            f2.write(huffheader + "\n" + encoded)
    f2.close()

"""Part B: Decoding"""

def parse_header(header_string):
    str_list = header_string.split(" ")
    freq_list = [0]*256
    i = 0
    while i<len(str_list):
        freq_list[int(str_list[i])] = int(str_list[i+1])
        i += 2
    return freq_list

def huffman_decode(encoded_file, decode_file):
    try:
        f = open(encoded_file, "r")
        if f.mode == 'r':
            txt = f.readlines()
        f.close()
    except:
        raise FileNotFoundError
    f2 = open(decode_file, "w")
    if txt != []:
        header = txt[0]
        try:
            code = txt[1]
        except:
            code = ""
        decoded = ""
        rootnode = create_huff_tree(parse_header(header))
        node = rootnode
        for i in code:
            if int(i)==0:
                node = node.left
            elif int(i)==1:
                node = node.right
            if node.left==None and node.right==None:
                decoded += chr(node.char_ascii)
                node = rootnode
        if code=="":
            decoded = chr(node.char_ascii)*node.freq
        f2.write(decoded)
    f2.close()
