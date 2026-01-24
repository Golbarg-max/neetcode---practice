class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWord = ""
        for s in strs:
            encodedWord += str(len(s)) + "#" + s
        return encodedWord
    def decode(self, s: str) -> List[str]:
        i = 0
        ls = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ls.append(s[i:j])
            i = j
        return ls
