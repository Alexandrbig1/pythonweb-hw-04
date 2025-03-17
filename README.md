# pythonweb-hw-04

## Description

This Python script reads all files in a user-specified source folder and distributes them into subfolders in a destination directory based on file extensions. The script performs sorting asynchronously for more efficient processing of a large number of files.

## Technical Description

1. Import necessary asynchronous libraries.
2. Create an `ArgumentParser` object to handle command-line arguments.
3. Add required arguments to specify the source and target folders.
4. Initialize asynchronous paths for the source and target folders.
5. Write an asynchronous function `read_folder` that recursively reads all files in the source folder and its subfolders.
6. Write an asynchronous function `copy_file` that copies each file into the corresponding subfolder in the target folder based on its extension.
7. Set up error logging.
8. Run the asynchronous `read_folder` function in the main block.
