try:
    file = open("songs.dat")
except:
    print("no songs.dat file found")

songs = file.read().splitlines()

for song in range(len(songs)):
    songs[song] = songs[song].split()

print(songs)
