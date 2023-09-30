

def count_point_mutations(s, t):
    return len([1 for c, d in zip(s, t) if c != d])


s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
print(count_point_mutations(s, t))
