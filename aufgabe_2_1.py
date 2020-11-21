# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def find_pos1(string, symbol):
    for counter, value in enumerate(string):
        if value == symbol:
            return counter 
    return -1

def find_pos2(string, symbol):
    if symbol in string:
        return string.index(symbol)
    else:
        return -1


# task 2a
# string = "Gestern war ich Erdbeeren ernten!"
# symbol = "e"
# string = "Abbild/JRTSm"
# symbol = "/"
# res = find_pos1(string, symbol)
# print(string)
# print(res)
# res = find_pos2(string, symbol)
# print(string)
# print(res)

filename    = "de_DE_frami.dic"
file        = open(filename, "r")
content     = file.readlines()
file.close()

filename    = "dictionary.txt"
file        = open(filename, "w")

symbol = "/"

for counter, line in enumerate(content):
    if (line == "\n") or (line == "\t\n") or (line[0] == "#"):
        pass
    else:
        index = find_pos1(line, symbol)
        # to prevent an empty line at the end
        if counter < (len(content)-1):
            file.write(line[:index]+"\n")
        else:
            file.write(line[:index])

file.close()