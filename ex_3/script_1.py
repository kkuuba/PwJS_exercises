import re

with open("data_file.txt", "r+") as file:
    data = file.read()
    file.close()

regex_to_del = re.compile(r"(\ssię\s|\si\s|\soraz\s|\snigdy\s|\sdlaczego\s)")
output_data = regex_to_del.sub(" ", data)

with open("data_file_out.txt", "w+") as file:
    file.write(output_data)
    file.close()
