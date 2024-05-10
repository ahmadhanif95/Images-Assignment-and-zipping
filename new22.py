import os
import shutil
import random

# Define source folder
source_folder = '25april24_0k_9k'
# Define destination folder prefix
destination_folder_prefix = 'A_'

# Create destination folders
def create_destination_folders(num_folders):
    for i in range(num_folders):
        folder_name = f"{destination_folder_prefix}{i+1}"
        os.makedirs(folder_name, exist_ok=True)

# Function to copy images to destination folders
def copy_images_to_folders(num_images, num_folders):
    with os.scandir(source_folder) as entries:
        images = [entry.name for entry in entries if entry.is_file()]
    random.shuffle(images)  # Shuffle images list randomly
    images_per_folder = num_images // num_folders
    for folder_index in range(num_folders):
        folder_name = f"{destination_folder_prefix}{folder_index+1}"
        for _ in range(images_per_folder):
            if images:  # Ensure there are still images left
                random_image = images.pop()  # Get and remove a random image from the list
                source_path = os.path.join(source_folder, random_image)
                # Copy the image to the destination folder
                shutil.copy(source_path, folder_name)

# Calculate number of images in source folder
num_images = len(os.listdir(source_folder))
# Calculate number of folders needed
num_folders = (num_images // 1000) + 1

# Create destination folders
create_destination_folders(num_folders)
# Copy images to destination folders
copy_images_to_folders(num_images, num_folders)

