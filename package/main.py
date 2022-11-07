from typing import List
class Solution:

    @staticmethod
    def equal_characters(a:str, b:str) -> bool: return a.lower() == b.lower()
    @staticmethod
    def upperAndLower(a:str, b:str) -> bool: return (a.islower() and b.isupper()) or (a.isupper() and b.islower())
    @staticmethod
    def upperNextToLower(s: str) -> List:
        for i in range(1,len(s)):
            if Solution.equal_characters(s[i-1],s[i]) and Solution.upperAndLower(s[i-1],s[i]):
                return [i-1,i]

if __name__ == '__main__':
    print(Solution.upperNextToLower("UnitTest"))
