import os
import shutil
import argparse
from pathlib import Path

def parse_folder(src_path, dest_path):
    try:
        for element in src_path.iterdir():
            if element.is_dir():
                parse_folder(element, dest_path)
            elif element.is_file():
                copy_file_to_dest(element, dest_path)
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file_to_dest(file_path, dest_path):
    extension = file_path.suffix[1:]  # Get the file extension without the dot
    new_dir = dest_path / extension
    
    if not new_dir.exists():
        new_dir.mkdir(parents=True)
    
    dest_file_path = new_dir / file_path.name
    shutil.copy2(file_path, dest_file_path)
    print(f"Copied '{file_path}' to '{dest_file_path}'")

def main():
    parser = argparse.ArgumentParser(description='Copy and sort files based on extension.')
    parser.add_argument('src_dir', type=str, help='Path to the source directory')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Path to the destination directory (default: dist)')

    args = parser.parse_args()
    
    src_path = Path(args.src_dir)
    dest_path = Path(args.dest_dir)

    if not src_path.exists():
        print(f"Source directory '{src_path}' does not exist.")
        return
    
    if not dest_path.exists():
        dest_path.mkdir(parents=True)

    parse_folder(src_path, dest_path)
    print(f"All files have been copied and sorted into '{dest_path}'")

if __name__ == "__main__":
    main()
