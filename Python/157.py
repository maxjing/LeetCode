"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution():
    def read(self, buf, n):
        res = 0
        buf4 = [""] * 4
        while n:
            r = read4(buf4)
            if r == 0:
                return res
            for i in range(min(r, n)):
                buf[res] = buf4[i]
                res += 1
                n -= 1
        return res
'''
这道题的意思 有一个 read4()的函数 take 一个空的array as buffer solution中的buf4， 一次只能读取4个char
read4()return 一个值 这个值是读取的数量，因为有可能最后一次不够4个 所以loop  min((r,n))
'''