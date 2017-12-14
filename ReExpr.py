import re

import math


class QuadraticFunction:

    def __init__(self, string_1):
        self._list=re.findall(r'\d',string_1)
        print(self._list)
        del self._list[1]
        print(self._list)
        self._list = list(map(int, self._list))

    def findsolution(self):
        delta= self._list[1] ** 2 - 4 * self._list[0] * self._list[2]
        print(delta)
        if delta>0:
            print('Delta: ', delta)
            x1 = (-self._list[1] - math.sqrt(delta)) / (2 * self._list[0])
            x2 = (-self._list[1] + math.sqrt(delta)) / (2 * self._list[0])
            print('x1: ', x1, ' x2: ', x2)
        elif delta == 0:
            print('Delta: ',delta)
            x=(-self._list[1] / (2 * self._list[0]))
            print('x = ',x)
        else:
            print('Delta: ', delta)
            print("There is no solution")




string_1 = '1x^2+5x-4'
string_2 = 'There are some words'

#print(re.split(r'(\s*)',string_2))

print(type(re.findall(r'\d', string_1)))

eq1=QuadraticFunction(string_1)
eq1.findsolution()



