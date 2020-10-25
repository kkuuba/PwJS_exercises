import os


def list_files(path):
    all_files = os.listdir("/{}".format(path))
    for file in all_files:
        if os.path.isdir("{}/{}".format(path, file)):
            print("{} -> ".format(file))
            list_files("{}/{}".format(path, file))
        else:
            print(file)


list_files("/dev")
