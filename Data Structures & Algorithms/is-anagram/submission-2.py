class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        
        if len(s)!=len(t):
            return False 
        else:
            for i in range(len(s)):
                list1.append(s[i])
                list2.append(t[i])
            
            list1.sort()
            list2.sort()
        
            return list1 == list2
