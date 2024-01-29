import os
import shutil

def sort_files(directory):
    for filename in os.listdir(directory):
        ext = os.path.splitext(filename)[-1].lower()
        ext_folder = os.path.join(directory, ext)
        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)
        shutil.move(os.path.join(directory, filename), os.path.join(ext_folder, filename))

sort_files(r"/path/to/your/directory")
