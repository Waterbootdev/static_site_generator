from functools import reduce

def reduce_lists(lists):
    return reduce(lambda x, y: x + y, lists, [])

def apply_pair(func):
    def from_pair(pair):
        return func(pair[0], pair[1])
    return from_pair

def alternated_seq(even, odd, length):
    return map(lambda index: even if index%2 == 0 else odd, range(length))

def is_even(length):
    return length%2 == 0
     
def is_odd(length):
    return length%2 == 1


