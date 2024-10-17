import os
import shutil

def organise_splice(top_folder):
    # Traverse the folder tree recursively
    for root, dirs, files in os.walk(top_folder):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                destination_path = os.path.join(top_folder, file)

                # If the file already exists in the destination folder, rename it to avoid overwriting
                if os.path.exists(destination_path):
                    base, extension = os.path.splitext(file)
                    count = 1
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(top_folder, f"{base}_{count}{extension}")
                        count +=1

                #Move the wav file to the top top_folder
                shutil.move(file_path, destination_path)
                print(f"Moved: {file_path} -> {destination_path}")

        print("All .wav files have been moved to the top folder. ")

if __name__ == "__main__":
    # Replace this with the path to your top top_folder
    top_folder = input("Enter the path to the top-level folder: " )

    if os.path.isdir(top_folder):
        organise_splice(top_folder)
    else:
        print("The provided path is not a valid directory.")
