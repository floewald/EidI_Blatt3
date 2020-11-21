# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def getIndex(word, content):
    for index, line in enumerate(content):
        word_dict = line.strip("\n")
        if word == word_dict:
            return index
    return -1

filename    = "dictionary.txt"
file        = open(filename, "r")
content     = file.readlines()
word        = input("Pleas enter a word you are lookin for:\n")
index       = getIndex(word, content)

if index == -1:
    print("Your word / input is not in the dictionary!")
    print("Index: {}".format(index))
else:
    print("Your entered word is at index {} of the dictionary.".format(index))