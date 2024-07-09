
class Solution:
    def reverseWords(self,S):
        words=S.split('.')
        reversed_words=words[::-1]
        reversed_string='.'.join(reversed_words)
        return reversed_string
s=str(input())
obj=reverseWords(s)
print(obj)

