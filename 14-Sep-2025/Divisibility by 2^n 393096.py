# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys

def count_trailing_zeros_in_binary(number):
    power_of_two_count = 0
    while number % 2 == 0:
        power_of_two_count += 1
        number //= 2
    return power_of_two_count


def solve_single_test_case(array_length, array_elements):
    current_power_of_two = sum(
        count_trailing_zeros_in_binary(element) for element in array_elements
    )

    if current_power_of_two >= array_length:
        return 0

    additional_power_needed = array_length - current_power_of_two

    index_contributions = [
        count_trailing_zeros_in_binary(index) for index in range(1, array_length + 1)
    ]

    index_contributions.sort(reverse=True)

    operations_performed = 0
    accumulated_power = 0

    for contribution in index_contributions:
        if contribution == 0:
            continue

        accumulated_power += contribution
        operations_performed += 1

        if accumulated_power >= additional_power_needed:
            return operations_performed

    return -1


def main():
    input_data = list(map(int, sys.stdin.buffer.read().split()))
    data_iterator = iter(input_data)

    number_of_test_cases = next(data_iterator)
    output_results = []

    for _ in range(number_of_test_cases):
        array_size = next(data_iterator)
        array_values = [next(data_iterator) for _ in range(array_size)]

        result = solve_single_test_case(array_size, array_values)
        output_results.append(str(result))

    sys.stdout.write("\n".join(output_results))


if __name__ == "__main__":
    main()
