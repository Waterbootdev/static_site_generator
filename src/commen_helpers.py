from functools import reduce

def reduce_lists(lists):
    return reduce(lambda x, y: x + y, lists, [])

def apply_pair(func):
    def from_pair(pair):
        return func(pair[0], pair[1])
    return from_pair

def apply_tripple(func):
    def from_triple(tripple):
        return func(tripple[0], tripple[1], tripple[2])
    return from_triple

def is_even(length):
    return length%2 == 0
     
def is_odd(length):
    return length%2 == 1

def alternated_seq(even, odd, length):
    return map(lambda index: even if is_even(index) else odd, range(length))



