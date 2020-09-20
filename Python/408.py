class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        while word and abbr:

            if word[0] == abbr[0]:
                word = word[1:]
                abbr = abbr[1:]
            # both are alpha but not equal
            elif word[0].isalpha() and abbr[0].isalpha():
                return False
            elif abbr[0] == '0':
                return False
            else:
                arr = []
                while abbr and not abbr[0].isalpha():
                    arr.append(abbr[0])
                    abbr = abbr[1:]
                size = int(''.join(arr))
                if size > len(word):
                    return False
                word = word[size:]

        return not abbr and not word