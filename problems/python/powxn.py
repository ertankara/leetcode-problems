from math import pow


class Solution():
    def myPow(_, x: float, n: int) -> float:
        '''Raises x to the nth power'''
        return pow(x, n)


def check_solution():
    solution = Solution()
    delta = 0.0001
    assert abs(solution.myPow(2.00000, 10) - 1024.00000 < delta)
    assert abs(solution.myPow(2.10000, 3) - 9.26100 < delta)
    assert abs(solution.myPow(2.00000, -2) - 2 < delta)
    assert abs(solution.myPow(-2.00000, 2) - 4 < delta)
    print("Correct!")


check_solution()
