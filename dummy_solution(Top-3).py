def process_logs(input_file, output_file):
    lines = []

    with open(input_file, 'r') as file:
        for line in file:
            lines.append(line)

    with open(output_file, 'w') as out_file:
        out_file.writelines(lines[100:])
        out_file.write('\n...\n')
        out_file.writelines(lines[:-100])
