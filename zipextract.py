import os
import zipfile
folder = '../roms'
extension = ".zip"
lists = []
for item in os.listdir(folder):
    if item.endswith(extension):
        lists.append(item)
        zipfile.ZipFile(item).extractall()
for items in range(len(lists)):
    os.system("del " + lists[items])
for item in os.listdir(folder):
    if item.endswith(extension):
        zipfile.ZipFile(item).extractall()
os.system("del *.zip")