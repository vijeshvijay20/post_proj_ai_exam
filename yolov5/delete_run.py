import shutil
import os 

def delete_folder_if_exists(folder_path):
    try:
        # Check if the folder exists
        if os.path.exists(folder_path):
            # If it exists, delete it and its contents
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' and its contents deleted.")
        else:
            print(f"Folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

