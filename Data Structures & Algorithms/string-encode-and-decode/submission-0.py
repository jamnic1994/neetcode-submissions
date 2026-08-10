class Solution:

    def encode(self, strs: List[str]) -> str:

        newString = "" 

        for string in strs:
            charCount = str(len(string))
            newString += charCount + "#" + string
            
        return newString

    def decode(self, s: str) -> List[str]:

        word = ""
        wordList = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            word = s[start:start + length]
            
            wordList.append(word)

            i = start + length

        return wordList                





