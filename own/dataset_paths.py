import os
import random

# This File creates the training.txt, validation.txt and testing.txt files
# These files contain the paths to input images and their conrresponding segmentation masks

def list_png_files_t(main_folder):
    # FO Test
    with open("data/testing.txt", "w") as txt_file:
        
        for root, dirs, files in os.walk(main_folder):
            for file in files:
                if file.endswith(".jpg"):
                    full_path = os.path.join(root, file)
                    txt_file.write(full_path + "\n")

def list_png_files_tr(main_folder):
    # FO TRAin
    with open("input.txt", "w") as txt_file:
        
        for root, dirs, files in os.walk(main_folder):
            for file in files:
                if file.endswith(".jpg"):
                    # Get the full path of the file
                    full_path = os.path.join(root, file)
                    # Write the full path to the text file
                    txt_file.write(full_path + "\n")

def list_png_files_val(main_folder):
    # FOR LABELS
    with open("label.txt", "w") as txt_file:
        for root, dirs, files in os.walk(main_folder):
            for file in files:
                if file.endswith("gtFine_labelColors.png"):
                    full_path = os.path.join(root, file)
                    txt_file.write(full_path + "\n")

main_folder_t = 'dataset/test'
main_folder_tr = 'dataset/train'
main_folder_val = 'dataset/labels'
list_png_files_t(main_folder_t)
list_png_files_tr(main_folder_tr)
list_png_files_val(main_folder_val)

# -------------------------------------- Combining the paths

def join_files(file1, file2, output_file="comb.txt"):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as final:
        for line1, line2 in zip(f1, f2):
            combined_line = f"{line1.strip()} {line2.strip()}"
            final.write(combined_line + "\n")

file1 = 'input.txt'
file2 = 'label.txt'
join_files(file1, file2)



# ---------------------------------- Train Val Split


def split_data(input_file, validation_file="data/validation.txt", percentage=0.2):
    with open(input_file, "r") as f:
        lines = f.readlines()

    num_validation = int(len(lines) * percentage)

    validation_lines = random.sample(lines, num_validation)

    with open(validation_file, "w") as vf:
        vf.writelines(validation_lines)

    remaining_lines = [line for line in lines if line not in validation_lines]

    with open("data/training.txt", "w") as f:
        f.writelines(remaining_lines)

input_file = 'comb.txt'
split_data(input_file)

