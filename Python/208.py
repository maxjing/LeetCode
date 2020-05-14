import collections


class Trie:

    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.is_word_end = False

    def insert(self, word: str) -> None:
        if not word:
            self.is_word_end = True
        else:
            self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.is_word_end
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)