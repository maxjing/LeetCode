class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        char_frequency = {}
        maxLength, window_start = 0, 0
        for window_end in range(len(tree)):
            right_char = tree[window_end]
            if(right_char not in char_frequency):
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            while len(char_frequency) > 2:

                left_char = tree[window_start]
                char_frequency[left_char] -= 1
                if(char_frequency[left_char] == 0):
                    del char_frequency[left_char]
                window_start += 1
            maxLength = max(maxLength, window_end - window_start + 1)
        return maxLength
