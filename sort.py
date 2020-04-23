# This is a simple folder sorting app that will sort your files based on their extensions and will move them in an output folder having sub directories based on the extensions
# Using os and shutil module


import os
import shutil


# Getting the directory

directory = input('Enter the desired directory::')

# Changing the dirctory

os.chdir(directory)

for root, dirs, files in os.walk(directory):
    for filed in files:
        fn, fext = os.path.splitext(filed)
        fext = fext[1:]
        # Checking if the directory exists or not
        if not os.path.exists(os.path.join('out', fext)):
            # If not then making one
            os.makedirs(os.path.join('out', fext))
            shutil.move(f'{root}\{filed}', f'{directory}\out\{fext}')
        else:
            # IF we donot do try and error it will give an error when the file is already at the output directory
            try:
                shutil.move(f'{root}\{filed}', f'{directory}\out\{fext}')
            except Exception:
                continue
