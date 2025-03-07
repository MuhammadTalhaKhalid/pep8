def find_max_min_difference(elements):
    print("Your list:", elements)
    pair_diff = {}

    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            diff = abs(elements[i] - elements[j])
            pair_diff[(elements[i], elements[j])] = diff

    maximum = max(pair_diff)
    minimum = min(pair_diff)

    print(f'Maximum distance between elements is {maximum} and their difference is {pair_diff[maximum]}')
    print(f'Minimum distance between elements is {minimum} and their difference is {pair_diff[minimum]}')


# Get user input and call the function

find_max_min_difference([1,2,5,76,24,67,23,67,23,75,8,23,2,68])
