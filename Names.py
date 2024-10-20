import os
import pandas as pd

def update_name_in_files(file1_path, file2_path, new_name):
    # Function to update the 'Name = ' line in both files
    def update_name_in_content(content, new_name):
        updated_content = []
        for line in content:
            if line.startswith("Name = "):
                updated_content.append(f"Name = {new_name}\n")
            else:
                updated_content.append(line)
        return updated_content

    # Check if files exist
    if os.path.exists(file1_path) and os.path.exists(file2_path):
        # Read, update, and save the changes in both files with utf-8 encoding
        with open(file1_path, 'r', encoding='utf-8') as file1:
            content1 = file1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as file2:
            content2 = file2.readlines()

        updated_content1 = update_name_in_content(content1, new_name)
        updated_content2 = update_name_in_content(content2, new_name)

        # Save the updated content back to the files with utf-8 encoding
        with open(file1_path, 'w', encoding='utf-8') as file1:
            file1.writelines(updated_content1)
        with open(file2_path, 'w', encoding='utf-8') as file2:
            file2.writelines(updated_content2)

        print(f"Successfully updated 'Name =' in {file1_path} and {file2_path}.\n")
    else:
        print(f"One or both files {file1_path} or {file2_path} do not exist.\n")

def main():
    # Load the Excel file
    excel_file = "Names.xlsx"
    
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print(f"File {excel_file} not found.")
        return

    # Assuming that column A has file names and column B has new names
    for index, row in df.iterrows():
        base_name = row[0]  # Column A - file name (e.g., 'Angez')
        new_name = row[1]   # Column B - new name to replace (e.g., 'Bruno')

        # Construct file paths
        file1_path = f"{base_name}.ini"
        file2_path = f"{base_name}FullArt.ini"

        # Perform the update
        update_name_in_files(file1_path, file2_path, new_name)

if __name__ == "__main__":
    main()