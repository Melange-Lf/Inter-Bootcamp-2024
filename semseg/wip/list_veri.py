import random

def split_data(input_file, validation_file="validation.txt", percentage=0.2):
    # Read all lines from the input file
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Calculate the number of lines to select for validation
    num_validation = int(len(lines) * percentage)

    # Randomly choose lines for validation
    validation_lines = random.sample(lines, num_validation)

    # Write the selected lines to the validation file
    with open(validation_file, "w") as vf:
        vf.writelines(validation_lines)

    # Remove the selected lines from the original file
    remaining_lines = [line for line in lines if line not in validation_lines]

    # Rewrite the original file without the validation lines
    with open("training.txt", "w") as f:
        f.writelines(remaining_lines)

if __name__ == "__main__":
    # Replace 'path_to_input_file' with your actual file path
    input_file = 'C:/Users/hp/Documents/code/Py/actual/Ai/inter_boot_2024/semseg/comb.txt'
    split_data(input_file)
