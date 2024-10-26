import numpy as np
import time
// !pip install memory-profiler

from memory_profiler import memory_usage


def process_logs_algo(input_file, output_file):
    start_time = time.time()
    first_lines = []
    last_lines = []
    total_lines = 0

    with open(input_file, 'r') as file:
        for line in file:
            total_lines += 1
            if total_lines <= 100:
                first_lines.append(line)
            else:
                if len(last_lines) < 100:
                    last_lines.append(line)
                else:
                    last_lines.pop(0)
                    last_lines.append(line)

    with open(output_file, 'w') as out_file:
        out_file.writelines(first_lines)
        out_file.write('\n...\n')
        out_file.writelines(last_lines)
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")

  
def process_logs_algo_arr(input_file, output_file):
    start_time = time.time()
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
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")


def process_logs3(input_file, output_file):
    start_time = time.time()
    lines = []

    with open(input_file, 'r') as file:
        for line in file:
            lines.append(line)

    with open(output_file, 'w') as out_file:
        out_file.writelines(lines[100:])
        out_file.write('\n...\n')
        out_file.writelines(lines[:-100])
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")


mem_usage = memory_usage((process_logs1, ('customer_transactions_log.csv', 'output.txt')))
print(f"Memory usage: {max(mem_usage) - min(mem_usage)} MB")

mem_usage = memory_usage((process_logs2, ('customer_transactions_log.csv', 'output.txt')))
print(f"Memory usage: {max(mem_usage) - min(mem_usage)} MB")

mem_usage = memory_usage((process_logs3, ('customer_transactions_log.csv', 'output.txt')))
print(f"Memory usage: {max(mem_usage) - min(mem_usage)} MB")
