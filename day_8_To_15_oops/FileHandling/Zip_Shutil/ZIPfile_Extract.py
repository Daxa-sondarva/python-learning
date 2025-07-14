import zipfile

# Open an existing ZIP file and extract all files
with zipfile.ZipFile("my_archive.zip", "r") as zipf:
    zipf.extractall("extracted_files")  # Extract to "extracted_files" folder

print("ZIP file extracted successfully!")
