class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "🔥".join(strs)
        res = ""
        if not strs:
            res = "😁"
        
        for ch in encoded_string:
            if ch.isascii():
                res += chr(ord(ch)+1)
            else:
                res += ch
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = ""
        for ch in s:
            if ch.isascii():
                res += chr(ord(ch)-1)
            else:
                res += ch
        return [] if s == "😁" else res.split("🔥") if res else [""]
