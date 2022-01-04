numbers = [2, 3, 1, 5, 9]

desc = {
    'length': (num_length := len(numbers)),
    'sum': (num_sum := sum(numbers)),
    'mean': num_sum / num_length,
}


print(desc)
