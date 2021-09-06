import zipfile

with zipfile.ZipFile("supermarkets.zip", 'r') as zip_ref:
    zip_ref.extractall()

with zipfile.ZipFile("supermarkets+TXT+files.zip", 'r') as zip_ref:
    zip_ref.extractall()