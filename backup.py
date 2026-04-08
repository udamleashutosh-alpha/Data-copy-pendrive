import os
import shutil

def backup_data(source, destination):
    if not os.path.exists(source):
        print("Source folder not found!")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    print("Copying files...")

    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)

        try:
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        except Exception as e:
            print(f"Error: {e}")

    print("Backup completed!\n")