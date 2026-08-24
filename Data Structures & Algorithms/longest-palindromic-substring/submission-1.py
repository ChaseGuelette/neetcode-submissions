class Solution:
    def longestPalindrome(self, s: str) -> str:

        # l, r = 0, 0
        # longest = ""
        # i = 1

        def expand(l, r, longest):
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if len(s[l:r+1]) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            return longest
            
        # longest = expand(1, 1, longest)
        # print(longest)



        # l, r = 0, 0
        longest = ""
        i = 0
        while i < len(s):

            #single center
            l, r = i, i
            longest = expand(l, r, longest)
            #double center:
            l, r = i, i + 1
            longest = expand(l, r, longest)

            i += 1
                
        return longest


        