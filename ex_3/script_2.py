with open("data_file.txt", "r+") as file:
    data = file.read()
    file.close()

replace_dict = {
    " i ": " oraz ",
    " oraz ": " i ",
    " nigdy ": " prawie nigdy ",
    " dlaczego ": " czemu "
}

for word in replace_dict:
    data = data.replace(word, replace_dict[word])

with open("data_file_out.txt", "w+") as file:
    file.write(data)
    file.close()
