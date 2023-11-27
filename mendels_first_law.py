

def mendels_first_law(k, m, n):
    population_size = k + m + n
    return (
        k / population_size + m / population_size * 
        (k / (population_size - 1) + (m - 1) / (population_size - 1) * 3 / 4 + 
        n / (k + m + n - 1) / 2) + n / (k + m + n) * 
        (k / (population_size - 1) + m / (population_size - 1) / 2))


k = 2 # homozygous dominant
m = 2 # heterozygous 
n = 2 # homozygous recessive
print(mendels_first_law(k, m, n))
