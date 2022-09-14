# Trie


class TrieNode(object):
    def __init__(self, data) -> None:
        self.data = data
        self.children = [None] * 26
        self.lastNode = False


class Trie(object):
    def __init__(self) -> None:
        self.root = TrieNode("")
        self.lastNode = False

    def _charToIndex(self, char: str) -> int:
        return ord(char) - ord("a")

    def insert(self, word: str) -> None:
        root = self.root
        for i in word:
            index = self._charToIndex(i)
            if not root.children[index]:
                root.children[index] = TrieNode(i)
            root = root.children[index]
        root.lastNode = True

    def search(self, word: str) -> bool:
        root = self.root
        for i in word:
            index = self._charToIndex(i)
            if not root.children[index]:
                return False
            root = root.children[index]
        return root.lastNode

    def startsWith(self, prefix: str) -> bool:
        pass


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.startsWith("app"))  # returns true
    trie.insert("app")
    print(trie.search("app"))  # returns true
