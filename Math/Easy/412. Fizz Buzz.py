from typing import *


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for i in range(n):
            idx = i + 1
            if (idx / 3).is_integer() and (idx / 5).is_integer():
                results.append('FizzBuzz')
            elif (idx / 3).is_integer():
                results.append('Fizz')
            elif (idx / 5).is_integer():
                results.append('Buzz')
            else:
                results.append(format(idx))

        return results