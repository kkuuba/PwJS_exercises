import re

with open("data_file.txt", "r+") as file:
    data = file.read()
    file.close()

replace_dict = {
    " oraz ": r"\si\s",
    " i ": r"\soraz\s",
    " prawie nigdy ": r"\snigdy\s",
    " czemu ": r"\sdlaczego\s"
}


for word in replace_dict.keys():
    output_data = replace_dict[word].sub(r"/{}".format(group), replace_dict[group])

with open("data_file_out.txt", "w+") as file:
    file.write(output_data)
    file.close()