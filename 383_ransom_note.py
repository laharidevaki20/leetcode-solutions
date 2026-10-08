class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count={}
        for i in magazine:
            if i not in mag_count:
                mag_count[i] = 1
            else:
                mag_count[i] += 1
        for i in ransomNote:
            if i not in mag_count:
                return False
            if mag_count[i] == 0:
                return False
            mag_count[i] -= 1
        return True