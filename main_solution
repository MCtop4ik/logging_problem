import numpy as np

def process_logs(input_file, output_file):
    first_lines = []
    last_lines = np.empty(100, dtype=object)
    last_index = 0
    total_lines = 0

    with open(input_file, 'r') as file:
        for line in file:
            total_lines += 1
            if total_lines <= 100:
                first_lines.append(line)
            else:
                last_lines[last_index] = line
                last_index = (last_index + 1) % 100

    with open(output_file, 'w') as out_file:
        out_file.writelines(first_lines)
        out_file.write('\n...\n')

        for i in range(last_index, last_index + 100):
            out_file.write(last_lines[i % 100])
