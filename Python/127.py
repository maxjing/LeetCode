class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque([(beginWord, 1)])
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        q.append((new_word, length + 1))
        return 0

# 需要分层遍历 找到第几步到达终点


class Solution:
    def ladderLength(self, b: str, e: str, wordList: List[str]) -> int:
        if len(wordList) == 0:
            return 0
        wordList = set(wordList)
        q = deque([b])
        seen = set([b])
        res = 1
        while q:
            size = len(q)
            res += 1
            for _ in range(size):
                w = q.popleft()
                for nextWord in self.getNextWord(w, wordList):
                    if nextWord in seen:
                        continue
                    if nextWord == e:
                        return res
                    seen.add(nextWord)
                    q.append(nextWord)
        return 0

    def getNextWord(self, s, wordList):
        nextWords = []
        for i in range(len(s)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == s[i]:
                    continue
                new_s = s[:i]+c+s[i+1:]
                if new_s in wordList:
                    wordList.remove(new_s)
                    nextWords.append(new_s)
        return nextWords
