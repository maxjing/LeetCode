class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.l = dict

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for v in self.l:
            if self.validate(word, v):
                return True
        return False

    def validate(self, s1, s2):
        if len(s1) != len(s2):
            return False
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff == 2:
                    return False
        return diff == 1

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

'''
one optimize is to use hashmap to store length:word, easier for look up
'''