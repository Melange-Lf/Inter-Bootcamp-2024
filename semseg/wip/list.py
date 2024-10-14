import os

# def list_png_files(main_folder):
#     # FO TRAIR
#     # Open the text file in write mode
#     with open("input.txt", "w") as txt_file:
#         # Walk through the main folder and its subdirectories
        
#         for root, dirs, files in os.walk(main_folder):
#             for file in files:
#                 if file.endswith(".jpg"):
#                     # Get the full path of the file
#                     full_path = os.path.join(root, file)
#                     # Write the full path to the text file
#                     txt_file.write(full_path + "\n")

def list_png_files(main_folder):
    # FOR LABELS
    # Open the text file in write mode
    with open("label.txt", "w") as txt_file:
        # Walk through the main folder and its subdirectories
        for root, dirs, files in os.walk(main_folder):
            for file in files:
                # Check if the file ends with "gtFine_labelColors.png"
                if file.endswith("gtFine_labelColors.png"):
                    # Get the full path of the file
                    full_path = os.path.join(root, file)
                    # Write the full path to the text file
                    txt_file.write(full_path + "\n")

main_folder = 'C:/Users/hp/Documents/code/Py/actual/Ai/inter_boot_2024/semseg/dataset/interboot/labels'
list_png_files(main_folder)
