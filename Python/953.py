class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        list = []
        for w in words:
            sublist = []
            for c in w:
                sublist.append(d[c])
            list.append(sublist)
        for o1, o2 in zip(list, list[1:]):
            #2020.05.28 no need to check length, none is less than any c
            if o1 > o2:
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


