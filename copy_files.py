import os
import shutil

def copy_recursive(src, dst):
    """
    Recursively copies a directory tree, similar to `cp -r`.
    Creates destination directories as needed.
    """
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            copy_recursive(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)

if __name__ == "__main__":
    source_dir = "/tmp/klpms_manual"
    destination_dir = "/app/klpms_manual_app"

    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
    else:
        print(f"Copying files from '{source_dir}' to '{destination_dir}'...")
        copy_recursive(source_dir, destination_dir)
        print("Copy complete.")
