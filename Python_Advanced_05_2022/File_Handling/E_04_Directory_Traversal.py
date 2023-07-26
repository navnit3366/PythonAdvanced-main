from os import listdir
from os.path import isdir, join


def dir_traversal(path, files_dict):
    for element in listdir(path):
        if isdir(join(path, element)):
            dir_traversal(join(path, element), files_dict)
        else:
            file_split = element.split(".")
            file_name = file_split[0]
            file_ext = file_split[1]
            if file_ext in files_dict:
                files_dict[file_ext].append(file_name)
            else:
                files_dict[file_ext] = [file_name]
    return files_dict


user_dir_path = input("Please input directory path:")
files = dir_traversal(user_dir_path, {})


with open(join(user_dir_path, "report.txt"), "a") as file:
    for extensions, names in sorted(files.items()):
        file.writelines(f".{extensions}\n")
        for name in names:
            file.writelines(f"- - - {name}.{extensions}\n")
