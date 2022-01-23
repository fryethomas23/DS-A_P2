from ipywidgets import interact, interact_manual
from IPython.display import display
from ipywidgets import widgets


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.word_end = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        else:
            return

    def get_child(self, char):
        return self.children.get(char)

    def get_children(self):
        return self.children

    def set_word_end(self):
        self.word_end = True
        return

    def get_word_end(self):
        return self.word_end

    def suffixes(self, arr=[]):
        arr = self.suffixes_recurse(self)
        return arr

    def suffixes_recurse(self, current, arr=[], suffix=""):
        if current.get_word_end() and suffix:
            arr.append(suffix)
        if current.children:
            for char, node in current.children.items():
                arr = self.suffixes_recurse(node, arr, suffix + char)
        return arr

# The Trie itself containing the root node and insert/find functions


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current = self.root
        for char in word:
            current.insert(char)
            current = current.get_child(char)

        current.set_word_end()

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            current = current.get_child(char)
            if not current:
                return None

        return current

    def __str__(self):
        return self.str_recurse(self.root, 0, "")

    def str_recurse(self, node, tab, string):
        for char in node.get_children().keys():
            string += "--"*tab + char + " : {\n"
            string = self.str_recurse(node.get_child(char), tab+1, string)

        if node.get_word_end():
            string += "--"*tab + "word_end: " + str(node.get_word_end()) + "\n"
        string += "--"*tab + "}\n"

        return string


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact_manual(f, prefix='')
# a = "nt", "nthology", "ntagonist", "ntonym"
# b = b not found
# anth = ologoy
