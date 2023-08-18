class Solution:
    def letter_comb_phone_number(self, digits:str):
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
        
            for i in range(index, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i + 1, path + j)
        if not digits:
            return []
        
        dict = {"2" : "abc", "3" : "def", "4" : "ghi",
                "5" : "jkl", "6" : "mno", "7" : "pqrs",
                "8" : "tuv", "9" : "wxyz"}
        result = []
        dfs(0, "")
        
        
        return result

if __name__ == '__main__':
    sol = Solution()
    res = sol.letter_comb_phone_number('2345')

    print(res)