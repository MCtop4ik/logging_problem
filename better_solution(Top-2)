def process_logs(input_file, output_file):
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
