# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
#task 3a
def read_line(string):
    n = string.count(",")
    if n == 2:
        if ", " in string:
            values = string.split(", ")
        elif "," in string:
            values = string.split(",")
        return (values[0], values[1], values[2])
    else:
        print("There are not 2 comma!")
        print("Terminate script")
        exit()

#task 3b
def read_file(file):
    content = file.readlines()
    filmtupels = []
    for line in content:
        filmtupels.append(read_line(line.strip("\n")))
    
    return filmtupels

#task 3c
def has_actor(filmtupels, actor):
    for listentry in filmtupels:
        if listentry[1] == actor:
            return True
        # or if only a part of the name is entered as string
        # if actor in listentry[1]:
        #     return True
    return False

# task 3d
def actor_collabration(filmtupel, actor):
    movies = [m[0] for m in filmtupel if m[1] == actor]
    actors = list(set([n[1] for m in movies for n in filmtupel if m == n[0] and n[1] != actor]))
    return sorted(actors)

# task 3e
def insert(filmtupel, t):
    newtupel = filmtupel[:]
    for index, m in enumerate(filmtupel):
        if m[2] > t[2]:
            newtupel.insert(index, t)
            return newtupel


string = "The Fugitive, Harrison Ford, Andrew Davis"
filmtupel = read_line(string)
print(filmtupel)

filename    = "hollywood.csv"
file        = open(filename, "r")
filmtupel   = read_file(file)
file.close()
print(filmtupel[0])

actor       = "Harrison Ford"
isInlist    = has_actor(filmtupel, actor)
print(isInlist)

actors = actor_collabration(filmtupel, actor)
print(actors)

newtupel = insert(filmtupel, ("Hallo", "Liam Neelson", "Severin Emmerswald"))
for m in filmtupel:
    print(m)

print()

for m in newtupel:
    print(m)