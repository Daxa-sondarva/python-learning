import zipfile

# Create a ZIP file and add files to it
with zipfile.ZipFile("my_archive.zip", "w") as zipf:
    zipf.write("example.txt")  # Add example.txt
    zipf.write("example2.txt")  # Add example.txt

print("ZIP file created successfully!")


