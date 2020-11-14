class Solution():
    def strStr(_, haystack: str, needle: str) -> str:
        '''Searches for given needle in the haystack and if it finds returns the
           found index, else will return -1
           returns 0 if needle is an empty string
        '''
        if len(needle) == 0:
            return 0

        try:
            ind = haystack.index(needle)
            return ind
        except ValueError:
            return -1

    def strStr2(_, haystack: str, needle: str) -> str:
        if len(needle) == 0:
            return 0

        for ind in range(len(haystack)):
            if haystack[ind] == needle[0]:
                if haystack[ind:ind + len(needle)] == needle:
                    return ind

        return -1


def check_solution():
    solution = Solution()
    assert solution.strStr('hello', 'll') == 2
    assert solution.strStr('aaaaa', 'bba') == -1
    assert solution.strStr('ahoy!', '') == 0
    print("Correct!")


check_solution()
