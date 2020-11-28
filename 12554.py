
N = int(input())

song = [x for x in "Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you".split()]
name = []
for i in range(N):
    n = input()
    name.append(n)

if N <= len(song):

    for i in range (len(song)):
        name.append(name[i])
    for j in range (len(song)):
        print("{}: {}".format(name[j], song[j]))
elif N > len(song):
    v = len(song) - (len(name) % (len(song)))
    for o in range(v):
        name.append(name[o])
    for i in range(len(name)):
        song.append(song[i])
    for j in range (len(name)):
        print("{}: {}".format(name[j], song[j]))

