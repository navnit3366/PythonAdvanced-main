import os
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
root.attributes('-topmost', True)
# file_path = filedialog.askdirectory()
# print(file_path)

files_dict = {}
list_dir = os.listdir(filedialog.askdirectory())
for file_n in list_dir:
    file_split = file_n.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    if file_ext in files_dict:
        files_dict[file_ext].append(file_name)
    else:
        files_dict[file_ext] = [file_name]

with open("report.txt", "a") as file:
    for extensions, names in sorted(files_dict.items()):
        file.writelines(f".{extensions}\n")
        for name in names:
            file.writelines(f"- - - {name}.{extensions}\n")


# a = os.listdir(filedialog.askdirectory())
# print(a)

