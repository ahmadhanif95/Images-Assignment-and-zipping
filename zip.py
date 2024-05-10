import os
import zipfile

def zip_folders(start_folder, end_folder):
    for i in range(start_folder, end_folder + 1):
        folder_name = f"A_{i}"
        folder_path = os.path.join(os.getcwd(), folder_name)
        zip_path = f"{folder_name}.zip"
        
        if os.path.exists(folder_path):
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
            print(f"Folder {folder_name} zipped successfully.")
        else:
            print(f"Folder {folder_name} does not exist.")

if __name__ == "__main__":
    start_folder = 1
    end_folder = 10
    zip_folders(start_folder, end_folder)

