class Solution15:
    def find_all_sub_str_without_bultin_fun(self,s):
        substr =[]
        for i in range(0,len(s)):
            curr = ""
            for j in range(i, len(s)):
                curr = curr + s[j]
                substr.append(curr)
        return substr

