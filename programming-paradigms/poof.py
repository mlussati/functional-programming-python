# Procedural programming
def add_values(any_list):
    sum_v: int = 0
    for x in any_list:
        sum_v += x

    return sum_v


m_list = [1, 2, 3, 4]
print(add_values(m_list))


# Object-Oriented programming
class ListOperations(object):
    def __init__(self, any_list):
        self.sum = None
        self.any_list = any_list

    def add_values(self):
        self.sum = sum(self.any_list)


sum_values = ListOperations(m_list)
sum_values.add_values()

print(sum_values.sum)

# Functional Programming
import functools
m_list = [1, 2, 3, 4]

sum_v = functools.reduce(lambda x, y: x + y, m_list)
print(sum_v)
