# Overview
A data compression algorithm reduces the amount of memory required to represent a message. The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data.
In this project, I have implemented the logic for both encoding and decoding.

- Time complexity encode: O(nlogn) where 'n' is the input, that is the string's length to encode
- Time complexity decode: O(n) where 'n' is the input, that is the encoded string's length to decode
- Space complexity encode: O(n) where n are the unique chars in the string


## Wikipedia's definition of Huffman Coding
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".
The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted



## How it Works

### Phase I - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.

1. First, determine the frequency of each character in the message.
  
    Example Input: AAAAAAABBBCCCCCCCDDEEEEEE

    Example table:

      | (Unique) Character| Frequency |
      | ----------------- |:---------:|
      |         A         |     7     |
      |         B         |     3     |
      |         C         |     7     |
      |         D         |     2     |
      |         E         |     6     |
      
2. Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, building and sorting a list of nodes in the order lowest to highest frequencies. 
We need a data structure that works as a priority queue, where a node that has lower frequency should have a higher priority to be popped-out. 
A min-heap seems a great choice for this scenerio.

3. Pop-out two nodes with the minimum frequency from the min-heap created in the above step.

4. Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two  nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the min-heap.

5. Repeat steps #3 and #4 until there is a single element left in the priority queue.


### Phase II - Generate the Encoded Data

Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.

  Example continued

| (Unique) Character| Frequency | Huffman Code |
| ----------------- |:---------:| :-----------:|
|         A         |     7     |      000     | 
|         B         |     3     |      001     | 
|         C         |     7     |      01      | 
|         D         |     2     |      10      | 
|         E         |     6     |      11      | 

This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101


### Phase III - Decode data

Once we have the encoded data, and the Huffman tree, we can easily decode the encoded data using the following steps:

1. Declare a blank decoded string
2. Pick a bit from the encoded data, traversing from left to right.
3. Start traversing the Huffman tree from the root.
  - If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
  - If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
4. Repeat steps #2 and #3 until the encoded data is completely traversed.



## Visualization Resource
Check this website to visualize the Huffman encoding for any string message - [Huffman Visualization](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
