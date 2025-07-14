import shutil

# Compress the "my_folder" directory into a ZIP archive
shutil.make_archive("backup", "zip", "shutil")

print("Folder compressed successfully!")
