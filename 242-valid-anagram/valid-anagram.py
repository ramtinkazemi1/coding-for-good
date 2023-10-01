class Solution:
    def isAnagram(self, s, t):
        
        dic1={}
        dic2={}

        for char in s:
          if char not in dic1:
            dic1[char]=1
          else:
            dic1[char]+=1
          
        for char in t:
          if char not in dic2:
            dic2[char]=1
          else:
            dic2[char]+=1

        for key, value in dic1.items():
          if key not in dic2:
            return False
          else:
              if dic2[key] != value:
                return False

        for key, value in dic2.items():
          if key not in dic1:
            return False
          else:
              if dic1[key] != value:
                return False

        return True
