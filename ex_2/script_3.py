import os


def change_ext(dest_path):
    files_names = os.listdir(dest_path)
    for file in files_names:
        if file.split(".")[1] == "jpeg":
            os.rename("{}/{}".format(dest_path, file), "{}/{}.{}".format(dest_path, file.split(".")[0], "png"))


change_ext("files")
