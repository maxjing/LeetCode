class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        new_words = []
        for w in words:
            new = []
            for c in w:
                new.append(d[c])
            new_words.append(new)
        #2020.05.24 zip, combine as 0 -> 1 , 1 -> 2
        for w1, w2 in zip(new_words, new_words[1:]):
            if w1 > w2:
                return False
        return True


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order.index(word1[j]) > order.index(word2[j]):
                        return False
                if j == min(len(word1), len(word2)) - 1:
                    if len(word1) > len(word2):
                        return False
        return True



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        prevOrder = []
        for i in range(len(words[0])):
            prevOrder.append(order.index(words[0][i]))

        for word in words[1:]:
            currentOrder = []
            for c in word:
                currentOrder.append(order.index(c))
            if not self.compare(prevOrder, currentOrder):
                return False
            prevOrder = currentOrder
        return True

    def compare(self, l1, l2):
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[i]:
                return True
            elif l1[i] > l2[i]:
                return False
            i += 1
            j += 1
        if i < len(l1):
            return False
        else:
            return True


