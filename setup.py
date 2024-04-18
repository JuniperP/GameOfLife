import os
import shutil

def zip_directory(source_dir, target):
    """
    Compresses a directory into a zip file.

    :param str source_dir: the directory to be compressed
    :param str target_dir: the target directory for the zip file
    """
    shutil.make_archive(base_name=target, format="zip", root_dir=source_dir)

def main():
    """
    The main function of the setup.py script.
    """
    # Create the zip files for the packages
    source_dir = os.path.join("py", "src")
    target_dir = os.path.join("py", "packaged", "src")
    zip_directory(source_dir, target_dir)

if __name__ == "__main__":
    main()
