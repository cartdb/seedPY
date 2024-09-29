import os
import zipfile
folder = '../roms'
extension = ".zip"
for item in os.listdir(folder):
    if item.endswith(extension):
        zipfile.ZipFile(item).extractall()
for item in os.listdir(folder):
    if item.endswith(extension):
        zipfile.ZipFile(item).extractall()
os.system("del *.zip")