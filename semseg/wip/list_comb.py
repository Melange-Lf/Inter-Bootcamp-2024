def join_files(file1, file2, output_file="training.txt"):
    # Open both input files and the output file
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as final:
        # Read lines from both files simultaneously
        for line1, line2 in zip(f1, f2):
            # Remove any trailing newline characters and join the lines
            combined_line = f"{line1.strip()} {line2.strip()}"
            # Write the combined line to the output file
            final.write(combined_line + "\n")

if __name__ == "__main__":
    # Replace 'path_to_file1' and 'path_to_file2' with your actual file paths
    file1 = 'C:/Users/hp/Documents/code/Py/actual/Ai/inter_boot_2024/semseg/input.txt'
    file2 = 'C:/Users/hp/Documents/code/Py/actual/Ai/inter_boot_2024/semseg/label.txt'
    join_files(file1, file2)
