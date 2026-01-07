"""
Advent of Code 2025 - Day 6
https://adventofcode.com/2025/day/6

This problem involves:
- Reading a grid of numbers with operations on the last line
- Applying operations ('+' or '*') to columns of numbers
- Summing the results
"""


def parse_input_part1(filename):
    """Parse input for Part 1 - simple column-based parsing."""
    tmp_all_inputs = []
    with open(filename, 'r') as f:
        for line in f:
            tmp_all_inputs.append([i for i in line.strip().split('  ')])

    all_inputs = []
    for input_arr in tmp_all_inputs:
        row = []
        for input_str in input_arr:
            for i in input_str.split(' '):
                if i != '':
                    row.append(i)
        all_inputs.append(row)

    operations_arr = all_inputs[-1]
    del all_inputs[-1]
    all_num_inputs = [[int(i) for i in arr] for arr in all_inputs]

    return all_num_inputs, operations_arr


def solve_part1(filename):
    """
    Part 1: Apply operations column-wise to the input grid.
    For each column:
    - If operation is '*', multiply all numbers in that column
    - If operation is '+', sum all numbers in that column
    Sum all the operation results.
    """
    all_num_inputs, operations_arr = parse_input_part1(filename)

    final_result = 0
    for operation_idx, operation in enumerate(operations_arr):
        if operation == '*':
            operation_result = 1
            for idx in range(len(all_num_inputs)):
                operation_result *= all_num_inputs[idx][operation_idx]
            final_result += operation_result
        elif operation == '+':
            operation_result = 0
            for idx in range(len(all_num_inputs)):
                operation_result += all_num_inputs[idx][operation_idx]
            final_result += operation_result

    return final_result


def parse_input_part2(filename):
    """Parse input for Part 2 - position-based parsing."""
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip('\n'))

    operations = lines[-1]
    numeric_lines = lines[:-1]

    # Find where operations are located (non-space characters)
    operation_indices = []
    for idx, operation in enumerate(operations):
        if operation != ' ':
            operation_indices.append(idx)

    return numeric_lines, operations, operation_indices


def solve_part2(filename):
    """
    Part 2: Apply operations based on character positions in the input.
    Operations are at specific character positions in the last line.
    Extract numbers from those positions across all numeric lines.
    """
    numeric_lines, operations, operation_indices = parse_input_part2(filename)

    final_value = 0
    for idx, start_idx in enumerate(operation_indices):
        columns = []
        for line in numeric_lines:
            if idx == len(operation_indices) - 1:
                columns.append(line[start_idx:])
            else:
                columns.append(line[start_idx:operation_indices[idx+1]-1])

        # Extract numbers by reading vertically through the columns
        num_values = []
        for char_idx in range(len(columns[0])):
            full_str_num = ''
            for str_num in columns:
                full_str_num += str_num[char_idx]
            num_values.append(int(full_str_num))

        # Apply the operation
        if operations[start_idx] == '+':
            final_value += sum(num_values)
        elif operations[start_idx] == '*':
            product = 1
            for val in num_values:
                product *= val
            final_value += product

    return final_value


def main():
    """Main function to run both parts of the solution."""
    input_file = 'question_6_input.txt'

    # Part 1
    result_part1 = solve_part1(input_file)
    print(f"Part 1 Result: {result_part1}")

    # Part 2
    result_part2 = solve_part2(input_file)
    print(f"Part 2 Result: {result_part2}")


if __name__ == "__main__":
    main()
