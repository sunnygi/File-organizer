import os
import shutil
import logging

# Configure logging
logging.basicConfig(filename="file_organizer.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".apk", ".bat", ".sh"],
    "Others": []  # Files that don't match any category
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        logging.error("The specified folder does not exist.")
        return

    files = os.listdir(folder_path)
    
    if not files:
        print("No files found in the folder.")
        logging.info("No files found in the folder.")
        return

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):  # Ensure it's a file, not a folder
            file_extension = os.path.splitext(file)[1].lower()
            folder_name = "Others"

            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    folder_name = category
                    break

            target_folder = os.path.join(folder_path, folder_name)
            os.makedirs(target_folder, exist_ok=True)

            try:
                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} → {folder_name}")
                logging.info(f"Moved: {file} → {folder_name}")
            except Exception as e:
                print(f"Error moving {file}: {e}")
                logging.error(f"Error moving {file}: {e}")

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ")
    organize_files(folder_to_organize)