class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = getVowels(s)
        vowelSet = {"a","A","e","E","i","I","o","O","u","U"}
        output = []
        for char in s:
            if char in vowelSet:
                output.append(vowels.pop())
                continue
            output.append(char)
        return "".join(output)
        
        
        
def getVowels(string):
    vowelSet = {"a","A","e","E","i","I","o","O","u","U"}
    vowels = []
    for char in string:
        if char in vowelSet:
            vowels.append(char)
    return vowels
            
        
