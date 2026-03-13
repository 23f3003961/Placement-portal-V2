import zipfile
import os

def zip_folder(folder_path, output_zip):
    folder_path = os.path.abspath(folder_path)

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Preserve folder structure inside zip
                arcname = os.path.relpath(file_path, os.path.dirname(folder_path))

                zipf.write(file_path, arcname)

# Folder you want to zip
zip_folder("placement-portal-v2", "placement_portal_23f3003961.zip")

print("Zip file created successfully!")