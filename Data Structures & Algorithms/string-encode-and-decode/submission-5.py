class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for word in strs:
            length_word = len(word)
            st += str(length_word)+"#"+word
        return st
    def decode(self, s: str) -> List[str]:
        li = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i+=1
            length = int(s[j:i])
            li.append(s[i+1: i+1+length])
            j = i + length + 1
            i = j
        return li
